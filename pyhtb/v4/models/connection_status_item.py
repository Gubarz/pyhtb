from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connection import Connection
    from ..models.connection_server import ConnectionServer


T = TypeVar("T", bound="ConnectionStatusItem")


@_attrs_define
class ConnectionStatusItem:
    """
    Attributes:
        connection (Connection | Unset):
        location_type_friendly (str | Unset):
        server (ConnectionServer | Unset):
        type_ (str | Unset):
        connection_type (str | Unset):
    """

    connection: Connection | Unset = UNSET
    location_type_friendly: str | Unset = UNSET
    server: ConnectionServer | Unset = UNSET
    type_: str | Unset = UNSET
    connection_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connection, Unset):
            connection = self.connection.to_dict()

        location_type_friendly = self.location_type_friendly

        server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        type_ = self.type_

        connection_type = self.connection_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection is not UNSET:
            field_dict["connection"] = connection
        if location_type_friendly is not UNSET:
            field_dict["location_type_friendly"] = location_type_friendly
        if server is not UNSET:
            field_dict["server"] = server
        if type_ is not UNSET:
            field_dict["type"] = type_
        if connection_type is not UNSET:
            field_dict["connection_type"] = connection_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection import Connection
        from ..models.connection_server import ConnectionServer

        d = dict(src_dict)
        _connection = d.pop("connection", UNSET)
        connection: Connection | Unset
        if isinstance(_connection, Unset):
            connection = UNSET
        else:
            connection = Connection.from_dict(_connection)

        location_type_friendly = d.pop("location_type_friendly", UNSET)

        _server = d.pop("server", UNSET)
        server: ConnectionServer | Unset
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = ConnectionServer.from_dict(_server)

        type_ = d.pop("type", UNSET)

        connection_type = d.pop("connection_type", UNSET)

        connection_status_item = cls(
            connection=connection,
            location_type_friendly=location_type_friendly,
            server=server,
            type_=type_,
            connection_type=connection_type,
        )

        connection_status_item.additional_properties = d
        return connection_status_item

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
