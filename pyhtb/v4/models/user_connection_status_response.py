from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_connection_status_response_connection_type_0 import (
        UserConnectionStatusResponseConnectionType0,
    )


T = TypeVar("T", bound="UserConnectionStatusResponse")


@_attrs_define
class UserConnectionStatusResponse:
    """Schema definition for User Connection Status Response

    Attributes:
        connection (str | Unset | UserConnectionStatusResponseConnectionType0):
        status (bool | Unset):
    """

    connection: str | Unset | UserConnectionStatusResponseConnectionType0 = UNSET
    status: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_connection_status_response_connection_type_0 import (
            UserConnectionStatusResponseConnectionType0,
        )

        connection: dict[str, Any] | str | Unset
        if isinstance(self.connection, Unset):
            connection = UNSET
        elif isinstance(self.connection, UserConnectionStatusResponseConnectionType0):
            connection = self.connection.to_dict()
        else:
            connection = self.connection

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection is not UNSET:
            field_dict["connection"] = connection
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_connection_status_response_connection_type_0 import (
            UserConnectionStatusResponseConnectionType0,
        )

        d = dict(src_dict)

        def _parse_connection(
            data: object,
        ) -> str | Unset | UserConnectionStatusResponseConnectionType0:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                connection_type_0 = (
                    UserConnectionStatusResponseConnectionType0.from_dict(data)
                )

                return connection_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(str | Unset | UserConnectionStatusResponseConnectionType0, data)

        connection = _parse_connection(d.pop("connection", UNSET))

        status = d.pop("status", UNSET)

        user_connection_status_response = cls(
            connection=connection,
            status=status,
        )

        user_connection_status_response.additional_properties = d
        return user_connection_status_response

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
