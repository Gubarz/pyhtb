from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PwnboxUsageResponse")


@_attrs_define
class PwnboxUsageResponse:
    """Schema definition for Pwnbox Usage Response

    Attributes:
        active_minutes (int | Unset):
        allowed (int | Unset):
        minutes (int | Unset):
        remaining (int | Unset):
        sessions (int | Unset):
        total (int | Unset):
        used (int | Unset):
    """

    active_minutes: int | Unset = UNSET
    allowed: int | Unset = UNSET
    minutes: int | Unset = UNSET
    remaining: int | Unset = UNSET
    sessions: int | Unset = UNSET
    total: int | Unset = UNSET
    used: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_minutes = self.active_minutes

        allowed = self.allowed

        minutes = self.minutes

        remaining = self.remaining

        sessions = self.sessions

        total = self.total

        used = self.used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_minutes is not UNSET:
            field_dict["active_minutes"] = active_minutes
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if sessions is not UNSET:
            field_dict["sessions"] = sessions
        if total is not UNSET:
            field_dict["total"] = total
        if used is not UNSET:
            field_dict["used"] = used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active_minutes = d.pop("active_minutes", UNSET)

        allowed = d.pop("allowed", UNSET)

        minutes = d.pop("minutes", UNSET)

        remaining = d.pop("remaining", UNSET)

        sessions = d.pop("sessions", UNSET)

        total = d.pop("total", UNSET)

        used = d.pop("used", UNSET)

        pwnbox_usage_response = cls(
            active_minutes=active_minutes,
            allowed=allowed,
            minutes=minutes,
            remaining=remaining,
            sessions=sessions,
            total=total,
            used=used,
        )

        pwnbox_usage_response.additional_properties = d
        return pwnbox_usage_response

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
