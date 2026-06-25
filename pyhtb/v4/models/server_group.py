from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_group_servers import ServerGroupServers


T = TypeVar("T", bound="ServerGroup")


@_attrs_define
class ServerGroup:
    """Schema definition for Server Group

    Attributes:
        location (str | Unset):  Example: EU.
        name (str | Unset):  Example: EU - Free.
        servers (ServerGroupServers | Unset):
    """

    location: str | Unset = UNSET
    name: str | Unset = UNSET
    servers: ServerGroupServers | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location = self.location

        name = self.name

        servers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = self.servers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if servers is not UNSET:
            field_dict["servers"] = servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_group_servers import ServerGroupServers

        d = dict(src_dict)
        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        _servers = d.pop("servers", UNSET)
        servers: ServerGroupServers | Unset
        if isinstance(_servers, Unset):
            servers = UNSET
        else:
            servers = ServerGroupServers.from_dict(_servers)

        server_group = cls(
            location=location,
            name=name,
            servers=servers,
        )

        server_group.additional_properties = d
        return server_group

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
