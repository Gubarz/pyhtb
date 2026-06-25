from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserProfileActivityBase")


@_attrs_define
class UserProfileActivityBase:
    """
    Attributes:
        type_ (str):
        id (int):
        name (str):
        points (int):
        own_date (datetime.datetime):
        avatar (str | Unset):
        blood (bool | None | Unset):
    """

    type_: str
    id: int
    name: str
    points: int
    own_date: datetime.datetime
    avatar: str | Unset = UNSET
    blood: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        name = self.name

        points = self.points

        own_date = self.own_date.isoformat()

        avatar = self.avatar

        blood: bool | None | Unset
        if isinstance(self.blood, Unset):
            blood = UNSET
        else:
            blood = self.blood

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "name": name,
                "points": points,
                "ownDate": own_date,
            }
        )
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if blood is not UNSET:
            field_dict["blood"] = blood

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        id = d.pop("id")

        name = d.pop("name")

        points = d.pop("points")

        own_date = datetime.datetime.fromisoformat(d.pop("ownDate"))

        avatar = d.pop("avatar", UNSET)

        def _parse_blood(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        blood = _parse_blood(d.pop("blood", UNSET))

        user_profile_activity_base = cls(
            type_=type_,
            id=id,
            name=name,
            points=points,
            own_date=own_date,
            avatar=avatar,
            blood=blood,
        )

        user_profile_activity_base.additional_properties = d
        return user_profile_activity_base

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
