import click
from .. import config
from .. import formatter
from pyhtb import PyHTB

@click.group(name="auth", help="Manage Hack The Box API credentials")
def auth_group():
    pass

@auth_group.command(name="set", help="Save your Hack The Box App Token")
@click.option("--token", "-t", help="HTB App Token")
def auth_set(token):
    if not token:
        token = click.prompt("Paste your HTB App Token (input hidden)", hide_input=True)
    
    token = token.strip()
    if not token:
        formatter.print_error("Token cannot be empty.")
        return
        
    try:
        config.save_token(token)
        formatter.print_success("Token stored securely in user config!")
    except Exception as e:
        formatter.print_error(f"Failed to store token: {e}")

@auth_group.command(name="unset", help="Delete the stored App Token")
def auth_unset():
    try:
        config.delete_token()
        formatter.print_success("Stored Token deleted successfully.")
    except Exception as e:
        formatter.print_error(f"Failed to delete token: {e}")

@auth_group.command(name="status", help="Verify connection and display profile info")
def auth_status():
    token = config.load_token()
    if not token:
        formatter.print_error("No App Token found. Run 'yahtbcli auth set' or set HTB_TOKEN environment variable.")
        return

    formatter.print_info("Connecting to Hack The Box API to verify token...")
    try:
        sdk = PyHTB(token=token)
        response = sdk.v4.get_user_profile_summary_detailed()
        if response.status_code == 200:
            profile = response.parsed
            stats = profile.user_stats
            formatter.print_success("Authenticated successfully!")
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
