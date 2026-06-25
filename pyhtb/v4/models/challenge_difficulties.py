from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChallengeDifficulties")


@_attrs_define
class ChallengeDifficulties:
    """
    Attributes:
        completion_percentage (float | Unset):
        name (str | Unset):
        owned_challenges (float | Unset):
        total_challenges (float | Unset):
    """

    completion_percentage: float | Unset = UNSET
    name: str | Unset = UNSET
    owned_challenges: float | Unset = UNSET
    total_challenges: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        completion_percentage = self.completion_percentage

        name = self.name

        owned_challenges = self.owned_challenges

        total_challenges = self.total_challenges

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completion_percentage is not UNSET:
            field_dict["completion_percentage"] = completion_percentage
        if name is not UNSET:
            field_dict["name"] = name
        if owned_challenges is not UNSET:
            field_dict["owned_challenges"] = owned_challenges
        if total_challenges is not UNSET:
            field_dict["total_challenges"] = total_challenges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        completion_percentage = d.pop("completion_percentage", UNSET)

        name = d.pop("name", UNSET)

        owned_challenges = d.pop("owned_challenges", UNSET)

        total_challenges = d.pop("total_challenges", UNSET)

        challenge_difficulties = cls(
            completion_percentage=completion_percentage,
            name=name,
            owned_challenges=owned_challenges,
            total_challenges=total_challenges,
        )

        challenge_difficulties.additional_properties = d
        return challenge_difficulties

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
