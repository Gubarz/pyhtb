from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChallengeActivity")


@_attrs_define
class ChallengeActivity:
    """Schema definition for Challenge Activity

    Attributes:
        created_at (datetime.datetime | Unset):  Example: 2020-02-07T20:03:28.000000Z.
        date (str | Unset):  Example: February 7th, 2020 10:03 pm.
        date_diff (str | Unset):  Example: 4 years ago.
        type_ (str | Unset):  Example: blood.
        user_avatar (None | str | Unset):  Example: /storage/avatars/fd5b946aaadbb0254014fa10a22dd403.png.
        user_id (int | Unset):  Example: 82600.
        user_name (str | Unset):  Example: del_KZx497Ju.
    """

    created_at: datetime.datetime | Unset = UNSET
    date: str | Unset = UNSET
    date_diff: str | Unset = UNSET
    type_: str | Unset = UNSET
    user_avatar: None | str | Unset = UNSET
    user_id: int | Unset = UNSET
    user_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

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
        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

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

        challenge_activity = cls(
            created_at=created_at,
            date=date,
            date_diff=date_diff,
            type_=type_,
            user_avatar=user_avatar,
            user_id=user_id,
            user_name=user_name,
        )

        challenge_activity.additional_properties = d
        return challenge_activity

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
