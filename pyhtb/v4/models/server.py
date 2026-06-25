from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Server")


@_attrs_define
class Server:
    """Schema definition for Server

    Attributes:
        current_clients (int | Unset):  Example: 85.
        friendly_name (str | Unset):  Example: US VIP+ 1.
        full (bool | Unset):
        id (int | Unset):  Example: 289.
        location (str | Unset):  Example: US.
    """

    current_clients: int | Unset = UNSET
    friendly_name: str | Unset = UNSET
    full: bool | Unset = UNSET
    id: int | Unset = UNSET
    location: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_clients = self.current_clients

        friendly_name = self.friendly_name

        full = self.full

        id = self.id

        location = self.location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_clients is not UNSET:
            field_dict["current_clients"] = current_clients
        if friendly_name is not UNSET:
            field_dict["friendly_name"] = friendly_name
        if full is not UNSET:
            field_dict["full"] = full
        if id is not UNSET:
            field_dict["id"] = id
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_clients = d.pop("current_clients", UNSET)

        friendly_name = d.pop("friendly_name", UNSET)

        full = d.pop("full", UNSET)

        id = d.pop("id", UNSET)

        location = d.pop("location", UNSET)

        server = cls(
            current_clients=current_clients,
            friendly_name=friendly_name,
            full=full,
            id=id,
            location=location,
        )

        server.additional_properties = d
        return server

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
