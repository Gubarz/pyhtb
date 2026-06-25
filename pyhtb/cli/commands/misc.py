import click

from .. import formatter
from ..common import fetch_profile, get_sdk, handle_errors


@click.command(name="whoami", help="Display details of the currently authenticated profile")
@handle_errors("connect")
def whoami():
    sdk = get_sdk()
    formatter.print_info("Connecting to Hack The Box API...")
    fetch_profile(sdk, "Authenticated as {name}!")


@click.command(name="search", help="Global search for machines and challenges")
@click.argument("query")
def search(query):
    sdk = get_sdk()

    _search_machines(sdk, query)
    formatter.console.print()
    _search_challenges(sdk, query)


@handle_errors("search machines")
def _search_machines(sdk, query):
    formatter.print_info(f"Searching machines for '{query}'...")
    response = sdk.v5.get_machines(keyword=query)
    if not response or not response.data:
        formatter.print_warning("No matching machines found.")
        return

    rows = []
    for m in response.data:
        tier_str = "[success]Free[/success]" if m.free else "[warning]VIP[/warning]"
        rows.append([
            m.id,
            m.name,
            formatter.format_os(m.os),
            formatter.format_difficulty(m.difficulty_text),
            m.points,
            tier_str,
        ])

    headers = ["ID", "Name", "OS", "Difficulty", "Points", "Tier"]
    formatter.render_table(f"Matching Machines ({len(rows)})", headers, rows)


@handle_errors("search challenges")
def _search_challenges(sdk, query):
    formatter.print_info(f"Searching challenges for '{query}'...")
    response = sdk.v4.get_challenges(keyword=query)
    if not response or not response.data:
        formatter.print_warning("No matching challenges found.")
        return

    rows = []
    for c in response.data:
        rows.append([
            c.id,
            c.name,
            c.category_name,
            formatter.format_difficulty(c.difficulty),
            c.solves,
            formatter.format_status(c.is_owned),
        ])

    headers = ["ID", "Name", "Category", "Difficulty", "Solves", "Status"]
    formatter.render_table(f"Matching Challenges ({len(rows)})", headers, rows)
