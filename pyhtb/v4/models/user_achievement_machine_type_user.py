from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAchievementMachineTypeUser")


@_attrs_define
class UserAchievementMachineTypeUser:
    """
    Attributes:
        avatar (str | Unset):
        avatar_url (str | Unset):
        id (int | Unset):
        name (str | Unset):
        retired (bool | Unset):
        starting_point (bool | Unset):
    """

    avatar: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    retired: bool | Unset = UNSET
    starting_point: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar = self.avatar

        avatar_url = self.avatar_url

        id = self.id

        name = self.name

        retired = self.retired

        starting_point = self.starting_point

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if retired is not UNSET:
            field_dict["retired"] = retired
        if starting_point is not UNSET:
            field_dict["starting_point"] = starting_point

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar = d.pop("avatar", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        retired = d.pop("retired", UNSET)

        starting_point = d.pop("starting_point", UNSET)

        user_achievement_machine_type_user = cls(
            avatar=avatar,
            avatar_url=avatar_url,
            id=id,
            name=name,
            retired=retired,
            starting_point=starting_point,
        )

        user_achievement_machine_type_user.additional_properties = d
        return user_achievement_machine_type_user

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
