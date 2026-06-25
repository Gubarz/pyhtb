from enum import Enum


class OwnResponseOwnType(str, Enum):
    ROOT = "Root"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
