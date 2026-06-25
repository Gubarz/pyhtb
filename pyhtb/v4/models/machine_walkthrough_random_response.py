from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.review_user import ReviewUser


T = TypeVar("T", bound="MachineWalkthroughRandomResponse")


@_attrs_define
class MachineWalkthroughRandomResponse:
    """
    Attributes:
        message (None | ReviewUser | Unset):
    """

    message: None | ReviewUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.review_user import ReviewUser

        message: dict[str, Any] | None | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        elif isinstance(self.message, ReviewUser):
            message = self.message.to_dict()
        else:
            message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.review_user import ReviewUser

        d = dict(src_dict)

        def _parse_message(data: object) -> None | ReviewUser | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_basic_info_type_0 = ReviewUser.from_dict(data)

                return componentsschemas_user_basic_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReviewUser | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        machine_walkthrough_random_response = cls(
            message=message,
        )

        machine_walkthrough_random_response.additional_properties = d
        return machine_walkthrough_random_response

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
