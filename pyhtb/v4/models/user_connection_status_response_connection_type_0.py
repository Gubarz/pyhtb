from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserConnectionStatusResponseConnectionType0")


@_attrs_define
class UserConnectionStatusResponseConnectionType0:
    """
    Attributes:
        down (float | Unset):  Example: 123.45.
        ip4 (str | Unset):  Example: 10.10.10.10.
        ip6 (str | Unset):  Example: 2001:db8::1.
        name (str | Unset):  Example: tun0.
        through_pwnbox (bool | Unset):
        up (float | Unset):  Example: 67.89.
    """

    down: float | Unset = UNSET
    ip4: str | Unset = UNSET
    ip6: str | Unset = UNSET
    name: str | Unset = UNSET
    through_pwnbox: bool | Unset = UNSET
    up: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        down = self.down

        ip4 = self.ip4

        ip6 = self.ip6

        name = self.name

        through_pwnbox = self.through_pwnbox

        up = self.up

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if down is not UNSET:
            field_dict["down"] = down
        if ip4 is not UNSET:
            field_dict["ip4"] = ip4
        if ip6 is not UNSET:
            field_dict["ip6"] = ip6
        if name is not UNSET:
            field_dict["name"] = name
        if through_pwnbox is not UNSET:
            field_dict["through_pwnbox"] = through_pwnbox
        if up is not UNSET:
            field_dict["up"] = up

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        down = d.pop("down", UNSET)

        ip4 = d.pop("ip4", UNSET)

        ip6 = d.pop("ip6", UNSET)

        name = d.pop("name", UNSET)

        through_pwnbox = d.pop("through_pwnbox", UNSET)

        up = d.pop("up", UNSET)

        user_connection_status_response_connection_type_0 = cls(
            down=down,
            ip4=ip4,
            ip6=ip6,
            name=name,
            through_pwnbox=through_pwnbox,
            up=up,
        )

        user_connection_status_response_connection_type_0.additional_properties = d
        return user_connection_status_response_connection_type_0

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
