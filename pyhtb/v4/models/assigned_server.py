from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssignedServer")


@_attrs_define
class AssignedServer:
    """Schema definition for Assigned Server

    Attributes:
        current_clients (int | Unset):  Example: 85.
        friendly_name (str | Unset):  Example: US VIP+ 1.
        id (int | Unset):  Example: 289.
        location (str | Unset):  Example: US.
        location_type_friendly (str | Unset):
        pro_lab_id (int | Unset):
    """

    current_clients: int | Unset = UNSET
    friendly_name: str | Unset = UNSET
    id: int | Unset = UNSET
    location: str | Unset = UNSET
    location_type_friendly: str | Unset = UNSET
    pro_lab_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_clients = self.current_clients

        friendly_name = self.friendly_name

        id = self.id

        location = self.location

        location_type_friendly = self.location_type_friendly

        pro_lab_id = self.pro_lab_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_clients is not UNSET:
            field_dict["current_clients"] = current_clients
        if friendly_name is not UNSET:
            field_dict["friendly_name"] = friendly_name
        if id is not UNSET:
            field_dict["id"] = id
        if location is not UNSET:
            field_dict["location"] = location
        if location_type_friendly is not UNSET:
            field_dict["location_type_friendly"] = location_type_friendly
        if pro_lab_id is not UNSET:
            field_dict["pro_lab_id"] = pro_lab_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_clients = d.pop("current_clients", UNSET)

        friendly_name = d.pop("friendly_name", UNSET)

        id = d.pop("id", UNSET)

        location = d.pop("location", UNSET)

        location_type_friendly = d.pop("location_type_friendly", UNSET)

        pro_lab_id = d.pop("pro_lab_id", UNSET)

        assigned_server = cls(
            current_clients=current_clients,
            friendly_name=friendly_name,
            id=id,
            location=location,
            location_type_friendly=location_type_friendly,
            pro_lab_id=pro_lab_id,
        )

        assigned_server.additional_properties = d
        return assigned_server

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
