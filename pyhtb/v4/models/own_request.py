from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OwnRequest")


@_attrs_define
class OwnRequest:
    """Schema definition for Own Request

    Attributes:
        challenge_id (int):  Example: 597.
        flag (str):  Example: 0cc175b9c0f1b6a831c399e269772661.
    """

    challenge_id: int
    flag: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenge_id = self.challenge_id

        flag = self.flag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "challenge_id": challenge_id,
                "flag": flag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        challenge_id = d.pop("challenge_id")

        flag = d.pop("flag")

        own_request = cls(
            challenge_id=challenge_id,
            flag=flag,
        )

        own_request.additional_properties = d
        return own_request

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
