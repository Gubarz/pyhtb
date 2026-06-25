import click
from . import formatter
from . import config
from .commands import auth_group, machine_group, challenge_group, vpn_group
from pyhtb import PyHTB

@click.group(help="Hack The Box Labs Command Line Interface")
@click.version_option(version="0.1.0")
def cli():
    pass

# Register subcommand groups
cli.add_command(auth_group)
cli.add_command(machine_group)
cli.add_command(challenge_group)
cli.add_command(vpn_group)

@cli.command(name="whoami", help="Display details of the currently authenticated profile")
def whoami():
    token = config.load_token()
    if not token:
        formatter.print_error("No App Token found. Run 'yahtbcli auth set' or set HTB_TOKEN environment variable.")
        return

    formatter.print_info("Connecting to Hack The Box API...")
    try:
        sdk = PyHTB(token=token)
        response = sdk.v4.get_user_profile_summary_detailed()
        if response.status_code == 200:
            profile = response.parsed
            stats = profile.user_stats
            formatter.print_success(f"Authenticated as {stats.name}!")
            details = {
                "Username": stats.name,
                "ID": stats.id,
                "Rank": stats.rank,
                "Points": stats.points,
                "System Owns": stats.system_owns,
                "User Owns": stats.user_owns,
            }
            formatter.render_details("Profile Information", details)
        else:
            formatter.print_error(f"Authentication failed. Status: {response.status_code}")
    except Exception as e:
        formatter.print_error(f"Connection failed: {e}")

@cli.command(name="search", help="Global search for machines and challenges")
@click.argument("query")
def search(query):
    token = config.load_token()
    if not token:
        formatter.print_error("No App Token found. Run 'yahtbcli auth set' or set HTB_TOKEN environment variable.")
        return

    sdk = PyHTB(token=token)
    
    # 1. Search Machines
    formatter.print_info(f"Searching machines for '{query}'...")
    try:
        mach_res = sdk.v5.get_machines(keyword=query)
        if mach_res and mach_res.data:
            rows = []
            for m in mach_res.data:
                tier_str = "[success]Free[/success]" if m.free else "[warning]VIP[/warning]"
                rows.append([
                    m.id,
                    m.name,
                    formatter.format_os(m.os),
                    formatter.format_difficulty(m.difficulty_text),
                    m.points,
                    tier_str
                ])
            headers = ["ID", "Name", "OS", "Difficulty", "Points", "Tier"]
            formatter.render_table(f"Matching Machines ({len(rows)})", headers, rows)
        else:
            formatter.print_warning("No matching machines found.")
    except Exception as e:
        formatter.print_error(f"Machine search failed: {e}")

    # 2. Search Challenges
    print()
    formatter.print_info(f"Searching challenges for '{query}'...")
    try:
        chal_res = sdk.v4.get_challenges(keyword=query)
        if chal_res and chal_res.data:
            rows = []
            for c in chal_res.data:
                rows.append([
                    c.id,
                    c.name,
                    c.category_name,
                    formatter.format_difficulty(c.difficulty),
                    c.solves,
                    formatter.format_status(c.is_owned)
                ])
            headers = ["ID", "Name", "Category", "Difficulty", "Solves", "Status"]
            formatter.render_table(f"Matching Challenges ({len(rows)})", headers, rows)
        else:
            formatter.print_warning("No matching challenges found.")
    except Exception as e:
        formatter.print_error(f"Challenge search failed: {e}")
