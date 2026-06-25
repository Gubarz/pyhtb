from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OwnRequest")


@_attrs_define
class OwnRequest:
    """Schema definition for Own Request

    Attributes:
        flag (str): MD5 hash of the machine flag Example: 0cc175b9c0f1b6a831c399e269772661.
        id (int): The machine ID Example: 597.
        difficulty (int | Unset):  Example: 50.
    """

    flag: str
    id: int
    difficulty: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flag = self.flag

        id = self.id

        difficulty = self.difficulty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "flag": flag,
                "id": id,
            }
        )
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        flag = d.pop("flag")

        id = d.pop("id")

        difficulty = d.pop("difficulty", UNSET)

        own_request = cls(
            flag=flag,
            id=id,
            difficulty=difficulty,
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
