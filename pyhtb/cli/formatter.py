from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.theme import Theme
from rich import box
from typing import Any, List, Dict, Union

# Define a premium color theme for HTB terminal
HTB_THEME = Theme({
    "info": "cyan",
    "success": "green",
    "warning": "yellow",
    "error": "red",
    "easy": "green",
    "medium": "dark_orange",
    "hard": "red",
    "insane": "magenta",
    "linux": "cyan",
    "windows": "bright_blue",
    "other_os": "white",
})

console = Console(theme=HTB_THEME)

def format_os(os_name: str) -> str:
    """Returns formatted OS name with matching emoji."""
    os_lower = os_name.lower() if os_name else ""
    if "linux" in os_lower:
        return "[linux]Linux 🐧[/linux]"
    elif "windows" in os_lower:
        return "[windows]Windows 🪟[/windows]"
    elif "freebsd" in os_lower or "bsd" in os_lower:
        return "[error]FreeBSD 😈[/error]"
    return f"[other_os]{os_name}[/other_os]"

def format_difficulty(diff_name: str) -> str:
    """Returns formatted difficulty name with theme colors."""
    if not diff_name:
        return ""
    diff_lower = diff_name.lower()
    if "easy" in diff_lower:
        return f"[easy]{diff_name}[/easy]"
    elif "medium" in diff_lower:
        return f"[medium]{diff_name}[/medium]"
    elif "hard" in diff_lower:
        return f"[hard]{diff_name}[/hard]"
    elif "insane" in diff_lower:
        return f"[insane]{diff_name}[/insane]"
    return diff_name

def format_status(is_owned: Union[bool, int, str]) -> str:
    """Formats flags status as Owned or Not Owned."""
    if is_owned in (True, 1, "Owned", "owned", "Y", "yes"):
        return "[success]Owned ✓[/success]"
    return "[error]Not Owned ✗[/error]"

def print_success(message: str) -> None:
    console.print(f"[success][+][/success] {message}")

def print_info(message: str) -> None:
    console.print(f"[info][*][/info] {message}")

def print_error(message: str) -> None:
    console.print(f"[error][✗][/error] {message}")

def print_warning(message: str) -> None:
    console.print(f"[warning][!][/warning] {message}")

def render_table(title: str, headers: List[str], rows: List[List[Any]]) -> None:
    """Renders a beautiful table with rich."""
    table = Table(title=f"[info]{title}[/info]", show_header=True, header_style="bold magenta", box=box.ROUNDED)
    
    for header in headers:
        table.add_column(header)
        
    for row in rows:
        # Convert all elements to strings
        table.add_row(*[str(item) for item in row])
        
    console.print(table)

def render_details(title: str, details: Dict[str, Any]) -> None:
    """Renders a panel of key-value details."""
    content = ""
    for k, v in details.items():
        content += f"[bold magenta]{k:<16}[/bold magenta]: {v}\n"
    
    panel = Panel(content.strip(), title=f"[info]{title}[/info]", border_style="cyan", expand=False)
    console.print(panel)

def print_api_error(action: str, detailed) -> None:
    """Formats and prints an API error, handling raw HTML error payloads gracefully."""
    status = detailed.status_code
    content = detailed.content.decode(errors="replace").strip()
    
    if content.startswith("<!DOCTYPE html") or "html" in content.lower()[:100]:
        print_error(f"Failed to {action}: Received HTTP {status} (HTML Error Page). The resource might not exist or the action is invalid.")
    else:
        import json
        try:
            data = json.loads(content)
            msg = data.get("message", content)
            print_error(f"Failed to {action}: {msg}")
        except Exception:
            print_error(f"Failed to {action}: {content}")
