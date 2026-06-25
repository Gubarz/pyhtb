from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActiveMachineInfo")


@_attrs_define
class ActiveMachineInfo:
    """
    Attributes:
        avatar (None | str | Unset):  Example: /storage/avatars/23e804513a47e8f20bc865d0419946e1.png.
        avatar_url (None | str | Unset):  Example: https://cdn.services-
            k8s.prod.aws.htb.systems/content/machines/avatar/9e4d90d2-73c7-4da0-a15f-662bbc048868_thumb_64.png.
        expires_at (str | Unset):  Example: 2024-05-18 17:42:04.
        id (int | Unset):  Example: 597.
        ip (None | str | Unset):  Example: 10.129.56.30.
        is_spawning (bool | Unset):
        lab_server (str | Unset):  Example: vip_lab.
        name (str | Unset):  Example: Usage.
        tier_id (None | str | Unset):
        type_ (str | Unset):  Example: Free.
        voted (None | str | Unset):
        voting (None | str | Unset):
        vpn_server_id (int | None | Unset):  Example: 289.
    """

    avatar: None | str | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    expires_at: str | Unset = UNSET
    id: int | Unset = UNSET
    ip: None | str | Unset = UNSET
    is_spawning: bool | Unset = UNSET
    lab_server: str | Unset = UNSET
    name: str | Unset = UNSET
    tier_id: None | str | Unset = UNSET
    type_: str | Unset = UNSET
    voted: None | str | Unset = UNSET
    voting: None | str | Unset = UNSET
    vpn_server_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar: None | str | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        expires_at = self.expires_at

        id = self.id

        ip: None | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        is_spawning = self.is_spawning

        lab_server = self.lab_server

        name = self.name

        tier_id: None | str | Unset
        if isinstance(self.tier_id, Unset):
            tier_id = UNSET
        else:
            tier_id = self.tier_id

        type_ = self.type_

        voted: None | str | Unset
        if isinstance(self.voted, Unset):
            voted = UNSET
        else:
            voted = self.voted

        voting: None | str | Unset
        if isinstance(self.voting, Unset):
            voting = UNSET
        else:
            voting = self.voting

        vpn_server_id: int | None | Unset
        if isinstance(self.vpn_server_id, Unset):
            vpn_server_id = UNSET
        else:
            vpn_server_id = self.vpn_server_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if ip is not UNSET:
            field_dict["ip"] = ip
        if is_spawning is not UNSET:
            field_dict["isSpawning"] = is_spawning
        if lab_server is not UNSET:
            field_dict["lab_server"] = lab_server
        if name is not UNSET:
            field_dict["name"] = name
        if tier_id is not UNSET:
            field_dict["tier_id"] = tier_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if voted is not UNSET:
            field_dict["voted"] = voted
        if voting is not UNSET:
            field_dict["voting"] = voting
        if vpn_server_id is not UNSET:
            field_dict["vpn_server_id"] = vpn_server_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))

        expires_at = d.pop("expires_at", UNSET)

        id = d.pop("id", UNSET)

        def _parse_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        is_spawning = d.pop("isSpawning", UNSET)

        lab_server = d.pop("lab_server", UNSET)

        name = d.pop("name", UNSET)

        def _parse_tier_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tier_id = _parse_tier_id(d.pop("tier_id", UNSET))

        type_ = d.pop("type", UNSET)

        def _parse_voted(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        voted = _parse_voted(d.pop("voted", UNSET))

        def _parse_voting(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        voting = _parse_voting(d.pop("voting", UNSET))

        def _parse_vpn_server_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vpn_server_id = _parse_vpn_server_id(d.pop("vpn_server_id", UNSET))

        active_machine_info = cls(
            avatar=avatar,
            avatar_url=avatar_url,
            expires_at=expires_at,
            id=id,
            ip=ip,
            is_spawning=is_spawning,
            lab_server=lab_server,
            name=name,
            tier_id=tier_id,
            type_=type_,
            voted=voted,
            voting=voting,
            vpn_server_id=vpn_server_id,
        )

        active_machine_info.additional_properties = d
        return active_machine_info

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
