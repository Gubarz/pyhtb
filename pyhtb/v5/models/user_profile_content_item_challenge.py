from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserProfileContentItemChallenge")


@_attrs_define
class UserProfileContentItemChallenge:
    """Challenge entry returned by the user profile content feed.

    Attributes:
        id (int): Challenge identifier.
        name (str): Challenge display name.
        category_name (str): Challenge category name.
        star_rating (float): Average star rating.
        difficulty (str): Challenge difficulty label.
        own_count (int): User completion count.
        release_date (datetime.datetime): Challenge release timestamp.
        rating_count (int): Number of ratings recorded for the challenge.
    """

    id: int
    name: str
    category_name: str
    star_rating: float
    difficulty: str
    own_count: int
    release_date: datetime.datetime
    rating_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        category_name = self.category_name

        star_rating = self.star_rating

        difficulty = self.difficulty

        own_count = self.own_count

        release_date = self.release_date.isoformat()

        rating_count = self.rating_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "categoryName": category_name,
                "starRating": star_rating,
                "difficulty": difficulty,
                "ownCount": own_count,
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

        category_name = d.pop("categoryName")

        star_rating = d.pop("starRating")

        difficulty = d.pop("difficulty")

        own_count = d.pop("ownCount")

        release_date = datetime.datetime.fromisoformat(d.pop("releaseDate"))

        rating_count = d.pop("ratingCount")

        user_profile_content_item_challenge = cls(
            id=id,
            name=name,
            category_name=category_name,
            star_rating=star_rating,
            difficulty=difficulty,
            own_count=own_count,
            release_date=release_date,
            rating_count=rating_count,
        )

        user_profile_content_item_challenge.additional_properties = d
        return user_profile_content_item_challenge

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
