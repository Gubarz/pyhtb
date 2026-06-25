from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.review_user import ReviewUser


T = TypeVar("T", bound="BloodInfo")


@_attrs_define
class BloodInfo:
    """Schema definition for Blood Info

    Attributes:
        blood_difference (str | Unset):
        created_at (str | Unset):
        user (None | ReviewUser | Unset):
    """

    blood_difference: str | Unset = UNSET
    created_at: str | Unset = UNSET
    user: None | ReviewUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.review_user import ReviewUser

        blood_difference = self.blood_difference

        created_at = self.created_at

        user: dict[str, Any] | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, ReviewUser):
            user = self.user.to_dict()
        else:
            user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blood_difference is not UNSET:
            field_dict["blood_difference"] = blood_difference
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.review_user import ReviewUser

        d = dict(src_dict)
        blood_difference = d.pop("blood_difference", UNSET)

        created_at = d.pop("created_at", UNSET)

        def _parse_user(data: object) -> None | ReviewUser | Unset:
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

        user = _parse_user(d.pop("user", UNSET))

        blood_info = cls(
            blood_difference=blood_difference,
            created_at=created_at,
            user=user,
        )

        blood_info.additional_properties = d
        return blood_info

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
