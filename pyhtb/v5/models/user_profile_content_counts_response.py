from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserProfileContentCountsResponse")


@_attrs_define
class UserProfileContentCountsResponse:
    """Schema definition for User Profile Content Counts responses

    Attributes:
        machine (int):
        challenge (int):
        sherlock (int):
        writeup (int):
    """

    machine: int
    challenge: int
    sherlock: int
    writeup: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        machine = self.machine

        challenge = self.challenge

        sherlock = self.sherlock

        writeup = self.writeup

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "machine": machine,
                "challenge": challenge,
                "sherlock": sherlock,
                "writeup": writeup,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        machine = d.pop("machine")

        challenge = d.pop("challenge")

        sherlock = d.pop("sherlock")

        writeup = d.pop("writeup")

        user_profile_content_counts_response = cls(
            machine=machine,
            challenge=challenge,
            sherlock=sherlock,
            writeup=writeup,
        )

        user_profile_content_counts_response.additional_properties = d
        return user_profile_content_counts_response

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
