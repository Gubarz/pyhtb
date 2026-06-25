from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeasonMachinesDataItem")


@_attrs_define
class SeasonMachinesDataItem:
    """
    Attributes:
        user_points (int | Unset):
        active (bool | Unset):
        avatar (str | Unset):
        difficulty_text (str | Unset):
        id (int | Unset):
        is_user_blood (bool | Unset):
        is_owned_root (bool | Unset):
        is_owned_user (bool | Unset):
        is_released (bool | Unset):
        is_root_blood (bool | Unset):
        name (str | Unset):
        os (str | Unset):
        release_time (datetime.datetime | Unset):
        root_points (int | Unset):
        unknown (bool | Unset):
        production (int | Unset):
        rating (float | Unset):
        rating_count (int | Unset):
        user_blood_points (int | Unset):
        root_blood_points (int | Unset):
    """

    user_points: int | Unset = UNSET
    active: bool | Unset = UNSET
    avatar: str | Unset = UNSET
    difficulty_text: str | Unset = UNSET
    id: int | Unset = UNSET
    is_user_blood: bool | Unset = UNSET
    is_owned_root: bool | Unset = UNSET
    is_owned_user: bool | Unset = UNSET
    is_released: bool | Unset = UNSET
    is_root_blood: bool | Unset = UNSET
    name: str | Unset = UNSET
    os: str | Unset = UNSET
    release_time: datetime.datetime | Unset = UNSET
    root_points: int | Unset = UNSET
    unknown: bool | Unset = UNSET
    production: int | Unset = UNSET
    rating: float | Unset = UNSET
    rating_count: int | Unset = UNSET
    user_blood_points: int | Unset = UNSET
    root_blood_points: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_points = self.user_points

        active = self.active

        avatar = self.avatar

        difficulty_text = self.difficulty_text

        id = self.id

        is_user_blood = self.is_user_blood

        is_owned_root = self.is_owned_root

        is_owned_user = self.is_owned_user

        is_released = self.is_released

        is_root_blood = self.is_root_blood

        name = self.name

        os = self.os

        release_time: str | Unset = UNSET
        if not isinstance(self.release_time, Unset):
            release_time = self.release_time.isoformat()

        root_points = self.root_points

        unknown = self.unknown

        production = self.production

        rating = self.rating

        rating_count = self.rating_count

        user_blood_points = self.user_blood_points

        root_blood_points = self.root_blood_points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_points is not UNSET:
            field_dict["user_points"] = user_points
        if active is not UNSET:
            field_dict["active"] = active
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if difficulty_text is not UNSET:
            field_dict["difficulty_text"] = difficulty_text
        if id is not UNSET:
            field_dict["id"] = id
        if is_user_blood is not UNSET:
            field_dict["is_user_blood"] = is_user_blood
        if is_owned_root is not UNSET:
            field_dict["is_owned_root"] = is_owned_root
        if is_owned_user is not UNSET:
            field_dict["is_owned_user"] = is_owned_user
        if is_released is not UNSET:
            field_dict["is_released"] = is_released
        if is_root_blood is not UNSET:
            field_dict["is_root_blood"] = is_root_blood
        if name is not UNSET:
            field_dict["name"] = name
        if os is not UNSET:
            field_dict["os"] = os
        if release_time is not UNSET:
            field_dict["release_time"] = release_time
        if root_points is not UNSET:
            field_dict["root_points"] = root_points
        if unknown is not UNSET:
            field_dict["unknown"] = unknown
        if production is not UNSET:
            field_dict["production"] = production
        if rating is not UNSET:
            field_dict["rating"] = rating
        if rating_count is not UNSET:
            field_dict["ratingCount"] = rating_count
        if user_blood_points is not UNSET:
            field_dict["user_blood_points"] = user_blood_points
        if root_blood_points is not UNSET:
            field_dict["root_blood_points"] = root_blood_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_points = d.pop("user_points", UNSET)

        active = d.pop("active", UNSET)

        avatar = d.pop("avatar", UNSET)

        difficulty_text = d.pop("difficulty_text", UNSET)

        id = d.pop("id", UNSET)

        is_user_blood = d.pop("is_user_blood", UNSET)

        is_owned_root = d.pop("is_owned_root", UNSET)

        is_owned_user = d.pop("is_owned_user", UNSET)

        is_released = d.pop("is_released", UNSET)

        is_root_blood = d.pop("is_root_blood", UNSET)

        name = d.pop("name", UNSET)

        os = d.pop("os", UNSET)

        _release_time = d.pop("release_time", UNSET)
        release_time: datetime.datetime | Unset
        if isinstance(_release_time, Unset):
            release_time = UNSET
        else:
            release_time = datetime.datetime.fromisoformat(_release_time)

        root_points = d.pop("root_points", UNSET)

        unknown = d.pop("unknown", UNSET)

        production = d.pop("production", UNSET)

        rating = d.pop("rating", UNSET)

        rating_count = d.pop("ratingCount", UNSET)

        user_blood_points = d.pop("user_blood_points", UNSET)

        root_blood_points = d.pop("root_blood_points", UNSET)

        season_machines_data_item = cls(
            user_points=user_points,
            active=active,
            avatar=avatar,
            difficulty_text=difficulty_text,
            id=id,
            is_user_blood=is_user_blood,
            is_owned_root=is_owned_root,
            is_owned_user=is_owned_user,
            is_released=is_released,
            is_root_blood=is_root_blood,
            name=name,
            os=os,
            release_time=release_time,
            root_points=root_points,
            unknown=unknown,
            production=production,
            rating=rating,
            rating_count=rating_count,
            user_blood_points=user_blood_points,
            root_blood_points=root_blood_points,
        )

        season_machines_data_item.additional_properties = d
        return season_machines_data_item

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
