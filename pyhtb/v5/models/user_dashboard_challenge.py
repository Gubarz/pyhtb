from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserDashboardChallenge")


@_attrs_define
class UserDashboardChallenge:
    """Summary information for a challenge card surfaced on dashboard endpoints.

    Attributes:
        difficulty (str): Challenge difficulty label.
        url (str): Relative link to the challenge page.
        avatar (str): Relative asset path for the challenge category icon.
        url_name (str): Challenge slug used in URLs.
        points (int | None): Points available for the challenge.
        category_id (int): Numerical identifier for the challenge category.
        category_name (str): Name of the challenge category.
        avatar_url (str): Absolute URL for the challenge avatar.
        rating (float | None): Average user rating for the challenge.
        rating_count (int): Number of rating submissions.
        progress (int | None): Completion percentage for the challenge if applicable.
        status (None | str): Availability label such as vip.
        id (int): Challenge identifier.
        name (str): Challenge display name.
        type_ (str): Resource type label (e.g., Retired Challenge).
        experience_points (int):
    """

    difficulty: str
    url: str
    avatar: str
    url_name: str
    points: int | None
    category_id: int
    category_name: str
    avatar_url: str
    rating: float | None
    rating_count: int
    progress: int | None
    status: None | str
    id: int
    name: str
    type_: str
    experience_points: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        difficulty = self.difficulty

        url = self.url

        avatar = self.avatar

        url_name = self.url_name

        points: int | None
        points = self.points

        category_id = self.category_id

        category_name = self.category_name

        avatar_url = self.avatar_url

        rating: float | None
        rating = self.rating

        rating_count = self.rating_count

        progress: int | None
        progress = self.progress

        status: None | str
        status = self.status

        id = self.id

        name = self.name

        type_ = self.type_

        experience_points = self.experience_points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "difficulty": difficulty,
                "url": url,
                "avatar": avatar,
                "urlName": url_name,
                "points": points,
                "categoryID": category_id,
                "categoryName": category_name,
                "avatarUrl": avatar_url,
                "rating": rating,
                "ratingCount": rating_count,
                "progress": progress,
                "status": status,
                "id": id,
                "name": name,
                "type": type_,
                "experiencePoints": experience_points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        difficulty = d.pop("difficulty")

        url = d.pop("url")

        avatar = d.pop("avatar")

        url_name = d.pop("urlName")

        def _parse_points(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        points = _parse_points(d.pop("points"))

        category_id = d.pop("categoryID")

        category_name = d.pop("categoryName")

        avatar_url = d.pop("avatarUrl")

        def _parse_rating(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        rating = _parse_rating(d.pop("rating"))

        rating_count = d.pop("ratingCount")

        def _parse_progress(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        progress = _parse_progress(d.pop("progress"))

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type")

        experience_points = d.pop("experiencePoints")

        user_dashboard_challenge = cls(
            difficulty=difficulty,
            url=url,
            avatar=avatar,
            url_name=url_name,
            points=points,
            category_id=category_id,
            category_name=category_name,
            avatar_url=avatar_url,
            rating=rating,
            rating_count=rating_count,
            progress=progress,
            status=status,
            id=id,
            name=name,
            type_=type_,
            experience_points=experience_points,
        )

        user_dashboard_challenge.additional_properties = d
        return user_dashboard_challenge

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
