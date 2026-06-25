from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MachineCreator")


@_attrs_define
class MachineCreator:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        avatar (None | str | Unset):
        is_respected (bool | Unset):
        profile_url (None | str | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    avatar: None | str | Unset = UNSET
    is_respected: bool | Unset = UNSET
    profile_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        avatar: None | str | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

        is_respected = self.is_respected

        profile_url: None | str | Unset
        if isinstance(self.profile_url, Unset):
            profile_url = UNSET
        else:
            profile_url = self.profile_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if is_respected is not UNSET:
            field_dict["isRespected"] = is_respected
        if profile_url is not UNSET:
            field_dict["profile_url"] = profile_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        is_respected = d.pop("isRespected", UNSET)

        def _parse_profile_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_url = _parse_profile_url(d.pop("profile_url", UNSET))

        machine_creator = cls(
            id=id,
            name=name,
            avatar=avatar,
            is_respected=is_respected,
            profile_url=profile_url,
        )

        machine_creator.additional_properties = d
        return machine_creator

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
