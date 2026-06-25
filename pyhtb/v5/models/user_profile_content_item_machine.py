from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserProfileContentItemMachine")


@_attrs_define
class UserProfileContentItemMachine:
    """Machine entry returned by the user profile content feed.

    Attributes:
        id (int): Machine identifier.
        name (str): Machine display name.
        os (str): Operating system of the machine.
        machine_avatar (str): Absolute URL to the machine avatar.
        difficulty (str): Machine difficulty label.
        star_rating (float): Average star rating.
        user_own_count (int): Number of user owns for the profile owner.
        root_own_count (int): Number of root owns for the profile owner.
        release_date (datetime.datetime): Machine release timestamp.
        rating_count (int): Number of ratings submitted for the machine.
    """

    id: int
    name: str
    os: str
    machine_avatar: str
    difficulty: str
    star_rating: float
    user_own_count: int
    root_own_count: int
    release_date: datetime.datetime
    rating_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        os = self.os

        machine_avatar = self.machine_avatar

        difficulty = self.difficulty

        star_rating = self.star_rating

        user_own_count = self.user_own_count

        root_own_count = self.root_own_count

        release_date = self.release_date.isoformat()

        rating_count = self.rating_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "os": os,
                "machineAvatar": machine_avatar,
                "difficulty": difficulty,
                "starRating": star_rating,
                "userOwnCount": user_own_count,
                "rootOwnCount": root_own_count,
                "releaseDate": release_date,
                "ratingCount": rating_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        os = d.pop("os")

        machine_avatar = d.pop("machineAvatar")

        difficulty = d.pop("difficulty")

        star_rating = d.pop("starRating")

        user_own_count = d.pop("userOwnCount")

        root_own_count = d.pop("rootOwnCount")

        release_date = datetime.datetime.fromisoformat(d.pop("releaseDate"))

        rating_count = d.pop("ratingCount")

        user_profile_content_item_machine = cls(
            id=id,
            name=name,
            os=os,
            machine_avatar=machine_avatar,
            difficulty=difficulty,
            star_rating=star_rating,
            user_own_count=user_own_count,
            root_own_count=root_own_count,
            release_date=release_date,
            rating_count=rating_count,
        )

        user_profile_content_item_machine.additional_properties = d
        return user_profile_content_item_machine

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
