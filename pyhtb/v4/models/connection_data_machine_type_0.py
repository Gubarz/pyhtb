from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionDataMachineType0")


@_attrs_define
class ConnectionDataMachineType0:
    """
    Attributes:
        avatar_thumb_url (str | Unset):
        id (int | Unset):
        name (str | Unset):
    """

    avatar_thumb_url: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_thumb_url = self.avatar_thumb_url

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar_thumb_url is not UNSET:
            field_dict["avatar_thumb_url"] = avatar_thumb_url
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar_thumb_url = d.pop("avatar_thumb_url", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        connection_data_machine_type_0 = cls(
            avatar_thumb_url=avatar_thumb_url,
            id=id,
            name=name,
        )

        connection_data_machine_type_0.additional_properties = d
        return connection_data_machine_type_0

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
