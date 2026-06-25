"""Unit tests for pure CLI helpers (no SDK calls)."""

import io
from types import SimpleNamespace

from pyhtb.cli import config, formatter
from pyhtb.cli.common import resolve_id
from pyhtb.cli.commands.vpn import _extract_ovpn_payload


# --- resolve_id -------------------------------------------------------------

def test_resolve_id_numeric_passthrough():
    # A numeric target is returned directly without hitting the search function.
    called = []
    assert resolve_id("42", lambda **kw: called.append(kw)) == 42
    assert called == []


def test_resolve_id_exact_name_match():
    data = [SimpleNamespace(id=1, name="Other"), SimpleNamespace(id=7, name="Target")]
    search = lambda **kw: SimpleNamespace(data=data)
    assert resolve_id("target", search) == 7  # case-insensitive


def test_resolve_id_no_match_returns_none():
    search = lambda **kw: SimpleNamespace(data=[SimpleNamespace(id=1, name="Nope")])
    assert resolve_id("missing", search) is None


def test_resolve_id_empty_results_returns_none():
    assert resolve_id("x", lambda **kw: SimpleNamespace(data=[])) is None


# --- formatters -------------------------------------------------------------

def test_format_os_known_and_unknown():
    assert "Linux" in formatter.format_os("Linux")
    assert "Windows" in formatter.format_os("Windows 10")
    assert "Solaris" in formatter.format_os("Solaris")  # passthrough
    assert formatter.format_os("") == "[other_os][/other_os]"


def test_format_difficulty():
    assert formatter.format_difficulty("Easy") == "[easy]Easy[/easy]"
    assert formatter.format_difficulty("Insane") == "[insane]Insane[/insane]"
    assert formatter.format_difficulty("") == ""


def test_format_status_truthy_variants():
    for owned in (True, 1, "Owned", "owned", "yes"):
        assert "Owned" in formatter.format_status(owned)
    assert "Not Owned" in formatter.format_status(False)
    assert "Not Owned" in formatter.format_status(0)


# --- _extract_ovpn_payload --------------------------------------------------

def test_extract_ovpn_from_bytesio():
    assert _extract_ovpn_payload(SimpleNamespace(payload=io.BytesIO(b"data"))) == "data"


def test_extract_ovpn_from_stringio():
    assert _extract_ovpn_payload(SimpleNamespace(payload=io.StringIO("data"))) == "data"


def test_extract_ovpn_from_raw_bytes_and_str():
    assert _extract_ovpn_payload(SimpleNamespace(payload=b"raw")) == "raw"
    assert _extract_ovpn_payload(SimpleNamespace(payload="raw")) == "raw"


def test_extract_ovpn_missing_payload():
    assert _extract_ovpn_payload(SimpleNamespace()) == ""
    assert _extract_ovpn_payload(None) == ""


# --- config token storage ---------------------------------------------------

def test_token_roundtrip(tmp_path, monkeypatch):
    token_file = tmp_path / "token"
    monkeypatch.setattr(config, "CONFIG_DIR", tmp_path)
    monkeypatch.setattr(config, "TOKEN_FILE", token_file)
    monkeypatch.delenv("HTB_TOKEN", raising=False)
    monkeypatch.delenv("HTB_API_KEY", raising=False)

    assert config.load_token() is None

    config.save_token("  secret  ")  # whitespace is stripped
    assert config.load_token() == "secret"
    # Stored with owner-only permissions.
    assert (token_file.stat().st_mode & 0o777) == 0o600

    config.delete_token()
    assert config.load_token() is None


def test_env_token_takes_precedence(monkeypatch):
    monkeypatch.setenv("HTB_TOKEN", "env-token")
    assert config.load_token() == "env-token"
