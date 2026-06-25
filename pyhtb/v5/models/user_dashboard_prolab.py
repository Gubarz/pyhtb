from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserDashboardProlab")


@_attrs_define
class UserDashboardProlab:
    """Summary information for Pro Lab entries shown on dashboard endpoints.

    Attributes:
        url (str): Relative link to the Pro Lab overview.
        mini (bool): Is item a mini-prolab or not
        identifier (str): Short identifier or slug.
        difficulty (None | str): Reported difficulty for the lab.
        avatar (None | str): Relative asset path for the lab image.
        avatar_url (str): Absolute URL for the lab image.
        category_name (str): Track or certification name associated with the lab.
        rating (float | None): Average participant rating.
        rating_count (int): Number of participant ratings.
        progress (int): Completion percentage inside the lab.
        tasks_completed (int): Completed task count.
        tasks_total (int): Total task count.
        id (int): Pro Lab identifier.
        name (str): Pro Lab display name.
        type_ (str): Resource type label (e.g., Pro Lab).
    """

    url: str
    mini: bool
    identifier: str
    difficulty: None | str
    avatar: None | str
    avatar_url: str
    category_name: str
    rating: float | None
    rating_count: int
    progress: int
    tasks_completed: int
    tasks_total: int
    id: int
    name: str
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        mini = self.mini

        identifier = self.identifier

        difficulty: None | str
        difficulty = self.difficulty

        avatar: None | str
        avatar = self.avatar

        avatar_url = self.avatar_url

        category_name = self.category_name

        rating: float | None
        rating = self.rating

        rating_count = self.rating_count

        progress = self.progress

        tasks_completed = self.tasks_completed

        tasks_total = self.tasks_total

        id = self.id

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "mini": mini,
                "identifier": identifier,
                "difficulty": difficulty,
                "avatar": avatar,
                "avatarUrl": avatar_url,
                "categoryName": category_name,
                "rating": rating,
                "ratingCount": rating_count,
                "progress": progress,
                "tasksCompleted": tasks_completed,
                "tasksTotal": tasks_total,
                "id": id,
                "name": name,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        mini = d.pop("mini")

        identifier = d.pop("identifier")

        def _parse_difficulty(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        difficulty = _parse_difficulty(d.pop("difficulty"))

        def _parse_avatar(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        avatar = _parse_avatar(d.pop("avatar"))

        avatar_url = d.pop("avatarUrl")

        category_name = d.pop("categoryName")

        def _parse_rating(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        rating = _parse_rating(d.pop("rating"))

        rating_count = d.pop("ratingCount")

        progress = d.pop("progress")

        tasks_completed = d.pop("tasksCompleted")

        tasks_total = d.pop("tasksTotal")

        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type")

        user_dashboard_prolab = cls(
            url=url,
            mini=mini,
            identifier=identifier,
            difficulty=difficulty,
            avatar=avatar,
            avatar_url=avatar_url,
            category_name=category_name,
            rating=rating,
            rating_count=rating_count,
            progress=progress,
            tasks_completed=tasks_completed,
            tasks_total=tasks_total,
            id=id,
            name=name,
            type_=type_,
        )

        user_dashboard_prolab.additional_properties = d
        return user_dashboard_prolab

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
