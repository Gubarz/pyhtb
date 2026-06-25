from enum import Enum


class ConnectionCompetitiveEntryType(str, Enum):
    COMPETITIVE = "competitive"

    def __str__(self) -> str:
        return str(self.value)
