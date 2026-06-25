from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserDashboardSherlock")


@_attrs_define
class UserDashboardSherlock:
    """Summary information for Sherlock investigations displayed in dashboard feeds.

    Attributes:
        url_name (str): Sherlock slug used in URLs.
        difficulty (str): Difficulty rating for the Sherlock.
        url (str): Relative link to the Sherlock page.
        category_id (int): Numerical identifier for the Sherlock category.
        category_name (str): Human readable category label.
        avatar (str): Relative asset path for the Sherlock image.
        avatar_url (str): Absolute URL for the Sherlock image.
        rating (float | None): Average user rating.
        rating_count (int): Count of user ratings.
        tasks_completed (int): Number of Sherlock tasks completed.
        tasks_total (int): Total Sherlock tasks available.
        progress (int): Completion percentage.
        status (None | str): Availability label.
        id (int): Sherlock identifier.
        name (str): Sherlock display name.
        type_ (str): Resource type label (e.g., Retired Sherlock).
    """

    url_name: str
    difficulty: str
    url: str
    category_id: int
    category_name: str
    avatar: str
    avatar_url: str
    rating: float | None
    rating_count: int
    tasks_completed: int
    tasks_total: int
    progress: int
    status: None | str
    id: int
    name: str
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url_name = self.url_name

        difficulty = self.difficulty

        url = self.url

        category_id = self.category_id

        category_name = self.category_name

        avatar = self.avatar

        avatar_url = self.avatar_url

        rating: float | None
        rating = self.rating

        rating_count = self.rating_count

        tasks_completed = self.tasks_completed

        tasks_total = self.tasks_total

        progress = self.progress

        status: None | str
        status = self.status

        id = self.id

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "urlName": url_name,
                "difficulty": difficulty,
                "url": url,
                "categoryID": category_id,
                "categoryName": category_name,
                "avatar": avatar,
                "avatarUrl": avatar_url,
                "rating": rating,
                "ratingCount": rating_count,
                "tasksCompleted": tasks_completed,
                "tasksTotal": tasks_total,
                "progress": progress,
                "status": status,
                "id": id,
                "name": name,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url_name = d.pop("urlName")

        difficulty = d.pop("difficulty")

        url = d.pop("url")

        category_id = d.pop("categoryID")

        category_name = d.pop("categoryName")

        avatar = d.pop("avatar")

        avatar_url = d.pop("avatarUrl")

        def _parse_rating(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        rating = _parse_rating(d.pop("rating"))

        rating_count = d.pop("ratingCount")

        tasks_completed = d.pop("tasksCompleted")

        tasks_total = d.pop("tasksTotal")

        progress = d.pop("progress")

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type")

        user_dashboard_sherlock = cls(
            url_name=url_name,
            difficulty=difficulty,
            url=url,
            category_id=category_id,
            category_name=category_name,
            avatar=avatar,
            avatar_url=avatar_url,
            rating=rating,
            rating_count=rating_count,
            tasks_completed=tasks_completed,
            tasks_total=tasks_total,
            progress=progress,
            status=status,
            id=id,
            name=name,
            type_=type_,
        )

        user_dashboard_sherlock.additional_properties = d
        return user_dashboard_sherlock

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
