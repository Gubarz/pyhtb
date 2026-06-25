from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VirtualMachineActiveInfo")


@_attrs_define
class VirtualMachineActiveInfo:
    """Schema definition for active virtual machine information

    Attributes:
        vpn_server_type (str):
        id (int):
        name (str):
        avatar (str):
        type_ (str):
        expires_at (str):
        is_spawning (bool):
        lab_server (str):
        vpn_server_id (int):
        avatar_url (str):
        ip (None | str):
    """

    vpn_server_type: str
    id: int
    name: str
    avatar: str
    type_: str
    expires_at: str
    is_spawning: bool
    lab_server: str
    vpn_server_id: int
    avatar_url: str
    ip: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vpn_server_type = self.vpn_server_type

        id = self.id

        name = self.name

        avatar = self.avatar

        type_ = self.type_

        expires_at = self.expires_at

        is_spawning = self.is_spawning

        lab_server = self.lab_server

        vpn_server_id = self.vpn_server_id

        avatar_url = self.avatar_url

        ip: None | str
        ip = self.ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vpn_server_type": vpn_server_type,
                "id": id,
                "name": name,
                "avatar": avatar,
                "type": type_,
                "expires_at": expires_at,
                "isSpawning": is_spawning,
                "lab_server": lab_server,
                "vpn_server_id": vpn_server_id,
                "avatar_url": avatar_url,
                "ip": ip,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vpn_server_type = d.pop("vpn_server_type")

        id = d.pop("id")

        name = d.pop("name")

        avatar = d.pop("avatar")

        type_ = d.pop("type")

        expires_at = d.pop("expires_at")

        is_spawning = d.pop("isSpawning")

        lab_server = d.pop("lab_server")

        vpn_server_id = d.pop("vpn_server_id")

        avatar_url = d.pop("avatar_url")

        def _parse_ip(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ip = _parse_ip(d.pop("ip"))

        virtual_machine_active_info = cls(
            vpn_server_type=vpn_server_type,
            id=id,
            name=name,
            avatar=avatar,
            type_=type_,
            expires_at=expires_at,
            is_spawning=is_spawning,
            lab_server=lab_server,
            vpn_server_id=vpn_server_id,
            avatar_url=avatar_url,
            ip=ip,
        )

        virtual_machine_active_info.additional_properties = d
        return virtual_machine_active_info

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
