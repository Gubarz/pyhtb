from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileProgressChallengeOwns")


@_attrs_define
class ProfileProgressChallengeOwns:
    """
    Attributes:
        percentage (float | Unset):
        solved (int | Unset):
        total (int | Unset):
    """

    percentage: float | Unset = UNSET
    solved: int | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        percentage = self.percentage

        solved = self.solved

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if solved is not UNSET:
            field_dict["solved"] = solved
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        percentage = d.pop("percentage", UNSET)

        solved = d.pop("solved", UNSET)

        total = d.pop("total", UNSET)

        profile_progress_challenge_owns = cls(
            percentage=percentage,
            solved=solved,
            total=total,
        )

        profile_progress_challenge_owns.additional_properties = d
        return profile_progress_challenge_owns

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
