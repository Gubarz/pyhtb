from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MachinePlayInfo")


@_attrs_define
class MachinePlayInfo:
    """
    Attributes:
        is_spawned (bool | None | Unset):
        is_spawning (bool | None | Unset):
        is_active (bool | None | Unset):
        active_player_count (int | None | Unset):
        expires_at (datetime.datetime | None | Unset):
        life_remaining (int | None | Unset):
    """

    is_spawned: bool | None | Unset = UNSET
    is_spawning: bool | None | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    active_player_count: int | None | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    life_remaining: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_spawned: bool | None | Unset
        if isinstance(self.is_spawned, Unset):
            is_spawned = UNSET
        else:
            is_spawned = self.is_spawned

        is_spawning: bool | None | Unset
        if isinstance(self.is_spawning, Unset):
            is_spawning = UNSET
        else:
            is_spawning = self.is_spawning

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        active_player_count: int | None | Unset
        if isinstance(self.active_player_count, Unset):
            active_player_count = UNSET
        else:
            active_player_count = self.active_player_count

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        life_remaining: int | None | Unset
        if isinstance(self.life_remaining, Unset):
            life_remaining = UNSET
        else:
            life_remaining = self.life_remaining

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_spawned is not UNSET:
            field_dict["isSpawned"] = is_spawned
        if is_spawning is not UNSET:
            field_dict["isSpawning"] = is_spawning
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if active_player_count is not UNSET:
            field_dict["active_player_count"] = active_player_count
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if life_remaining is not UNSET:
            field_dict["life_remaining"] = life_remaining

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_is_spawned(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_spawned = _parse_is_spawned(d.pop("isSpawned", UNSET))

        def _parse_is_spawning(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_spawning = _parse_is_spawning(d.pop("isSpawning", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("isActive", UNSET))

        def _parse_active_player_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        active_player_count = _parse_active_player_count(
            d.pop("active_player_count", UNSET)
        )

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_life_remaining(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        life_remaining = _parse_life_remaining(d.pop("life_remaining", UNSET))

        machine_play_info = cls(
            is_spawned=is_spawned,
            is_spawning=is_spawning,
            is_active=is_active,
            active_player_count=active_player_count,
            expires_at=expires_at,
            life_remaining=life_remaining,
        )

        machine_play_info.additional_properties = d
        return machine_play_info

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
