from enum import Enum


class PwnboxRequestLocation(str, Enum):
    AU = "au"
    CA = "ca"
    DE = "de"
    IN = "in"
    UK = "uk"
    US_EAST = "us-east"
    US_WEST = "us-west"

    def __str__(self) -> str:
        return str(self.value)
