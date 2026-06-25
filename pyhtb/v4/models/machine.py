from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Machine")


@_attrs_define
class Machine:
    """Schema definition for Machine

    Attributes:
        avatar_thumb_url (str | Unset):  Example:
            https://labs.hackthebox.com/storage/avatars/f85bcb72ecffef8a5b2afd2fbc3ac153_thumb.png.
        id (int | Unset):  Example: 1.
        name (str | Unset):  Example: RASTA-DC01.
        os (str | Unset):  Example: Windows.
    """

    avatar_thumb_url: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    os: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_thumb_url = self.avatar_thumb_url

        id = self.id

        name = self.name

        os = self.os

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar_thumb_url is not UNSET:
            field_dict["avatar_thumb_url"] = avatar_thumb_url
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if os is not UNSET:
            field_dict["os"] = os

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar_thumb_url = d.pop("avatar_thumb_url", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        os = d.pop("os", UNSET)

        machine = cls(
            avatar_thumb_url=avatar_thumb_url,
            id=id,
            name=name,
            os=os,
        )

        machine.additional_properties = d
        return machine

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
