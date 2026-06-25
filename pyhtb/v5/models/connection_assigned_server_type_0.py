from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionAssignedServerType0")


@_attrs_define
class ConnectionAssignedServerType0:
    """
    Attributes:
        id (int | Unset):
        friendly_name (str | Unset):
        current_clients (int | Unset):
        location (str | Unset):
    """

    id: int | Unset = UNSET
    friendly_name: str | Unset = UNSET
    current_clients: int | Unset = UNSET
    location: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        friendly_name = self.friendly_name

        current_clients = self.current_clients

        location = self.location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if friendly_name is not UNSET:
            field_dict["friendly_name"] = friendly_name
        if current_clients is not UNSET:
            field_dict["current_clients"] = current_clients
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        friendly_name = d.pop("friendly_name", UNSET)

        current_clients = d.pop("current_clients", UNSET)

        location = d.pop("location", UNSET)

        connection_assigned_server_type_0 = cls(
            id=id,
            friendly_name=friendly_name,
            current_clients=current_clients,
            location=location,
        )

        connection_assigned_server_type_0.additional_properties = d
        return connection_assigned_server_type_0

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
