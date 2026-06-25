from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChallengeCategories")


@_attrs_define
class ChallengeCategories:
    """
    Attributes:
        avg_user_solved (float | Unset):
        completion_percentage (float | Unset):
        name (str | Unset):
        owned_flags (float | Unset):
        total_flags (float | Unset):
    """

    avg_user_solved: float | Unset = UNSET
    completion_percentage: float | Unset = UNSET
    name: str | Unset = UNSET
    owned_flags: float | Unset = UNSET
    total_flags: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_user_solved = self.avg_user_solved

        completion_percentage = self.completion_percentage

        name = self.name

        owned_flags = self.owned_flags

        total_flags = self.total_flags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_user_solved is not UNSET:
            field_dict["avg_user_solved"] = avg_user_solved
        if completion_percentage is not UNSET:
            field_dict["completion_percentage"] = completion_percentage
        if name is not UNSET:
            field_dict["name"] = name
        if owned_flags is not UNSET:
            field_dict["owned_flags"] = owned_flags
        if total_flags is not UNSET:
            field_dict["total_flags"] = total_flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_user_solved = d.pop("avg_user_solved", UNSET)

        completion_percentage = d.pop("completion_percentage", UNSET)

        name = d.pop("name", UNSET)

        owned_flags = d.pop("owned_flags", UNSET)

        total_flags = d.pop("total_flags", UNSET)

        challenge_categories = cls(
            avg_user_solved=avg_user_solved,
            completion_percentage=completion_percentage,
            name=name,
            owned_flags=owned_flags,
            total_flags=total_flags,
        )

        challenge_categories.additional_properties = d
        return challenge_categories

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
