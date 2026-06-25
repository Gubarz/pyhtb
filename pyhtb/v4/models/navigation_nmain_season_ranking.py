from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.latest_season import LatestSeason
    from ..models.upcoming_season import UpcomingSeason


T = TypeVar("T", bound="NavigationNmainSeasonRanking")


@_attrs_define
class NavigationNmainSeasonRanking:
    """
    Attributes:
        latest_season (LatestSeason | Unset): Schema definition for Latest Season
        league (str | Unset):
        rank (int | Unset):
        rank_suffix (str | Unset):
        upcoming_season (UpcomingSeason | Unset):
    """

    latest_season: LatestSeason | Unset = UNSET
    league: str | Unset = UNSET
    rank: int | Unset = UNSET
    rank_suffix: str | Unset = UNSET
    upcoming_season: UpcomingSeason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latest_season: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest_season, Unset):
            latest_season = self.latest_season.to_dict()

        league = self.league

        rank = self.rank

        rank_suffix = self.rank_suffix

        upcoming_season: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upcoming_season, Unset):
            upcoming_season = self.upcoming_season.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latest_season is not UNSET:
            field_dict["latest_season"] = latest_season
        if league is not UNSET:
            field_dict["league"] = league
        if rank is not UNSET:
            field_dict["rank"] = rank
        if rank_suffix is not UNSET:
            field_dict["rank_suffix"] = rank_suffix
        if upcoming_season is not UNSET:
            field_dict["upcoming_season"] = upcoming_season

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.latest_season import LatestSeason
        from ..models.upcoming_season import UpcomingSeason

        d = dict(src_dict)
        _latest_season = d.pop("latest_season", UNSET)
        latest_season: LatestSeason | Unset
        if isinstance(_latest_season, Unset):
            latest_season = UNSET
        else:
            latest_season = LatestSeason.from_dict(_latest_season)

        league = d.pop("league", UNSET)

        rank = d.pop("rank", UNSET)

        rank_suffix = d.pop("rank_suffix", UNSET)

        _upcoming_season = d.pop("upcoming_season", UNSET)
        upcoming_season: UpcomingSeason | Unset
        if isinstance(_upcoming_season, Unset):
            upcoming_season = UNSET
        else:
            upcoming_season = UpcomingSeason.from_dict(_upcoming_season)

        navigation_nmain_season_ranking = cls(
            latest_season=latest_season,
            league=league,
            rank=rank,
            rank_suffix=rank_suffix,
            upcoming_season=upcoming_season,
        )

        navigation_nmain_season_ranking.additional_properties = d
        return navigation_nmain_season_ranking

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
