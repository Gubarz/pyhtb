from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SherlockRetiresType0")


@_attrs_define
class SherlockRetiresType0:
    """
    Attributes:
        name (str | Unset):
        difficulty (str | Unset):
        avatar_url (str | Unset):
    """

    name: str | Unset = UNSET
    difficulty: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        difficulty = self.difficulty

        avatar_url = self.avatar_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        difficulty = d.pop("difficulty", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        sherlock_retires_type_0 = cls(
            name=name,
            difficulty=difficulty,
            avatar_url=avatar_url,
        )

        sherlock_retires_type_0.additional_properties = d
        return sherlock_retires_type_0

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
