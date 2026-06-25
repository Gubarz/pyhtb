from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileUserTeamInfo")


@_attrs_define
class ProfileUserTeamInfo:
    """
    Attributes:
        avatar (str | Unset):
        name (str | Unset):
        ranking (int | Unset):
    """

    avatar: str | Unset = UNSET
    name: str | Unset = UNSET
    ranking: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar = self.avatar

        name = self.name

        ranking = self.ranking

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if name is not UNSET:
            field_dict["name"] = name
        if ranking is not UNSET:
            field_dict["ranking"] = ranking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar = d.pop("avatar", UNSET)

        name = d.pop("name", UNSET)

        ranking = d.pop("ranking", UNSET)

        profile_user_team_info = cls(
            avatar=avatar,
            name=name,
            ranking=ranking,
        )

        profile_user_team_info.additional_properties = d
        return profile_user_team_info

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
