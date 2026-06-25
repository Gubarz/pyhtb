from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionServer")


@_attrs_define
class ConnectionServer:
    """
    Attributes:
        friendly_name (str | Unset):
        hostname (str | Unset):
        id (int | Unset):
        pro_lab_id (int | Unset):
    """

    friendly_name: str | Unset = UNSET
    hostname: str | Unset = UNSET
    id: int | Unset = UNSET
    pro_lab_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        friendly_name = self.friendly_name

        hostname = self.hostname

        id = self.id

        pro_lab_id = self.pro_lab_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if friendly_name is not UNSET:
            field_dict["friendly_name"] = friendly_name
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if id is not UNSET:
            field_dict["id"] = id
        if pro_lab_id is not UNSET:
            field_dict["pro_lab_id"] = pro_lab_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        friendly_name = d.pop("friendly_name", UNSET)

        hostname = d.pop("hostname", UNSET)

        id = d.pop("id", UNSET)

        pro_lab_id = d.pop("pro_lab_id", UNSET)

        connection_server = cls(
            friendly_name=friendly_name,
            hostname=hostname,
            id=id,
            pro_lab_id=pro_lab_id,
        )

        connection_server.additional_properties = d
        return connection_server

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
