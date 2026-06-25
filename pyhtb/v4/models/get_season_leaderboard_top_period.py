from enum import Enum


class GetSeasonLeaderboardTopPeriod(str, Enum):
    VALUE_0 = "1Y"
    VALUE_1 = "6M"
    VALUE_2 = "3M"
    VALUE_3 = "1M"
    VALUE_4 = "1W"

    def __str__(self) -> str:
        return str(self.value)
