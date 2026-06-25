from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PwnboxStatusRUnningData")


@_attrs_define
class PwnboxStatusRUnningData:
    """
    Attributes:
        created_at (datetime.datetime | Unset):
        expires_at (datetime.datetime | Unset):
        flock_id (int | Unset):
        hostname (str | Unset):
        id (int | Unset):
        is_ready (bool | Unset):
        life_remaining (int | Unset):
        location (str | Unset):
        proxy_url (str | Unset):
        spectate_url (str | Unset):
        status (str | Unset):
        updated_at (datetime.datetime | Unset):
        username (str | Unset):
        vnc_password (str | Unset):
        vnc_view_only_password (str | Unset):
    """

    created_at: datetime.datetime | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    flock_id: int | Unset = UNSET
    hostname: str | Unset = UNSET
    id: int | Unset = UNSET
    is_ready: bool | Unset = UNSET
    life_remaining: int | Unset = UNSET
    location: str | Unset = UNSET
    proxy_url: str | Unset = UNSET
    spectate_url: str | Unset = UNSET
    status: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    username: str | Unset = UNSET
    vnc_password: str | Unset = UNSET
    vnc_view_only_password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        flock_id = self.flock_id

        hostname = self.hostname

        id = self.id

        is_ready = self.is_ready

        life_remaining = self.life_remaining

        location = self.location

        proxy_url = self.proxy_url

        spectate_url = self.spectate_url

        status = self.status

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        username = self.username

        vnc_password = self.vnc_password

        vnc_view_only_password = self.vnc_view_only_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if flock_id is not UNSET:
            field_dict["flock_id"] = flock_id
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if id is not UNSET:
            field_dict["id"] = id
        if is_ready is not UNSET:
            field_dict["is_ready"] = is_ready
        if life_remaining is not UNSET:
            field_dict["life_remaining"] = life_remaining
        if location is not UNSET:
            field_dict["location"] = location
        if proxy_url is not UNSET:
            field_dict["proxy_url"] = proxy_url
        if spectate_url is not UNSET:
            field_dict["spectate_url"] = spectate_url
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if username is not UNSET:
            field_dict["username"] = username
        if vnc_password is not UNSET:
            field_dict["vnc_password"] = vnc_password
        if vnc_view_only_password is not UNSET:
            field_dict["vnc_view_only_password"] = vnc_view_only_password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)

        flock_id = d.pop("flock_id", UNSET)

        hostname = d.pop("hostname", UNSET)

        id = d.pop("id", UNSET)

        is_ready = d.pop("is_ready", UNSET)

        life_remaining = d.pop("life_remaining", UNSET)

        location = d.pop("location", UNSET)

        proxy_url = d.pop("proxy_url", UNSET)

        spectate_url = d.pop("spectate_url", UNSET)

        status = d.pop("status", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        username = d.pop("username", UNSET)

        vnc_password = d.pop("vnc_password", UNSET)

        vnc_view_only_password = d.pop("vnc_view_only_password", UNSET)

        pwnbox_status_r_unning_data = cls(
            created_at=created_at,
            expires_at=expires_at,
            flock_id=flock_id,
            hostname=hostname,
            id=id,
            is_ready=is_ready,
            life_remaining=life_remaining,
            location=location,
            proxy_url=proxy_url,
            spectate_url=spectate_url,
            status=status,
            updated_at=updated_at,
            username=username,
            vnc_password=vnc_password,
            vnc_view_only_password=vnc_view_only_password,
        )

        pwnbox_status_r_unning_data.additional_properties = d
        return pwnbox_status_r_unning_data

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
