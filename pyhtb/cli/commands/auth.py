import click

from .. import config, formatter
from ..common import fail, fetch_profile, get_sdk, handle_errors


@click.group(name="auth", help="Manage Hack The Box API credentials")
def auth_group():
    pass


@auth_group.command(name="set", help="Save your Hack The Box App Token")
@click.option("--token", "-t", help="HTB App Token")
@handle_errors("store token")
def auth_set(token):
    if not token:
        token = click.prompt("Paste your HTB App Token (input hidden)", hide_input=True)

    token = token.strip()
    if not token:
        fail("Token cannot be empty.")

    config.save_token(token)
    formatter.print_success("Token stored securely in user config!")


@auth_group.command(name="unset", help="Delete the stored App Token")
@handle_errors("delete token")
def auth_unset():
    config.delete_token()
    formatter.print_success("Stored Token deleted successfully.")


@auth_group.command(name="status", help="Verify connection and display profile info")
@handle_errors("connect")
def auth_status():
    sdk = get_sdk()
    formatter.print_info("Connecting to Hack The Box API to verify token...")
    fetch_profile(sdk, "Authenticated successfully!")
