from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connection_competitive_entry import ConnectionCompetitiveEntry
    from ..models.connection_lab_entry import ConnectionLabEntry
    from ..models.connection_pro_lab_entry import ConnectionProLabEntry


T = TypeVar("T", bound="ConnectionsResponse")


@_attrs_define
class ConnectionsResponse:
    """Schema definition for Connections Response

    Attributes:
        data (list[ConnectionCompetitiveEntry | ConnectionLabEntry | ConnectionProLabEntry] | Unset):
    """

    data: (
        list[ConnectionCompetitiveEntry | ConnectionLabEntry | ConnectionProLabEntry]
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.connection_lab_entry import ConnectionLabEntry
        from ..models.connection_pro_lab_entry import ConnectionProLabEntry

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for componentsschemas_connections_data_item_data in self.data:
                componentsschemas_connections_data_item: dict[str, Any]
                if isinstance(
                    componentsschemas_connections_data_item_data, ConnectionLabEntry
                ):
                    componentsschemas_connections_data_item = (
                        componentsschemas_connections_data_item_data.to_dict()
                    )
                elif isinstance(
                    componentsschemas_connections_data_item_data, ConnectionProLabEntry
                ):
                    componentsschemas_connections_data_item = (
                        componentsschemas_connections_data_item_data.to_dict()
                    )
                else:
                    componentsschemas_connections_data_item = (
                        componentsschemas_connections_data_item_data.to_dict()
                    )

                data.append(componentsschemas_connections_data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_competitive_entry import ConnectionCompetitiveEntry
        from ..models.connection_lab_entry import ConnectionLabEntry
        from ..models.connection_pro_lab_entry import ConnectionProLabEntry

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: (
            list[
                ConnectionCompetitiveEntry | ConnectionLabEntry | ConnectionProLabEntry
            ]
            | Unset
        ) = UNSET
        if _data is not UNSET:
            data = []
            for componentsschemas_connections_data_item_data in _data:

                def _parse_componentsschemas_connections_data_item(
                    data: object,
                ) -> (
                    ConnectionCompetitiveEntry
                    | ConnectionLabEntry
                    | ConnectionProLabEntry
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_connection_type_0 = (
                            ConnectionLabEntry.from_dict(data)
                        )

                        return componentsschemas_connection_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_connection_type_1 = (
                            ConnectionProLabEntry.from_dict(data)
                        )

                        return componentsschemas_connection_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_connection_type_2 = (
                        ConnectionCompetitiveEntry.from_dict(data)
                    )

                    return componentsschemas_connection_type_2

                componentsschemas_connections_data_item = (
                    _parse_componentsschemas_connections_data_item(
                        componentsschemas_connections_data_item_data
                    )
                )

                data.append(componentsschemas_connections_data_item)

        connections_response = cls(
            data=data,
        )

        connections_response.additional_properties = d
        return connections_response

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
