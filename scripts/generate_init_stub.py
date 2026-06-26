"""Generate the public pyhtb facade and typing stub from endpoint modules."""

from __future__ import annotations

import ast
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYHTB = ROOT / "pyhtb"
INIT_OUTPUT = PYHTB / "__init__.py"
STUB_OUTPUT = PYHTB / "__init__.pyi"

PACKAGES = [
    ("v4", PYHTB / "v4" / "api", "V4"),
    ("v5", PYHTB / "v5" / "api", "V5"),
    ("experience_v1", PYHTB / "experience" / "v1" / "api", "ExpV1"),
]

TARGET_CLASSES = {
    "v4": ("ClientV4", "AuthenticatedClientV4"),
    "v5": ("ClientV5", "AuthenticatedClientV5"),
    "experience_v1": ("ClientV1", "AuthenticatedClientV1"),
}

FUNC_TO_METHOD = {
    "sync": ("", False),
    "sync_detailed": ("_detailed", False),
    "asyncio": ("_async", True),
    "asyncio_detailed": ("_async_detailed", True),
}

SKIP_MODULES = {"typing", "http", "urllib.parse", "io"}
SKIP_NAMES = {
    "Any",
    "AuthenticatedClient",
    "BytesIO",
    "Client",
    "HTTPStatus",
    "errors",
    "quote",
}

TYPE_IMPORT_RE = re.compile(r"^from \.\.\.types import (?P<names>.+)$", re.MULTILINE)


class RewriteNames(ast.NodeTransformer):
    """Rewrite endpoint-local names to globally unique facade aliases."""

    def __init__(self, names: dict[str, str]) -> None:
        self.names = names

    def visit_Name(self, node: ast.Name) -> ast.AST:
        if node.id in self.names:
            return ast.copy_location(ast.Name(id=self.names[node.id], ctx=node.ctx), node)
        return node


def module_name_for(path: Path) -> str:
    return ".".join(path.with_suffix("").relative_to(ROOT).parts)


def alias_for_module(module: str, prefix: str) -> str:
    parts = module.split(".api.", maxsplit=1)[-1].split(".")
    return prefix + "Api" + "".join(part.title().replace("_", "") for part in parts)


def resolve_import_module(current_module: str, node: ast.ImportFrom) -> str:
    if node.level == 0:
        return node.module or ""

    parts = current_module.split(".")
    base = ".".join(parts[: -node.level])
    return f"{base}.{node.module}" if node.module else base


def collect_import_aliases(
    tree: ast.Module,
    module: str,
    prefix: str,
) -> tuple[list[str], dict[str, str]]:
    imports: list[str] = []
    names: dict[str, str] = {}
    used_aliases: set[str] = set()

    for node in tree.body:
        if not isinstance(node, ast.ImportFrom):
            continue

        target_mod = resolve_import_module(module, node)
        if target_mod in SKIP_MODULES or target_mod.endswith(".client"):
            continue

        for alias in node.names:
            original = alias.asname or alias.name
            if alias.name in SKIP_NAMES or original in SKIP_NAMES:
                continue

            stub_alias = f"{prefix}{alias.name}"
            counter = 2
            while stub_alias in used_aliases:
                stub_alias = f"{prefix}{alias.name}{counter}"
                counter += 1

            used_aliases.add(stub_alias)
            imports.append(f"from {target_mod} import {alias.name} as {stub_alias}")
            names[original] = stub_alias

    return imports, names


def referenced_names(node: ast.AST) -> set[str]:
    return {child.id for child in ast.walk(node) if isinstance(child, ast.Name)}


def add_missing_type_aliases(
    tree: ast.Module,
    module: str,
    prefix: str,
    imports: list[str],
    names: dict[str, str],
) -> None:
    used: set[str] = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            used.update(referenced_names(node.args))
            if node.returns is not None:
                used.update(referenced_names(node.returns))

    package_root = module.split(".api.", maxsplit=1)[0]
    for name in sorted(used & {"UNSET", "Unset"}):
        if name in names:
            continue
        alias = f"{prefix}{name}"
        imports.append(f"from {package_root}.types import {name} as {alias}")
        names[name] = alias


def rewrite_expr(expr: ast.expr, names: dict[str, str]) -> ast.expr:
    rewritten = RewriteNames(names).visit(ast.fix_missing_locations(expr))
    return ast.fix_missing_locations(rewritten)  # type: ignore[return-value]


def format_arg(
    arg: ast.arg,
    default: ast.expr | None,
    names: dict[str, str],
    *,
    stub: bool,
) -> str:
    text = arg.arg
    if arg.annotation is not None:
        text += f": {ast.unparse(rewrite_expr(arg.annotation, names))}"
    if default is not None:
        text += " = ..." if stub else f" = {ast.unparse(rewrite_expr(default, names))}"
    return text


def signature_parts(
    func: ast.FunctionDef | ast.AsyncFunctionDef,
    names: dict[str, str],
    *,
    stub: bool,
) -> tuple[list[str], list[str], list[str], str]:
    args = func.args
    defaults = [None] * (len(args.args) - len(args.defaults)) + list(args.defaults)
    positional: list[str] = []
    keyword_only: list[str] = []
    call_args: list[str] = []

    for arg, default in zip(args.args, defaults):
        if arg.arg == "client":
            continue
        positional.append(format_arg(arg, default, names, stub=stub))
        call_args.append(f"{arg.arg}={arg.arg}")

    for arg, default in zip(args.kwonlyargs, args.kw_defaults):
        if arg.arg == "client":
            continue
        keyword_only.append(format_arg(arg, default, names, stub=stub))
        call_args.append(f"{arg.arg}={arg.arg}")

    return_type = "Any"
    if func.returns is not None:
        return_type = ast.unparse(rewrite_expr(func.returns, names))

    return positional, keyword_only, call_args, return_type


def stub_method_signature(
    func: ast.FunctionDef | ast.AsyncFunctionDef,
    method_name: str,
    names: dict[str, str],
    is_async: bool,
) -> str:
    positional, keyword_only, _, return_type = signature_parts(func, names, stub=True)
    signature = ["self"]
    signature.extend(positional)
    if keyword_only:
        signature.append("*")
        signature.extend(keyword_only)
    prefix = "async def" if is_async else "def"
    return f"    {prefix} {method_name}({', '.join(signature)}) -> {return_type}: ..."


def runtime_method(
    func: ast.FunctionDef | ast.AsyncFunctionDef,
    module_alias: str,
    func_name: str,
    method_name: str,
    names: dict[str, str],
    is_async: bool,
) -> list[str]:
    positional, keyword_only, call_args, return_type = signature_parts(func, names, stub=False)
    signature = ["self"]
    signature.extend(positional)
    if keyword_only:
        signature.append("*")
        signature.extend(keyword_only)

    prefix = "async def" if is_async else "def"
    call_prefix = "return await" if is_async else "return"
    call_parts = ["client=self", *call_args]
    lines = [
        f"    {prefix} {method_name}({', '.join(signature)}) -> {return_type}:",
        f"        {call_prefix} {module_alias}.{func_name}(",
    ]
    lines.extend(f"            {part}," for part in call_parts)
    lines.append("        )")
    return lines


def dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result


def patch_missing_unset_imports() -> None:
    """Repair generated modules that reference Unset without importing it."""

    for _, api_dir, _ in PACKAGES:
        for path in sorted(api_dir.rglob("*.py")):
            if path.name == "__init__.py":
                continue

            text = path.read_text()
            if not re.search(r"\bUnset\b", text):
                continue

            match = TYPE_IMPORT_RE.search(text)
            if match is None:
                continue

            names = [name.strip() for name in match.group("names").split(",")]
            if "Unset" in names:
                continue

            names.append("Unset")
            replacement = "from ...types import " + ", ".join(names)
            path.write_text(text[: match.start()] + replacement + text[match.end() :])


def collect_facade() -> tuple[list[str], list[str], dict[str, list[str]], dict[str, list[str]]]:
    type_imports = [
        "from typing import Any, Optional",
        "from pyhtb.v4.client import AuthenticatedClient as AuthenticatedClientV4Gen, Client as ClientV4Gen",
        "from pyhtb.v5.client import AuthenticatedClient as AuthenticatedClientV5Gen, Client as ClientV5Gen",
        "from pyhtb.experience.v1.client import AuthenticatedClient as AuthenticatedClientV1Gen, Client as ClientV1Gen",
    ]
    endpoint_imports: list[str] = []

    runtime_methods: dict[str, list[str]] = {
        "ClientV4": [],
        "AuthenticatedClientV4": [],
        "ClientV5": [],
        "AuthenticatedClientV5": [],
        "ClientV1": [],
        "AuthenticatedClientV1": [],
    }
    stub_methods: dict[str, list[str]] = {class_name: [] for class_name in runtime_methods}

    for key, api_dir, prefix in PACKAGES:
        for path in sorted(api_dir.rglob("*.py")):
            if path.name == "__init__.py":
                continue

            module = module_name_for(path)
            module_alias = alias_for_module(module, prefix)
            endpoint_imports.append(f"from {module.rsplit('.', maxsplit=1)[0]} import {path.stem} as {module_alias}")

            tree = ast.parse(path.read_text())
            module_imports, names = collect_import_aliases(tree, module, prefix)
            add_missing_type_aliases(tree, module, prefix, module_imports, names)
            type_imports.extend(module_imports)

            functions = {
                node.name: node
                for node in tree.body
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            }

            for func_name, (suffix, is_async) in FUNC_TO_METHOD.items():
                func = functions.get(func_name)
                if func is None:
                    continue

                method_name = f"{path.stem}{suffix}"
                for class_name in TARGET_CLASSES[key]:
                    stub_methods[class_name].append(
                        stub_method_signature(func, method_name, names, is_async)
                    )
                    runtime_methods[class_name].extend(
                        runtime_method(func, module_alias, func_name, method_name, names, is_async)
                    )
                    runtime_methods[class_name].append("")

    return dedupe(type_imports), dedupe(endpoint_imports), runtime_methods, stub_methods


def build_runtime() -> str:
    type_imports, endpoint_imports, class_methods, _ = collect_facade()
    lines = [
        "# Generated by scripts/generate_init_stub.py.",
        "# Regenerate with ./api/regen.sh.",
        "from __future__ import annotations",
        "",
        "from typing import Any, Optional",
        "",
        "import httpx",
        *type_imports[1:],
        *endpoint_imports,
        "",
    ]

    for class_name, base in [
        ("ClientV4", "ClientV4Gen"),
        ("AuthenticatedClientV4", "AuthenticatedClientV4Gen"),
        ("ClientV5", "ClientV5Gen"),
        ("AuthenticatedClientV5", "AuthenticatedClientV5Gen"),
        ("ClientV1", "ClientV1Gen"),
        ("AuthenticatedClientV1", "AuthenticatedClientV1Gen"),
    ]:
        lines.append(f"class {class_name}({base}):")
        methods = class_methods[class_name]
        lines.extend(methods if methods else ["    pass"])
        lines.append("")

    lines.extend(
        [
            "class PyHTB:",
            "    def __init__(",
            "        self,",
            "        token: Optional[str] = None,",
            '        base_url_v4: str = "https://labs.hackthebox.com/api/v4",',
            '        base_url_v5: str = "https://labs.hackthebox.com/api/v5",',
            '        base_url_experience_v1: str = "https://labs.hackthebox.com/api/experience/v1",',
            "        timeout: Optional[float] = None,",
            "        verify_ssl: bool = True,",
            "    ) -> None:",
            "        httpx_timeout = httpx.Timeout(timeout) if timeout is not None else None",
            "",
            "        if token:",
            "            self.v4 = AuthenticatedClientV4(",
            "                base_url=base_url_v4,",
            "                token=token,",
            "                timeout=httpx_timeout,",
            "                verify_ssl=verify_ssl,",
            "            )",
            "            self.v5 = AuthenticatedClientV5(",
            "                base_url=base_url_v5,",
            "                token=token,",
            "                timeout=httpx_timeout,",
            "                verify_ssl=verify_ssl,",
            "            )",
            "            self.experience_v1 = AuthenticatedClientV1(",
            "                base_url=base_url_experience_v1,",
            "                token=token,",
            "                timeout=httpx_timeout,",
            "                verify_ssl=verify_ssl,",
            "            )",
            "        else:",
            "            self.v4 = ClientV4(",
            "                base_url=base_url_v4,",
            "                timeout=httpx_timeout,",
            "                verify_ssl=verify_ssl,",
            "            )",
            "            self.v5 = ClientV5(",
            "                base_url=base_url_v5,",
            "                timeout=httpx_timeout,",
            "                verify_ssl=verify_ssl,",
            "            )",
            "            self.experience_v1 = ClientV1(",
            "                base_url=base_url_experience_v1,",
            "                timeout=httpx_timeout,",
            "                verify_ssl=verify_ssl,",
            "            )",
            "",
            "",
            '__all__ = ["PyHTB"]',
        ]
    )

    return "\n".join(lines) + "\n"


def build_stub() -> str:
    type_imports, _, _, class_methods = collect_facade()
    lines = [
        "# Generated by scripts/generate_init_stub.py.",
        "# Regenerate with ./api/regen.sh.",
        *type_imports,
        "",
    ]

    for class_name, base in [
        ("ClientV4", "ClientV4Gen"),
        ("AuthenticatedClientV4", "AuthenticatedClientV4Gen"),
        ("ClientV5", "ClientV5Gen"),
        ("AuthenticatedClientV5", "AuthenticatedClientV5Gen"),
        ("ClientV1", "ClientV1Gen"),
        ("AuthenticatedClientV1", "AuthenticatedClientV1Gen"),
    ]:
        lines.append(f"class {class_name}({base}):")
        methods = class_methods[class_name]
        lines.extend(methods if methods else ["    pass"])
        lines.append("")

    lines.extend(
        [
            "class PyHTB:",
            "    v4: ClientV4 | AuthenticatedClientV4",
            "    v5: ClientV5 | AuthenticatedClientV5",
            "    experience_v1: ClientV1 | AuthenticatedClientV1",
            "    def __init__(",
            "        self,",
            "        token: Optional[str] = ...,",
            "        base_url_v4: str = ...,",
            "        base_url_v5: str = ...,",
            "        base_url_experience_v1: str = ...,",
            "        timeout: Optional[float] = ...,",
            "        verify_ssl: bool = ...,",
            "    ) -> None: ...",
            "",
            "__all__: list[str]",
        ]
    )

    return "\n".join(lines) + "\n"


def main() -> None:
    patch_missing_unset_imports()
    INIT_OUTPUT.write_text(build_runtime())
    STUB_OUTPUT.write_text(build_stub())


if __name__ == "__main__":
    main()
