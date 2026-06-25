import html
import time

import click
from rich.progress import Progress, SpinnerColumn, TextColumn

from pyhtb.v4.models.get_challenges_difficulty_item import GetChallengesDifficultyItem
from pyhtb.v4.models.own_request import OwnRequest
from pyhtb.v4.models.post_container_start_json_body import PostContainerStartJsonBody
from pyhtb.v4.models.post_container_stop_json_body import PostContainerStopJsonBody

from .. import formatter
from ..common import fail, fail_api, get_sdk, handle_errors, resolve_id

# Container assignment polling: 15 attempts every 2s (~30s total).
CONTAINER_POLL_ATTEMPTS = 15
CONTAINER_POLL_INTERVAL = 2


@click.group(name="challenge", help="Interact with Hack The Box challenges")
def challenge_group():
    pass


def _resolve_category_id(sdk, category):
    """Resolve a category name to its ID, failing if it cannot be matched."""
    cat_res = sdk.v4.get_challenge_categories_list()
    categories = getattr(cat_res, "info", None)
    if not isinstance(categories, list):
        categories = []

    target = category.lower()
    for cat in categories:
        if cat.name and cat.name.lower() == target:
            return cat.id

    available = ", ".join(cat.name for cat in categories if cat.name)
    fail(f"Unknown category '{category}'. Available: {available}")


@challenge_group.command(name="list", help="List challenges on Hack The Box")
@click.option("--category", help="Filter by category (e.g. Reversing, Crypto, Pwn, Web, Forensics)")
@click.option(
    "--difficulty",
    type=click.Choice(["easy", "medium", "hard", "insane", "very-easy"], case_sensitive=False),
    help="Filter by difficulty",
)
@click.option("--search", "keyword", help="Search keyword")
@click.option("--page", type=int, default=1, help="Page number (default: 1)")
@click.option("--limit", type=int, default=20, help="Limit results (default: 20)")
@handle_errors("fetch challenges")
def challenges_list(category, difficulty, keyword, page, limit):
    sdk = get_sdk()

    kwargs = {"page": page, "per_page": limit}
    if keyword:
        kwargs["keyword"] = keyword
    if difficulty:
        kwargs["difficulty"] = [GetChallengesDifficultyItem(difficulty.lower())]
    if category:
        kwargs["category"] = [_resolve_category_id(sdk, category)]

    formatter.print_info("Fetching challenges...")
    response = sdk.v4.get_challenges(**kwargs)
    if not response or not response.data:
        formatter.print_warning("No challenges found.")
        return

    rows = []
    for chal in response.data:
        docker_support = (
            "[success]Yes[/success]"
            if chal.play_methods and ("container" in chal.play_methods or "docker" in chal.play_methods)
            else "[error]No[/error]"
        )
        rows.append(
            [
                chal.id,
                chal.name,
                chal.category_name,
                formatter.format_difficulty(chal.difficulty),
                chal.solves,
                formatter.format_status(chal.is_owned),
                docker_support,
            ]
        )

    headers = ["ID", "Name", "Category", "Difficulty", "Solves", "Status", "Docker"]
    formatter.render_table("Challenges", headers, rows)


@challenge_group.command(name="info", help="Show details of a specific challenge")
@click.argument("target")
@handle_errors("retrieve challenge details")
def challenges_info(target):
    sdk = get_sdk()
    formatter.print_info(f"Retrieving challenge profile for '{target}'...")

    response = sdk.v4.get_challenge_info(target)
    if not response or not getattr(response, "challenge", None):
        fail(f"Challenge '{target}' not found.")

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
        formatter.console.print(f"\nDescription:\n{html.unescape(chal.description)}\n")


@challenge_group.command(name="start", help="Start a Docker container for a challenge")
@click.argument("target")
@handle_errors("start container")
def challenges_start(target):
    sdk = get_sdk()
    challenge_id = resolve_id(target, sdk.v4.get_challenges)
    if not challenge_id:
        fail(f"Could not resolve target '{target}' to a valid challenge ID.")

    formatter.print_info(f"Starting Docker container for challenge ID {challenge_id}...")
    body = PostContainerStartJsonBody(containerable_id=challenge_id)
    detailed = sdk.v4.post_container_start_detailed(body=body)
    if detailed.status_code != 200:
        fail_api("start container", detailed)

    formatter.print_success("Container start request accepted!")
    formatter.print_info("Waiting for container assignment...")

    ip, ports = _poll_container(sdk, challenge_id)
    if ip:
        formatter.print_success("Container is online!")
        formatter.print_success(f"IP Address: [success]{ip}[/success]")
        if ports:
            formatter.print_success(f"Port(s): [success]{', '.join(map(str, ports))}[/success]")
    else:
        formatter.print_warning(
            "Container started but IP assignment is taking longer than expected. "
            "Run 'pyhtb challenge info <name>' to check status."
        )


def _poll_container(sdk, challenge_id):
    """Poll for a started container's IP/ports, returning (ip, ports) or (None, None)."""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=formatter.console,
        transient=True,
    ) as progress:
        progress.add_task("Retrieving IP and ports...", total=None)
        for _ in range(CONTAINER_POLL_ATTEMPTS):
            time.sleep(CONTAINER_POLL_INTERVAL)
            try:
                info_res = sdk.v4.get_challenge_info(str(challenge_id))
            except Exception:
                continue
            if info_res and getattr(info_res, "challenge", None):
                chal = info_res.challenge
                if chal.docker_ip:
                    return chal.docker_ip, chal.docker_ports
    return None, None


@challenge_group.command(name="stop", help="Stop the Docker container for a challenge")
@click.argument("target")
@handle_errors("stop container")
def challenges_stop(target):
    sdk = get_sdk()
    challenge_id = resolve_id(target, sdk.v4.get_challenges)
    if not challenge_id:
        fail(f"Could not resolve target '{target}' to a valid challenge ID.")

    formatter.print_info(f"Stopping Docker container for challenge ID {challenge_id}...")
    body = PostContainerStopJsonBody(containerable_id=challenge_id)
    detailed = sdk.v4.post_container_stop_detailed(body=body)
    if detailed.status_code == 200:
        formatter.print_success("Container stopped successfully!")
    else:
        fail_api("stop container", detailed)


@challenge_group.command(name="own", help="Submit flag for a challenge")
@click.argument("target")
@click.argument("flag")
@handle_errors("submit flag")
def challenges_own(target, flag):
    sdk = get_sdk()
    challenge_id = resolve_id(target, sdk.v4.get_challenges)
    if not challenge_id:
        fail(f"Could not resolve target '{target}' to a valid challenge ID.")

    formatter.print_info(f"Submitting flag for challenge ID {challenge_id}...")
    body = OwnRequest(flag=flag, challenge_id=challenge_id)
    detailed = sdk.v4.post_challenge_own_detailed(body=body)

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
