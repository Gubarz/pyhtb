from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserDashboardMachine")


@_attrs_define
class UserDashboardMachine:
    """Summary information for a machine card shown on dashboard endpoints.

    Attributes:
        os (str): Operating system of the machine.
        difficulty (str): Difficulty label as shown in the UI.
        avatar (str): Relative asset path for the machine avatar.
        url (str): Relative link to the machine detail page.
        user_flag (bool): Indicates whether the user captured the user flag.
        root_flag (bool): Indicates whether the user captured the root flag.
        avatar_url (str): Absolute URL for the machine avatar.
        points (int | None): Points awarded for the machine.
        rating (float | None): Average user rating.
        rating_count (int): Number of ratings submitted.
        tasks_completed (int): Tasks completed within the machine entry.
        tasks_total (int): Total tasks available for the machine entry.
        progress (int): Overall completion percentage.
        guided (bool): Whether the machine is part of a guided experience.
        status (None | str): Subscription requirement or availability label.
        id (int): Internal machine identifier.
        name (str): Machine display name.
        type_ (str): Machine status label (e.g., Active Machine).
        experience_points (int):
    """

    os: str
    difficulty: str
    avatar: str
    url: str
    user_flag: bool
    root_flag: bool
    avatar_url: str
    points: int | None
    rating: float | None
    rating_count: int
    tasks_completed: int
    tasks_total: int
    progress: int
    guided: bool
    status: None | str
    id: int
    name: str
    type_: str
    experience_points: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        os = self.os

        difficulty = self.difficulty

        avatar = self.avatar

        url = self.url

        user_flag = self.user_flag

        root_flag = self.root_flag

        avatar_url = self.avatar_url

        points: int | None
        points = self.points

        rating: float | None
        rating = self.rating

        rating_count = self.rating_count

        tasks_completed = self.tasks_completed

        tasks_total = self.tasks_total

        progress = self.progress

        guided = self.guided

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
                "os": os,
                "difficulty": difficulty,
                "avatar": avatar,
                "url": url,
                "user_flag": user_flag,
                "root_flag": root_flag,
                "avatarUrl": avatar_url,
                "points": points,
                "rating": rating,
                "ratingCount": rating_count,
                "tasksCompleted": tasks_completed,
                "tasksTotal": tasks_total,
                "progress": progress,
                "guided": guided,
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
        os = d.pop("os")

        difficulty = d.pop("difficulty")

        avatar = d.pop("avatar")

        url = d.pop("url")

        user_flag = d.pop("user_flag")

        root_flag = d.pop("root_flag")

        avatar_url = d.pop("avatarUrl")

        def _parse_points(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        points = _parse_points(d.pop("points"))

        def _parse_rating(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        rating = _parse_rating(d.pop("rating"))

        rating_count = d.pop("ratingCount")

        tasks_completed = d.pop("tasksCompleted")

        tasks_total = d.pop("tasksTotal")

        progress = d.pop("progress")

        guided = d.pop("guided")

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))

        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type")

        experience_points = d.pop("experiencePoints")

        user_dashboard_machine = cls(
            os=os,
            difficulty=difficulty,
            avatar=avatar,
            url=url,
            user_flag=user_flag,
            root_flag=root_flag,
            avatar_url=avatar_url,
            points=points,
            rating=rating,
            rating_count=rating_count,
            tasks_completed=tasks_completed,
            tasks_total=tasks_total,
            progress=progress,
            guided=guided,
            status=status,
            id=id,
            name=name,
            type_=type_,
            experience_points=experience_points,
        )

        user_dashboard_machine.additional_properties = d
        return user_dashboard_machine

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
