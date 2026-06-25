from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.navigation_main_ranking import NavigationMainRanking
    from ..models.navigation_nmain_season_ranking import NavigationNmainSeasonRanking


T = TypeVar("T", bound="NavigationMainData")


@_attrs_define
class NavigationMainData:
    """
    Attributes:
        ranking (NavigationMainRanking | Unset):
        season_ranking (NavigationNmainSeasonRanking | Unset):
        sso_linked (bool | Unset):
    """

    ranking: NavigationMainRanking | Unset = UNSET
    season_ranking: NavigationNmainSeasonRanking | Unset = UNSET
    sso_linked: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ranking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ranking, Unset):
            ranking = self.ranking.to_dict()

        season_ranking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.season_ranking, Unset):
            season_ranking = self.season_ranking.to_dict()

        sso_linked = self.sso_linked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ranking is not UNSET:
            field_dict["ranking"] = ranking
        if season_ranking is not UNSET:
            field_dict["season_ranking"] = season_ranking
        if sso_linked is not UNSET:
            field_dict["sso_linked"] = sso_linked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.navigation_main_ranking import NavigationMainRanking
        from ..models.navigation_nmain_season_ranking import (
            NavigationNmainSeasonRanking,
        )

        d = dict(src_dict)
        _ranking = d.pop("ranking", UNSET)
        ranking: NavigationMainRanking | Unset
        if isinstance(_ranking, Unset):
            ranking = UNSET
        else:
            ranking = NavigationMainRanking.from_dict(_ranking)

        _season_ranking = d.pop("season_ranking", UNSET)
        season_ranking: NavigationNmainSeasonRanking | Unset
        if isinstance(_season_ranking, Unset):
            season_ranking = UNSET
        else:
            season_ranking = NavigationNmainSeasonRanking.from_dict(_season_ranking)

        sso_linked = d.pop("sso_linked", UNSET)

        navigation_main_data = cls(
            ranking=ranking,
            season_ranking=season_ranking,
            sso_linked=sso_linked,
        )

        navigation_main_data.additional_properties = d
        return navigation_main_data

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
