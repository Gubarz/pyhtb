from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assigned_server import AssignedServer
    from ..models.options import Options


T = TypeVar("T", bound="ConnectionsServerData")


@_attrs_define
class ConnectionsServerData:
    """
    Attributes:
        assigned (AssignedServer | None | Unset): Schema definition for Assigned Server
        disabled (bool | Unset):
        options (Options | Unset): Schema definition for Options
    """

    assigned: AssignedServer | None | Unset = UNSET
    disabled: bool | Unset = UNSET
    options: Options | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.assigned_server import AssignedServer

        assigned: dict[str, Any] | None | Unset
        if isinstance(self.assigned, Unset):
            assigned = UNSET
        elif isinstance(self.assigned, AssignedServer):
            assigned = self.assigned.to_dict()
        else:
            assigned = self.assigned

        disabled = self.disabled

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assigned is not UNSET:
            field_dict["assigned"] = assigned
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assigned_server import AssignedServer
        from ..models.options import Options

        d = dict(src_dict)

        def _parse_assigned(data: object) -> AssignedServer | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_assigned_server_connections_servers_type_0 = (
                    AssignedServer.from_dict(data)
                )

                return componentsschemas_assigned_server_connections_servers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssignedServer | None | Unset, data)

        assigned = _parse_assigned(d.pop("assigned", UNSET))

        disabled = d.pop("disabled", UNSET)

        _options = d.pop("options", UNSET)
        options: Options | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = Options.from_dict(_options)

        connections_server_data = cls(
            assigned=assigned,
            disabled=disabled,
            options=options,
        )

        connections_server_data.additional_properties = d
        return connections_server_data

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
