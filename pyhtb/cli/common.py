import functools
from typing import Callable, NoReturn, Optional

import click

from pyhtb import PyHTB

from . import config, formatter


def get_sdk() -> PyHTB:
    token = config.load_token()
    if not token:
        formatter.print_error(
            "No API token found. Please set HTB_TOKEN environment variable "
            "or run 'pyhtb auth set'."
        )
        raise click.Abort()
    return PyHTB(token=token)


def fail(message: str) -> NoReturn:
    """Print a themed error and exit with a nonzero status.

    Use this for genuine command failures (not found, rejected, bad input) so
    that scripts and automation can detect them via the exit code.
    """
    formatter.print_error(message)
    raise click.exceptions.Exit(1)


def fail_api(action: str, detailed) -> NoReturn:
    """Report an unsuccessful API response and exit with a nonzero status."""
    formatter.print_api_error(action, detailed)
    raise click.exceptions.Exit(1)


def handle_errors(action: str) -> Callable:
    """Decorator that reports any uncaught exception as a friendly CLI error.

    The themed error is printed via the formatter, then the command exits with a
    nonzero status so scripts and automation can detect the failure.
    """

    def decorator(fn: Callable) -> Callable:
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except (click.Abort, click.exceptions.Exit):
                raise
            except Exception as e:
                formatter.print_error(f"Failed to {action}: {e}")
                raise click.exceptions.Exit(1)

        return wrapper

    return decorator


def resolve_id(target: str, search_fn: Callable) -> Optional[int]:
    """Resolve a target to a numeric ID.

    Numeric targets are returned as-is; otherwise the target is treated as a
    name and looked up via ``search_fn`` (any SDK list endpoint that accepts a
    ``keyword`` argument and returns objects with ``id``/``name``).
    """
    if target.isdigit():
        return int(target)

    formatter.print_info(f"Resolving name '{target}'...")
    res = search_fn(keyword=target)
    if res and res.data:
        target_lower = target.lower()
        return next((item.id for item in res.data if item.name.lower() == target_lower), None)
    return None


def fetch_profile(sdk: PyHTB, success_message: str):
    """Fetch the authenticated user's profile, rendering it on success.

    Prints ``success_message`` (which may reference the profile via ``{name}``)
    before rendering the details panel and returning the parsed profile. Calls
    :func:`fail` (exiting nonzero) if the request was not successful.
    """
    response = sdk.v4.get_user_profile_summary_detailed()
    if response.status_code != 200:
        fail(f"Authentication failed. Status: {response.status_code}")

    profile = response.parsed
    formatter.print_success(success_message.format(name=profile.user_stats.name))
    render_profile_details("Profile Information", profile)
    return profile


def render_profile_details(title: str, profile) -> None:
    stats = profile.user_stats
    details = {
        "Username": stats.name,
        "ID": stats.id,
        "Rank": stats.rank,
        "Points": stats.points,
        "System Owns": stats.system_owns,
        "User Owns": stats.user_owns,
    }
    formatter.render_details(title, details)
