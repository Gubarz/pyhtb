from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.challenge import Challenge


T = TypeVar("T", bound="ChallengeIdResponse")


@_attrs_define
class ChallengeIdResponse:
    """Schema definition for Challenge Id Response

    Attributes:
        challenge (Challenge | Unset): Schema definition for Challenge
    """

    challenge: Challenge | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenge: dict[str, Any] | Unset = UNSET
        if not isinstance(self.challenge, Unset):
            challenge = self.challenge.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if challenge is not UNSET:
            field_dict["challenge"] = challenge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.challenge import Challenge

        d = dict(src_dict)
        _challenge = d.pop("challenge", UNSET)
        challenge: Challenge | Unset
        if isinstance(_challenge, Unset):
            challenge = UNSET
        else:
            challenge = Challenge.from_dict(_challenge)

        challenge_id_response = cls(
            challenge=challenge,
        )

        challenge_id_response.additional_properties = d
        return challenge_id_response

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
