from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.challenge_suggested_data import ChallengeSuggestedData


T = TypeVar("T", bound="ChallengeSuggestedResponse")


@_attrs_define
class ChallengeSuggestedResponse:
    """Schema definition for Challenge Suggested Response

    Attributes:
        data (ChallengeSuggestedData | Unset):
        message (str | Unset):
        status (bool | Unset):
    """

    data: ChallengeSuggestedData | Unset = UNSET
    message: str | Unset = UNSET
    status: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        message = self.message

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if message is not UNSET:
            field_dict["message"] = message
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.challenge_suggested_data import ChallengeSuggestedData

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: ChallengeSuggestedData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ChallengeSuggestedData.from_dict(_data)

        message = d.pop("message", UNSET)

        status = d.pop("status", UNSET)

        challenge_suggested_response = cls(
            data=data,
            message=message,
            status=status,
        )

        challenge_suggested_response.additional_properties = d
        return challenge_suggested_response

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
