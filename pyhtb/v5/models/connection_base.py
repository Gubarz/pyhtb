from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connection_assigned_server_type_0 import ConnectionAssignedServerType0


T = TypeVar("T", bound="ConnectionBase")


@_attrs_define
class ConnectionBase:
    """
    Attributes:
        type_ (str):
        location_type_friendly (None | str | Unset):
        assigned_server (ConnectionAssignedServerType0 | None | Unset):
    """

    type_: str
    location_type_friendly: None | str | Unset = UNSET
    assigned_server: ConnectionAssignedServerType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.connection_assigned_server_type_0 import (
            ConnectionAssignedServerType0,
        )

        type_ = self.type_

        location_type_friendly: None | str | Unset
        if isinstance(self.location_type_friendly, Unset):
            location_type_friendly = UNSET
        else:
            location_type_friendly = self.location_type_friendly

        assigned_server: dict[str, Any] | None | Unset
        if isinstance(self.assigned_server, Unset):
            assigned_server = UNSET
        elif isinstance(self.assigned_server, ConnectionAssignedServerType0):
            assigned_server = self.assigned_server.to_dict()
        else:
            assigned_server = self.assigned_server

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if location_type_friendly is not UNSET:
            field_dict["location_type_friendly"] = location_type_friendly
        if assigned_server is not UNSET:
            field_dict["assigned_server"] = assigned_server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_assigned_server_type_0 import (
            ConnectionAssignedServerType0,
        )

        d = dict(src_dict)
        type_ = d.pop("type")

        def _parse_location_type_friendly(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_type_friendly = _parse_location_type_friendly(
            d.pop("location_type_friendly", UNSET)
        )

        def _parse_assigned_server(
            data: object,
        ) -> ConnectionAssignedServerType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_connection_assigned_server_type_0 = (
                    ConnectionAssignedServerType0.from_dict(data)
                )

                return componentsschemas_connection_assigned_server_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConnectionAssignedServerType0 | None | Unset, data)

        assigned_server = _parse_assigned_server(d.pop("assigned_server", UNSET))

        connection_base = cls(
            type_=type_,
            location_type_friendly=location_type_friendly,
            assigned_server=assigned_server,
        )

        connection_base.additional_properties = d
        return connection_base

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
