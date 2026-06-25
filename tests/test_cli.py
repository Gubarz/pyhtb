"""CLI command tests via CliRunner.

Scope: read-only commands and exit-code behavior. POST-backed commands
(own/start/stop/reset/switch/download) are intentionally not exercised here.
"""

from types import SimpleNamespace as NS

from pyhtb.cli.main import cli


def _machine(**over):
    base = dict(
        id=1, name="Blocky", os="Linux", difficulty_text="Easy", points=20,
        auth_user_in_user_owns=True, auth_user_in_root_owns=False,
        active=True, free=True,
    )
    base.update(over)
    return NS(**base)


def _machine_info(**over):
    base = dict(
        id=1, name="Blocky", os="Linux", difficulty_text="Easy", points=20,
        release=None, auth_user_in_user_owns=True, auth_user_in_root_owns=False,
        ip="10.10.10.1", maker=NS(name="ippsec"), maker2=None,
        play_info=NS(is_active=True, is_spawned=False),
    )
    base.update(over)
    return NS(**base)


def _challenge(**over):
    base = dict(
        id=1, name="Spookifier", category_name="Web", difficulty="Easy",
        solves=1234, is_owned=False, play_methods=["container"],
    )
    base.update(over)
    return NS(**base)


# --- no token ---------------------------------------------------------------

def test_missing_token_aborts_nonzero(runner, no_token):
    result = runner.invoke(cli, ["machine", "list"])
    assert result.exit_code != 0
    assert "No API token" in result.output


# --- machine list -----------------------------------------------------------

def test_machine_list_ok(runner, fake_sdk):
    fake_sdk.v5.get_machines.return_value = NS(data=[_machine(), _machine(id=2, name="Lame")])
    result = runner.invoke(cli, ["machine", "list"])
    assert result.exit_code == 0
    assert "Blocky" in result.output


def test_machine_list_empty_is_warning_not_failure(runner, fake_sdk):
    fake_sdk.v5.get_machines.return_value = NS(data=[])
    result = runner.invoke(cli, ["machine", "list"])
    assert result.exit_code == 0
    assert "No machines found" in result.output


# --- machine info (v4-direct, v5 fallback, not found) -----------------------

def test_machine_info_direct_hit(runner, fake_sdk):
    fake_sdk.v4.get_machine_profile.return_value = NS(info=_machine_info())
    result = runner.invoke(cli, ["machine", "info", "Blocky"])
    assert result.exit_code == 0
    assert "Blocky" in result.output
    # Resolved on the direct v4 call; no v5 search needed.
    fake_sdk.v5.get_machines.assert_not_called()


def test_machine_info_falls_back_to_v5_search(runner, fake_sdk):
    fake_sdk.v4.get_machine_profile.side_effect = [Exception("no direct"), NS(info=_machine_info(id=10))]
    fake_sdk.v5.get_machines.return_value = NS(data=[NS(id=10, name="Blocky")])
    result = runner.invoke(cli, ["machine", "info", "Blocky"])
    assert result.exit_code == 0
    fake_sdk.v5.get_machines.assert_called_once()


def test_machine_info_not_found_exits_nonzero(runner, fake_sdk):
    fake_sdk.v4.get_machine_profile.return_value = NS(info=None)
    fake_sdk.v5.get_machines.return_value = NS(data=[])
    result = runner.invoke(cli, ["machine", "info", "ghost"])
    assert result.exit_code != 0
    assert "not found" in result.output


# --- challenge list + category resolution -----------------------------------

def test_challenge_list_ok(runner, fake_sdk):
    fake_sdk.v4.get_challenges.return_value = NS(data=[_challenge()])
    result = runner.invoke(cli, ["challenge", "list"])
    assert result.exit_code == 0
    assert "Spookifier" in result.output


def test_challenge_list_resolves_category(runner, fake_sdk):
    fake_sdk.v4.get_challenge_categories_list.return_value = NS(info=[NS(id=3, name="Web")])
    fake_sdk.v4.get_challenges.return_value = NS(data=[_challenge()])
    result = runner.invoke(cli, ["challenge", "list", "--category", "web"])
    assert result.exit_code == 0
    # Resolved name -> id was forwarded to the API.
    assert fake_sdk.v4.get_challenges.call_args.kwargs["category"] == [3]


def test_challenge_list_unknown_category_exits_nonzero(runner, fake_sdk):
    fake_sdk.v4.get_challenge_categories_list.return_value = NS(info=[NS(id=3, name="Web")])
    result = runner.invoke(cli, ["challenge", "list", "--category", "Nope"])
    assert result.exit_code != 0
    assert "Unknown category" in result.output
    fake_sdk.v4.get_challenges.assert_not_called()


# --- vpn status -------------------------------------------------------------

def test_vpn_status_ok(runner, fake_sdk):
    item = NS(
        connection=NS(ip4="10.10.14.2"),
        server=NS(friendly_name="EU Free 1"),
        location_type_friendly="Europe",
        connection_type="OpenVPN",
    )
    fake_sdk.v4.get_connection_status.return_value = [item]
    result = runner.invoke(cli, ["vpn", "status"])
    assert result.exit_code == 0
    assert "10.10.14.2" in result.output


def test_vpn_status_none_is_warning(runner, fake_sdk):
    fake_sdk.v4.get_connection_status.return_value = None
    result = runner.invoke(cli, ["vpn", "status"])
    assert result.exit_code == 0
    assert "No active VPN" in result.output


# --- whoami / profile -------------------------------------------------------

def _profile(name="neo"):
    return NS(status_code=200, parsed=NS(user_stats=NS(
        name=name, id=1, rank="Pro Hacker", points=100, system_owns=5, user_owns=10,
    )))


def test_whoami_ok(runner, fake_sdk):
    fake_sdk.v4.get_user_profile_summary_detailed.return_value = _profile()
    result = runner.invoke(cli, ["whoami"])
    assert result.exit_code == 0
    assert "neo" in result.output


def test_whoami_auth_failure_exits_nonzero(runner, fake_sdk):
    fake_sdk.v4.get_user_profile_summary_detailed.return_value = NS(status_code=403, parsed=None)
    result = runner.invoke(cli, ["whoami"])
    assert result.exit_code != 0
    assert "Authentication failed" in result.output


# --- search -----------------------------------------------------------------

def test_search_ok(runner, fake_sdk):
    fake_sdk.v5.get_machines.return_value = NS(data=[_machine(name="Void")])
    fake_sdk.v4.get_challenges.return_value = NS(data=[_challenge(name="VoidChal")])
    result = runner.invoke(cli, ["search", "void"])
    assert result.exit_code == 0
    assert "Void" in result.output


# --- unhandled exception is caught by the decorator -------------------------

def test_unexpected_exception_is_friendly_and_nonzero(runner, fake_sdk):
    fake_sdk.v5.get_machines.side_effect = RuntimeError("boom")
    result = runner.invoke(cli, ["machine", "list"])
    assert result.exit_code != 0
    assert "Failed to fetch machines" in result.output
    assert "boom" in result.output
