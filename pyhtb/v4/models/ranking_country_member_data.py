from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rankings_item import RankingsItem


T = TypeVar("T", bound="RankingCountryMemberData")


@_attrs_define
class RankingCountryMemberData:
    """
    Attributes:
        country_name (str | Unset):
        rankings (list[RankingsItem] | Unset):
    """

    country_name: str | Unset = UNSET
    rankings: list[RankingsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_name = self.country_name

        rankings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rankings, Unset):
            rankings = []
            for (
                componentsschemas_ranking_country_rankings_items_item_data
            ) in self.rankings:
                componentsschemas_ranking_country_rankings_items_item = (
                    componentsschemas_ranking_country_rankings_items_item_data.to_dict()
                )
                rankings.append(componentsschemas_ranking_country_rankings_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country_name is not UNSET:
            field_dict["country_name"] = country_name
        if rankings is not UNSET:
            field_dict["rankings"] = rankings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rankings_item import RankingsItem

        d = dict(src_dict)
        country_name = d.pop("country_name", UNSET)

        _rankings = d.pop("rankings", UNSET)
        rankings: list[RankingsItem] | Unset = UNSET
        if _rankings is not UNSET:
            rankings = []
            for componentsschemas_ranking_country_rankings_items_item_data in _rankings:
                componentsschemas_ranking_country_rankings_items_item = (
                    RankingsItem.from_dict(
                        componentsschemas_ranking_country_rankings_items_item_data
                    )
                )

                rankings.append(componentsschemas_ranking_country_rankings_items_item)

        ranking_country_member_data = cls(
            country_name=country_name,
            rankings=rankings,
        )

        ranking_country_member_data.additional_properties = d
        return ranking_country_member_data

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
