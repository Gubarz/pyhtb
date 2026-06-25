from enum import Enum


class UserRankingType1(str, Enum):
    UNRANKED = "unranked"

    def __str__(self) -> str:
        return str(self.value)
