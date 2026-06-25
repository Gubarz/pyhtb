import click
from .. import formatter
from .. import config
from pyhtb import PyHTB
from pyhtb.v4.models.own_request import OwnRequest
from pyhtb.v4.models.post_container_start_json_body import PostContainerStartJsonBody
from pyhtb.v4.models.post_container_stop_json_body import PostContainerStopJsonBody

def get_sdk():
    token = config.load_token()
    if not token:
        formatter.print_error("No API token found. Please set HTB_TOKEN environment variable or run 'yahtbcli auth set'.")
        raise click.Abort()
    return PyHTB(token=token)

@click.group(name="challenge", help="Interact with Hack The Box challenges")
def challenge_group():
    pass

@challenge_group.command(name="list", help="List challenges on Hack The Box")
@click.option("--category", help="Filter by category (e.g. Reversing, Crypto, Pwn, Web, Forensics)")
@click.option("--difficulty", type=click.Choice(["easy", "medium", "hard", "insane", "very-easy"], case_sensitive=False), help="Filter by difficulty")
@click.option("--search", "keyword", help="Search keyword")
@click.option("--page", type=int, default=1, help="Page number (default: 1)")
@click.option("--limit", type=int, default=20, help="Limit results (default: 20)")
def challenges_list(category, difficulty, keyword, page, limit):
    sdk = get_sdk()
    formatter.print_info("Fetching challenges...")
    try:
        category_ids = None
        if category:
            try:
                cat_res = sdk.v4.get_challenge_categories_list()
                if cat_res:
                    cats = getattr(cat_res, "info", None) or getattr(cat_res, "data", None)
                    if isinstance(cats, list):
                        for cat in cats:
                            if getattr(cat, "name", "").lower() == category.lower():
                                category_ids = [getattr(cat, "id")]
                                break
                    if category_ids is None:
                        available = [getattr(c, "name", "?") for c in (cats or [])]
                        formatter.print_warning(f"Unknown category '{category}'. Available: {', '.join(available)}")
                        return
            except Exception as e:
                formatter.print_error(f"Failed to resolve category: {e}")
                return
                
        diff_item = None
        if difficulty:
            from pyhtb.v4.models.get_challenges_difficulty_item import GetChallengesDifficultyItem
            diff_item = [GetChallengesDifficultyItem(difficulty.lower())]

        kwargs = {
            "page": page,
            "per_page": limit
        }
        if keyword:
            kwargs["keyword"] = keyword
        if category_ids:
            kwargs["category"] = category_ids
        if diff_item is not None:
            kwargs["difficulty"] = diff_item

        response = sdk.v4.get_challenges(**kwargs)
        
        if not response or not response.data:
            formatter.print_warning("No challenges found.")
            return
            
        rows = []
        for chal in response.data:
            owned_status = formatter.format_status(chal.is_owned)
            docker_support = "[success]Yes[/success]" if chal.play_methods and ("container" in chal.play_methods or "docker" in chal.play_methods) else "[error]No[/error]"
            
            rows.append([
                chal.id,
                chal.name,
                chal.category_name,
                formatter.format_difficulty(chal.difficulty),
                chal.solves,
                owned_status,
                docker_support
            ])
            
        headers = ["ID", "Name", "Category", "Difficulty", "Solves", "Status", "Docker"]
        formatter.render_table("Challenges", headers, rows)
    except Exception as e:
        formatter.print_error(f"Failed to fetch challenges: {e}")

@challenge_group.command(name="info", help="Show details of a specific challenge")
@click.argument("target")
def challenges_info(target):
    sdk = get_sdk()
    formatter.print_info(f"Retrieving challenge profile for '{target}'...")
    try:
        response = sdk.v4.get_challenge_info(target)
        if not response or not getattr(response, "challenge", None):
            formatter.print_error(f"Challenge '{target}' not found.")
            return
            
        chal = response.challenge
        details = {
            "ID": chal.id,
            "Name": chal.name,
            "Category": chal.category_name,
            "Difficulty": formatter.format_difficulty(chal.difficulty),
            "Points": chal.points,
            "Creator": chal.creator_name,
            "Solves": chal.solves,
            "Stars": chal.stars,
            "Status": formatter.format_status(chal.auth_user_solve),
            "Docker Support": "[success]Yes[/success]" if chal.docker else "[error]No[/error]",
        }
        
        if chal.docker and chal.docker_status:
            details["Docker Status"] = chal.docker_status
            if chal.docker_ip:
                details["Docker IP"] = chal.docker_ip
            if chal.docker_ports:
                details["Docker Ports"] = ", ".join(map(str, chal.docker_ports))
                
        formatter.render_details(f"Challenge: {chal.name}", details)
        if chal.description:
            import html
            print(f"\nDescription:\n{html.unescape(chal.description)}\n")
    except Exception as e:
        formatter.print_error(f"Failed to retrieve challenge details: {e}")
def resolve_challenge_id(sdk, target: str):
    if target.isdigit():
        return int(target)
    formatter.print_info(f"Resolving challenge name '{target}'...")
    try:
        res = sdk.v4.get_challenges(keyword=target)
        if res and res.data:
            for item in res.data:
                if item.name.lower() == target.lower():
                    return item.id
    except Exception as e:
        formatter.print_error(f"Search failed: {e}")
    return None

@challenge_group.command(name="start", help="Start a Docker container for a challenge")
@click.argument("target")
def challenges_start(target):
    sdk = get_sdk()
    challenge_id = resolve_challenge_id(sdk, target)
    if not challenge_id:
        formatter.print_error(f"Could not resolve target '{target}' to a valid challenge ID.")
        return
        
    formatter.print_info(f"Starting Docker container for challenge ID {challenge_id}...")
    try:
        body = PostContainerStartJsonBody(containerable_id=challenge_id)
        detailed = sdk.v4.post_container_start_detailed(body=body)
        if detailed.status_code == 200:
            formatter.print_success("Container start request accepted!")
            
            from rich.progress import Progress, SpinnerColumn, TextColumn
            import time
            
            ip = None
            ports = None
            formatter.print_info("Waiting for container assignment...")
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=formatter.console,
                transient=True
            ) as progress:
                task = progress.add_task("Retrieving IP and ports...", total=None)
                for _ in range(15):
                    time.sleep(2)
                    try:
                        info_res = sdk.v4.get_challenge_info(str(challenge_id))
                        if info_res and getattr(info_res, "challenge", None):
                            chal = info_res.challenge
                            if chal.docker_ip:
                                ip = chal.docker_ip
                                ports = chal.docker_ports
                                break
                    except Exception:
                        pass
            
            if ip:
                formatter.print_success("Container is online!")
                formatter.print_success(f"IP Address: [success]{ip}[/success]")
                if ports:
                    formatter.print_success(f"Port(s): [success]{', '.join(map(str, ports))}[/success]")
            else:
                formatter.print_warning("Container started but IP assignment is taking longer than expected. Run 'yahtbcli challenge info <name>' to check status.")
        else:
            formatter.print_api_error("start container", detailed)
    except Exception as e:
        formatter.print_error(f"Failed to start container: {e}")

@challenge_group.command(name="stop", help="Stop the Docker container for a challenge")
@click.argument("target")
def challenges_stop(target):
    sdk = get_sdk()
    challenge_id = resolve_challenge_id(sdk, target)
    if not challenge_id:
        formatter.print_error(f"Could not resolve target '{target}' to a valid challenge ID.")
        return
        
    formatter.print_info(f"Stopping Docker container for challenge ID {challenge_id}...")
    try:
        body = PostContainerStopJsonBody(containerable_id=challenge_id)
        detailed = sdk.v4.post_container_stop_detailed(body=body)
        if detailed.status_code == 200:
            formatter.print_success("Container stopped successfully!")
        else:
            formatter.print_api_error("stop container", detailed)
    except Exception as e:
        formatter.print_error(f"Failed to stop container: {e}")

@challenge_group.command(name="own", help="Submit flag for a challenge")
@click.argument("target")
@click.argument("flag")
def challenges_own(target, flag):
    sdk = get_sdk()
    challenge_id = resolve_challenge_id(sdk, target)
    if not challenge_id:
        formatter.print_error(f"Could not resolve target '{target}' to a valid challenge ID.")
        return

    formatter.print_info(f"Submitting flag for challenge ID {challenge_id}...")
    try:
        body = OwnRequest(flag=flag, challenge_id=challenge_id)
        detailed = sdk.v4.post_challenge_own_detailed(body=body)
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
