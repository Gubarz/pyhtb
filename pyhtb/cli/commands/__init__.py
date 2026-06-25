from .auth import auth_group
from .machines import machine_group
from .challenges import challenge_group
from .vpn import vpn_group
from .misc import whoami, search

__all__ = [
    "auth_group",
    "machine_group",
    "challenge_group",
    "vpn_group",
    "whoami",
    "search",
]
