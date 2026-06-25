from importlib.metadata import PackageNotFoundError, version

import click

from .commands import (
    auth_group,
    challenge_group,
    machine_group,
    search,
    vpn_group,
    whoami,
)

try:
    _VERSION = version("pyhtb")
except PackageNotFoundError:
    _VERSION = "0.0.0"


@click.group(help="Hack The Box Labs Command Line Interface")
@click.version_option(version=_VERSION)
def cli():
    pass


# Register subcommand groups and top-level commands
cli.add_command(auth_group)
cli.add_command(machine_group)
cli.add_command(challenge_group)
cli.add_command(vpn_group)
cli.add_command(whoami)
cli.add_command(search)
