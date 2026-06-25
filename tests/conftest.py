from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest
from click.testing import CliRunner

from pyhtb.cli import common


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def fake_sdk(monkeypatch):
    """Patch ``get_sdk()`` (via ``common.PyHTB``) to return a MagicMock SDK.

    ``get_sdk`` reads a token then constructs ``common.PyHTB(token=...)``; both
    are looked up in ``common``'s namespace at call time, so patching here covers
    every command module that imported ``get_sdk``.
    """
    sdk = MagicMock()
    monkeypatch.setenv("HTB_TOKEN", "test-token")
    monkeypatch.setattr(common, "PyHTB", lambda token: sdk)
    return sdk


@pytest.fixture
def no_token(monkeypatch):
    """Make token resolution return nothing, so ``get_sdk()`` aborts."""
    monkeypatch.setattr(common.config, "load_token", lambda: None)


def ns(**kwargs):
    """Shorthand for building a typed-ish response object with concrete values."""
    return SimpleNamespace(**kwargs)
