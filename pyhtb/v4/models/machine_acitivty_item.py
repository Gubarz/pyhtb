from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MachineAcitivtyItem")


@_attrs_define
class MachineAcitivtyItem:
    """
    Attributes:
        blood_type (None | str | Unset):
        created_at (str | Unset):
        date (str | Unset):
        date_diff (str | Unset):
        type_ (str | Unset):
        user_avatar (None | str | Unset):
        user_id (int | Unset):
        user_name (str | Unset):
    """

    blood_type: None | str | Unset = UNSET
    created_at: str | Unset = UNSET
    date: str | Unset = UNSET
    date_diff: str | Unset = UNSET
    type_: str | Unset = UNSET
    user_avatar: None | str | Unset = UNSET
    user_id: int | Unset = UNSET
    user_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blood_type: None | str | Unset
        if isinstance(self.blood_type, Unset):
            blood_type = UNSET
        else:
            blood_type = self.blood_type

        created_at = self.created_at

        date = self.date

        date_diff = self.date_diff

        type_ = self.type_

        user_avatar: None | str | Unset
        if isinstance(self.user_avatar, Unset):
            user_avatar = UNSET
        else:
            user_avatar = self.user_avatar

        user_id = self.user_id

        user_name = self.user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blood_type is not UNSET:
            field_dict["blood_type"] = blood_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if date is not UNSET:
            field_dict["date"] = date
        if date_diff is not UNSET:
            field_dict["date_diff"] = date_diff
        if type_ is not UNSET:
            field_dict["type"] = type_
        if user_avatar is not UNSET:
            field_dict["user_avatar"] = user_avatar
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_name is not UNSET:
            field_dict["user_name"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_blood_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        blood_type = _parse_blood_type(d.pop("blood_type", UNSET))

        created_at = d.pop("created_at", UNSET)

        date = d.pop("date", UNSET)

        date_diff = d.pop("date_diff", UNSET)

        type_ = d.pop("type", UNSET)

        def _parse_user_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_avatar = _parse_user_avatar(d.pop("user_avatar", UNSET))

        user_id = d.pop("user_id", UNSET)

        user_name = d.pop("user_name", UNSET)

        machine_acitivty_item = cls(
            blood_type=blood_type,
            created_at=created_at,
            date=date,
            date_diff=date_diff,
            type_=type_,
            user_avatar=user_avatar,
            user_id=user_id,
            user_name=user_name,
        )

        machine_acitivty_item.additional_properties = d
        return machine_acitivty_item

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
