from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RankingDataUserProperties")


@_attrs_define
class RankingDataUserProperties:
    """
    Attributes:
        avatar (str | Unset):
        id (int | Unset):
        name (str | Unset):
        rank (int | Unset):
        rank_growth (str | Unset):
    """

    avatar: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    rank: int | Unset = UNSET
    rank_growth: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar = self.avatar

        id = self.id

        name = self.name

        rank = self.rank

        rank_growth = self.rank_growth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if rank is not UNSET:
            field_dict["rank"] = rank
        if rank_growth is not UNSET:
            field_dict["rank_growth"] = rank_growth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar = d.pop("avatar", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        rank = d.pop("rank", UNSET)

        rank_growth = d.pop("rank_growth", UNSET)

        ranking_data_user_properties = cls(
            avatar=avatar,
            id=id,
            name=name,
            rank=rank,
            rank_growth=rank_growth,
        )

        ranking_data_user_properties.additional_properties = d
        return ranking_data_user_properties

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
