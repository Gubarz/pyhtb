import time
import click
from .. import formatter
from .. import config
from pyhtb import PyHTB
from pyhtb.v5.models.get_machines_state_item import GetMachinesStateItem
from pyhtb.v5.models.get_machines_difficulty_item import GetMachinesDifficultyItem
from pyhtb.v5.models.get_machines_os_item import GetMachinesOsItem
from pyhtb.v5.models.get_machines_todo import GetMachinesTodo
from pyhtb.v4.models.spawn_request import SpawnRequest
from pyhtb.v5.models.own_request import OwnRequest
from rich.progress import Progress, SpinnerColumn, TextColumn

def get_sdk():
    token = config.load_token()
    if not token:
        formatter.print_error("No API token found. Please set HTB_TOKEN environment variable or run 'yahtbcli auth set'.")
        raise click.Abort()
    return PyHTB(token=token)

@click.group(name="machine", help="Interact with Hack The Box machines")
def machine_group():
    pass

@machine_group.command(name="list", help="List machines on Hack The Box")
@click.option("--retired", is_flag=True, help="List retired machines instead of active ones")
@click.option("--todo", is_flag=True, help="List machines on your todo list")
@click.option("--difficulty", type=click.Choice(["easy", "medium", "hard", "insane"], case_sensitive=False), help="Filter by difficulty")
@click.option("--os", "os_name", type=click.Choice(["linux", "windows", "other"], case_sensitive=False), help="Filter by OS")
@click.option("--page", type=int, default=1, help="Page number (default: 1)")
@click.option("--limit", type=int, default=20, help="Number of machines to list (default: 20)")
@click.option("--search", "keyword", help="Search keyword")
def machines_list(retired, todo, difficulty, os_name, page, limit, keyword):
    sdk = get_sdk()
    state_item = GetMachinesStateItem.RETIRED if retired else GetMachinesStateItem.ACTIVE
    
    diff_item = None
    if difficulty:
        diff_item = [GetMachinesDifficultyItem(difficulty.lower())]
        
    os_item = None
    if os_name:
        os_item = [GetMachinesOsItem(os_name.lower())]
        
    todo_item = GetMachinesTodo.VALUE_1 if todo else None
    
    formatter.print_info("Fetching machines...")
    try:
        kwargs = {
            "state": [state_item],
            "page": page,
            "per_page": limit
        }
        if diff_item is not None:
            kwargs["difficulty"] = diff_item
        if os_item is not None:
            kwargs["os"] = os_item
        if todo_item is not None:
            kwargs["todo"] = todo_item
        if keyword:
            kwargs["keyword"] = keyword

        response = sdk.v5.get_machines(**kwargs)
        
        if not response or not response.data:
            formatter.print_warning("No machines found matching the criteria.")
            return
            
        rows = []
        for machine in response.data:
            owned_status = "Not Owned"
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
            
            rows.append([
                machine.id,
                machine.name,
                formatter.format_os(machine.os),
                formatter.format_difficulty(machine.difficulty_text),
                machine.points,
                owned_status,
                active_str,
                free_str
            ])
            
        headers = ["ID", "Name", "OS", "Difficulty", "Points", "Owned", "Active", "Tier"]
        formatter.render_table("Hack The Box Machines", headers, rows)
        
    except Exception as e:
        formatter.print_error(f"Failed to fetch machines: {e}")

@machine_group.command(name="info", help="Show details of a specific machine")
@click.argument("target")
def machines_info(target):
    sdk = get_sdk()
    formatter.print_info(f"Retrieving profile for '{target}'...")
    
    try:
        response = None
        # Try fetching directly by target (numeric or slug)
        try:
            response = sdk.v4.get_machine_profile(target)
        except Exception:
            pass
            
        if not response or not getattr(response, "info", None):
            # Try searching by name/keyword in V5
            search_res = sdk.v5.get_machines(keyword=target)
            if search_res and search_res.data:
                for item in search_res.data:
                    if item.name.lower() == target.lower():
                        response = sdk.v4.get_machine_profile(str(item.id))
                        break
                        
        if not response or not getattr(response, "info", None):
            formatter.print_error(f"Machine '{target}' not found.")
            return
            
        info = response.info
        is_active = False
        if info.play_info:
            is_active = bool(info.play_info.is_active or info.play_info.is_spawned)

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
        
    except Exception as e:
        formatter.print_error(f"Failed to retrieve profile: {e}")

@machine_group.command(name="active", help="Show active virtual machine details")
def machines_active():
    sdk = get_sdk()
    formatter.print_info("Checking active target machine...")
    try:
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
    except Exception as e:
        formatter.print_error(f"Failed to retrieve active machine: {e}")

@machine_group.command(name="start", help="Start a virtual machine")
@click.argument("target")
@click.option("--poll/--no-poll", default=True, help="Poll until the machine is fully started and has an IP")
def machines_start(target, poll):
    sdk = get_sdk()
    machine_id = None
    if target.isdigit():
        machine_id = int(target)
    else:
        formatter.print_info(f"Resolving machine name '{target}'...")
        try:
            res = sdk.v5.get_machines(keyword=target)
            if res and res.data:
                for item in res.data:
                    if item.name.lower() == target.lower():
                        machine_id = item.id
                        break
        except Exception as e:
            formatter.print_error(f"Search failed: {e}")
            return
            
    if not machine_id:
        formatter.print_error(f"Could not resolve target '{target}' to a valid machine ID.")
        return
        
    formatter.print_info(f"Starting machine ID {machine_id}...")
    try:
        req = SpawnRequest(machine_id=machine_id)
        detailed = sdk.v4.post_vm_spawn_detailed(body=req)
        if detailed.status_code not in (200, 201, 202):
            formatter.print_api_error("start machine", detailed)
            return
            
        formatter.print_success("Start request sent successfully!")
        
        if not poll:
            return
            
        formatter.print_info("Waiting for machine to boot...")
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=formatter.console,
            transient=True
        ) as progress:
            task = progress.add_task("Initializing...", total=None)
            
            start_time = time.time()
            ip = None
            while time.time() - start_time < 300:
                time.sleep(5)
                try:
                    active_res = sdk.v5.get_virtual_machine_active()
                    if active_res and active_res.info:
                        info = active_res.info
                        if info.id == machine_id:
                            if info.ip:
                                ip = info.ip
                                break
                            elif info.is_spawning:
                                progress.update(task, description=f"Booting target {info.name}...")
                            else:
                                progress.update(task, description="Waiting for IP address assignment...")
                        else:
                            formatter.print_warning(f"Active machine is ID {info.id} ({info.name}), expected {machine_id}.")
                            break
                except Exception:
                    pass
                    
            if ip:
                formatter.print_success(f"Machine is online! IP: [success]{ip}[/success]")
            else:
                formatter.print_warning("Timeout or active target mismatch. Run 'yahtbcli machine active' to check status.")
                
    except Exception as e:
        formatter.print_error(f"Failed to start machine: {e}")

@machine_group.command(name="stop", help="Terminate the active virtual machine")
def machines_stop():
    sdk = get_sdk()
    try:
        active_res = sdk.v5.get_virtual_machine_active()
        if not active_res or not active_res.info:
            formatter.print_warning("No active machine to stop.")
            return
            
        info = active_res.info
        formatter.print_info(f"Stopping active machine '{info.name}' (ID: {info.id})...")
        
        req = SpawnRequest(machine_id=info.id)
        detailed = sdk.v4.post_vm_terminate_detailed(body=req)
        if detailed.status_code in (200, 201, 202):
            formatter.print_success("Termination request sent successfully!")
        else:
            formatter.print_api_error("terminate machine", detailed)
    except Exception as e:
        formatter.print_error(f"Failed to stop machine: {e}")

@machine_group.command(name="reset", help="Reset the active virtual machine")
def machines_reset():
    sdk = get_sdk()
    try:
        active_res = sdk.v5.get_virtual_machine_active()
        if not active_res or not active_res.info:
            formatter.print_warning("No active machine to reset.")
            return
            
        info = active_res.info
        formatter.print_info(f"Resetting active machine '{info.name}' (ID: {info.id})...")
        
        req = SpawnRequest(machine_id=info.id)
        detailed = sdk.v4.post_vm_reset_detailed(body=req)
        if detailed.status_code in (200, 201, 202):
            formatter.print_success("Reset request sent successfully!")
        else:
            formatter.print_api_error("reset machine", detailed)
    except Exception as e:
        formatter.print_error(f"Failed to reset machine: {e}")

@machine_group.command(name="own", help="Submit flag for a machine")
@click.argument("target")
@click.argument("flag")
@click.option("--difficulty", type=int, help="Difficulty rating (10 to 100)")
def machines_own(target, flag, difficulty):
    sdk = get_sdk()
    machine_id = None
    if target.isdigit():
        machine_id = int(target)
    else:
        formatter.print_info(f"Resolving machine name '{target}'...")
        try:
            res = sdk.v5.get_machines(keyword=target)
            if res and res.data:
                for item in res.data:
                    if item.name.lower() == target.lower():
                        machine_id = item.id
                        break
        except Exception as e:
            formatter.print_error(f"Search failed: {e}")
            return
            
    if not machine_id:
        formatter.print_error(f"Could not resolve target '{target}' to a valid machine ID.")
        return
        
    formatter.print_info(f"Submitting flag for machine ID {machine_id}...")
    try:
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
                formatter.print_error(res.message)
        elif detailed.status_code == 400:
            res = detailed.parsed
            formatter.print_error(res.message if res else "Invalid request or flag.")
        else:
            formatter.print_api_error("submit flag", detailed)
    except Exception as e:
        formatter.print_error(f"Failed to submit flag: {e}")
