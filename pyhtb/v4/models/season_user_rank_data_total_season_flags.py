from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeasonUserRankDataTotalSeasonFlags")


@_attrs_define
class SeasonUserRankDataTotalSeasonFlags:
    """
    Attributes:
        obtained (int | Unset):
        total (int | Unset):
    """

    obtained: int | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        obtained = self.obtained

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if obtained is not UNSET:
            field_dict["obtained"] = obtained
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        obtained = d.pop("obtained", UNSET)

        total = d.pop("total", UNSET)

        season_user_rank_data_total_season_flags = cls(
            obtained=obtained,
            total=total,
        )

        season_user_rank_data_total_season_flags.additional_properties = d
        return season_user_rank_data_total_season_flags

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
