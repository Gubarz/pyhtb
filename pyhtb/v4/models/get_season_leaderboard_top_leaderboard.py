from enum import Enum


class GetSeasonLeaderboardTopLeaderboard(str, Enum):
    PLAYERS = "players"
    TEAMS = "teams"

    def __str__(self) -> str:
        return str(self.value)
