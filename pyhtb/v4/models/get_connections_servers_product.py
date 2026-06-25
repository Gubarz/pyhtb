from enum import Enum


class GetConnectionsServersProduct(str, Enum):
    COMPETITIVE = "competitive"
    FORTRESSES = "fortresses"
    LABS = "labs"
    STARTING_POINT = "starting_point"

    def __str__(self) -> str:
        return str(self.value)
