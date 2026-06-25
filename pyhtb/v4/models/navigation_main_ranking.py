from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NavigationMainRanking")


@_attrs_define
class NavigationMainRanking:
    """
    Attributes:
        current_xp (float | Unset):
        id (int | Unset):
        name (str | Unset):
        next_rank_xp (float | Unset):
    """

    current_xp: float | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    next_rank_xp: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_xp = self.current_xp

        id = self.id

        name = self.name

        next_rank_xp = self.next_rank_xp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_xp is not UNSET:
            field_dict["current_xp"] = current_xp
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if next_rank_xp is not UNSET:
            field_dict["next_rank_xp"] = next_rank_xp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_xp = d.pop("current_xp", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        next_rank_xp = d.pop("next_rank_xp", UNSET)

        navigation_main_ranking = cls(
            current_xp=current_xp,
            id=id,
            name=name,
            next_rank_xp=next_rank_xp,
        )

        navigation_main_ranking.additional_properties = d
        return navigation_main_ranking

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
