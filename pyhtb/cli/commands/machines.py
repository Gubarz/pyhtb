import time

import click
from rich.progress import Progress, SpinnerColumn, TextColumn

from pyhtb.v4.models.spawn_request import SpawnRequest
from pyhtb.v5.models.get_machines_difficulty_item import GetMachinesDifficultyItem
from pyhtb.v5.models.get_machines_os_item import GetMachinesOsItem
from pyhtb.v5.models.get_machines_state_item import GetMachinesStateItem
from pyhtb.v5.models.get_machines_todo import GetMachinesTodo
from pyhtb.v5.models.own_request import OwnRequest

from .. import formatter
from ..common import fail, fail_api, get_sdk, handle_errors, resolve_id

SUCCESS_STATUS_CODES = {200, 201, 202}

# Boot polling: check every 5s for up to 5 minutes.
BOOT_POLL_TIMEOUT = 300
BOOT_POLL_INTERVAL = 5


@click.group(name="machine", help="Interact with Hack The Box machines")
def machine_group():
    pass


@machine_group.command(name="list", help="List machines on Hack The Box")
@click.option("--retired", is_flag=True, help="List retired machines instead of active ones")
@click.option("--todo", is_flag=True, help="List machines on your todo list")
@click.option(
    "--difficulty",
    type=click.Choice(["easy", "medium", "hard", "insane"], case_sensitive=False),
    help="Filter by difficulty",
)
@click.option(
    "--os",
    "os_name",
    type=click.Choice(["linux", "windows", "other"], case_sensitive=False),
    help="Filter by OS",
)
@click.option("--page", type=int, default=1, help="Page number (default: 1)")
@click.option("--limit", type=int, default=20, help="Number of machines to list (default: 20)")
@click.option("--search", "keyword", help="Search keyword")
@handle_errors("fetch machines")
def machines_list(retired, todo, difficulty, os_name, page, limit, keyword):
    sdk = get_sdk()
    state_item = GetMachinesStateItem.RETIRED if retired else GetMachinesStateItem.ACTIVE

    kwargs = {"state": [state_item], "page": page, "per_page": limit}
    if difficulty:
        kwargs["difficulty"] = [GetMachinesDifficultyItem(difficulty.lower())]
    if os_name:
        kwargs["os"] = [GetMachinesOsItem(os_name.lower())]
    if todo:
        kwargs["todo"] = GetMachinesTodo.VALUE_1
    if keyword:
        kwargs["keyword"] = keyword

    formatter.print_info("Fetching machines...")
    response = sdk.v5.get_machines(**kwargs)
    if not response or not response.data:
        formatter.print_warning("No machines found matching the criteria.")
        return

    rows = []
    for machine in response.data:
        if machine.auth_user_in_user_owns and machine.auth_user_in_root_owns:
            owned_status = "[success]Both ✓[/success]"
        elif machine.auth_user_in_user_owns:
            owned_status = "[success]User ✓[/success]"
        elif machine.auth_user_in_root_owns:
            owned_status = "[success]Root ✓[/success]"
        else:
            owned_status = "[error]None ✗[/error]"

        active_str = "[success]Yes[/success]" if machine.active else "[error]No[/error]"
        free_str = "[success]Free[/success]" if machine.free else "[warning]VIP[/warning]"

        rows.append(
            [
                machine.id,
                machine.name,
                formatter.format_os(machine.os),
                formatter.format_difficulty(machine.difficulty_text),
                machine.points,
                owned_status,
                active_str,
                free_str,
            ]
        )

    headers = ["ID", "Name", "OS", "Difficulty", "Points", "Owned", "Active", "Tier"]
    formatter.render_table("Hack The Box Machines", headers, rows)


@machine_group.command(name="info", help="Show details of a specific machine")
@click.argument("target")
@handle_errors("retrieve profile")
def machines_info(target):
    sdk = get_sdk()
    formatter.print_info(f"Retrieving profile for '{target}'...")

    # The v4 profile endpoint accepts IDs and some slug/alternate identifiers
    # directly; try it first and fall back to a v5 name search only if needed.
    try:
        response = sdk.v4.get_machine_profile(target)
    except Exception:
        response = None

    if not response or not getattr(response, "info", None):
        machine_id = resolve_id(target, sdk.v5.get_machines)
        if machine_id:
            response = sdk.v4.get_machine_profile(str(machine_id))

    if not response or not getattr(response, "info", None):
        fail(f"Machine '{target}' not found.")

    info = response.info
    is_active = bool(info.play_info and (info.play_info.is_active or info.play_info.is_spawned))

    details = {
        "ID": info.id,
        "Name": info.name,
        "OS": formatter.format_os(info.os),
        "Difficulty": formatter.format_difficulty(info.difficulty_text),
        "Points": info.points,
        "Release Date": info.release.strftime("%Y-%m-%d %H:%M:%S") if info.release else "N/A",
        "User Owned": formatter.format_status(info.auth_user_in_user_owns),
        "Root Owned": formatter.format_status(info.auth_user_in_root_owns),
        "IP Address": info.ip if is_active else "Not active",
        "Created By": info.maker.name if info.maker else "N/A",
    }
    if info.maker2:
        details["Co-Creator"] = info.maker2.name

    formatter.render_details(f"Machine: {info.name}", details)


@machine_group.command(name="active", help="Show active virtual machine details")
@handle_errors("retrieve active machine")
def machines_active():
    sdk = get_sdk()
    formatter.print_info("Checking active target machine...")
    response = sdk.v5.get_virtual_machine_active()
    if not response or not response.info:
        formatter.print_warning("No machine is currently active.")
        return

    info = response.info
    details = {
        "ID": info.id,
        "Name": info.name,
        "IP": info.ip or "Spawning...",
        "Expires At": info.expires_at,
        "Lab Server": info.lab_server,
        "Status": "Spawning ⏳" if info.is_spawning else "Active 🚀",
    }
    formatter.render_details("Active Virtual Machine", details)


@machine_group.command(name="start", help="Start a virtual machine")
@click.argument("target")
@click.option("--poll/--no-poll", default=True, help="Poll until the machine is fully started and has an IP")
@handle_errors("start machine")
def machines_start(target, poll):
    sdk = get_sdk()
    machine_id = resolve_id(target, sdk.v5.get_machines)
    if not machine_id:
        fail(f"Could not resolve target '{target}' to a valid machine ID.")

    formatter.print_info(f"Starting machine ID {machine_id}...")
    req = SpawnRequest(machine_id=machine_id)
    detailed = sdk.v4.post_vm_spawn_detailed(body=req)
    if detailed.status_code not in SUCCESS_STATUS_CODES:
        fail_api("start machine", detailed)

    formatter.print_success("Start request sent successfully!")
    if not poll:
        return

    formatter.print_info("Waiting for machine to boot...")
    ip = _poll_machine_boot(sdk, machine_id)
    if ip:
        formatter.print_success(f"Machine is online! IP: [success]{ip}[/success]")
    else:
        formatter.print_warning(
            "Timeout or active target mismatch. Run 'pyhtb machine active' to check status."
        )


def _poll_machine_boot(sdk, machine_id):
    """Poll the active machine endpoint until the target has an IP. Returns the IP or None."""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=formatter.console,
        transient=True,
    ) as progress:
        task = progress.add_task("Initializing...", total=None)

        start_time = time.time()
        while time.time() - start_time < BOOT_POLL_TIMEOUT:
            time.sleep(BOOT_POLL_INTERVAL)
            try:
                active_res = sdk.v5.get_virtual_machine_active()
            except Exception:
                continue
            if not (active_res and active_res.info):
                continue

            info = active_res.info
            if info.id != machine_id:
                formatter.print_warning(
                    f"Active machine is ID {info.id} ({info.name}), expected {machine_id}."
                )
                return None
            if info.ip:
                return info.ip
            if info.is_spawning:
                progress.update(task, description=f"Booting target {info.name}...")
            else:
                progress.update(task, description="Waiting for IP address assignment...")
    return None


def _change_active_machine_state(sdk, request_fn, *, verb, gerund, error_action):
    """Shared flow for stop/reset: look up the active machine and submit a state change.

    ``verb`` is the bare action ("stop"), ``gerund`` its -ing form ("Stopping"),
    and ``error_action`` the phrase passed to ``print_api_error`` on failure.
    """
    active_res = sdk.v5.get_virtual_machine_active()
    if not active_res or not active_res.info:
        formatter.print_warning(f"No active machine to {verb}.")
        return

    info = active_res.info
    formatter.print_info(f"{gerund} active machine '{info.name}' (ID: {info.id})...")

    detailed = request_fn(body=SpawnRequest(machine_id=info.id))
    if detailed.status_code in SUCCESS_STATUS_CODES:
        formatter.print_success(f"{verb.capitalize()} request sent successfully!")
    else:
        fail_api(error_action, detailed)


@machine_group.command(name="stop", help="Terminate the active virtual machine")
@handle_errors("stop machine")
def machines_stop():
    sdk = get_sdk()
    _change_active_machine_state(
        sdk, sdk.v4.post_vm_terminate_detailed,
        verb="stop", gerund="Stopping", error_action="terminate machine",
    )


@machine_group.command(name="reset", help="Reset the active virtual machine")
@handle_errors("reset machine")
def machines_reset():
    sdk = get_sdk()
    _change_active_machine_state(
        sdk, sdk.v4.post_vm_reset_detailed,
        verb="reset", gerund="Resetting", error_action="reset machine",
    )


@machine_group.command(name="own", help="Submit flag for a machine")
@click.argument("target")
@click.argument("flag")
@click.option("--difficulty", type=int, help="Difficulty rating (10 to 100)")
@handle_errors("submit flag")
def machines_own(target, flag, difficulty):
    sdk = get_sdk()
    machine_id = resolve_id(target, sdk.v5.get_machines)
    if not machine_id:
        fail(f"Could not resolve target '{target}' to a valid machine ID.")

    formatter.print_info(f"Submitting flag for machine ID {machine_id}...")
    body = OwnRequest(flag=flag, id=machine_id)
    if difficulty is not None:
        body.difficulty = difficulty

    detailed = sdk.v5.post_machine_own_detailed(body=body)
    if detailed.status_code == 200:
        res = detailed.parsed
        if getattr(res, "success", False):
            formatter.print_success(res.message)
            if getattr(res, "points", 0):
                formatter.print_success(f"Earned Points: {res.points}")
        else:
            fail(res.message)
    elif detailed.status_code == 400:
        res = detailed.parsed
        fail(res.message if res else "Invalid request or flag.")
    else:
        fail_api("submit flag", detailed)
