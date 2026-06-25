from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserDashboardTrack")


@_attrs_define
class UserDashboardTrack:
    """Summary information for track cards surfaced on dashboard views.

    Attributes:
        avatar (str): Relative asset path for the track image.
        avatar_url (str): Absolute URL for the track image.
        url (str): Relative link to the track landing page.
        difficulty (str): Difficulty level assigned to the track.
        like_count (int): Number of likes.
        progress (int): Completion percentage inside the track.
        tasks_completed (int): Number of completed tasks.
        tasks_total (int): Total number of tasks.
        id (int): Track identifier.
        name (str): Track display name.
        type_ (str): Resource type label (e.g., Track).
    """

    avatar: str
    avatar_url: str
    url: str
    difficulty: str
    like_count: int
    progress: int
    tasks_completed: int
    tasks_total: int
    id: int
    name: str
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar = self.avatar

        avatar_url = self.avatar_url

        url = self.url

        difficulty = self.difficulty

        like_count = self.like_count

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
                "avatar": avatar,
                "avatarUrl": avatar_url,
                "url": url,
                "difficulty": difficulty,
                "likeCount": like_count,
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
        avatar = d.pop("avatar")

        avatar_url = d.pop("avatarUrl")

        url = d.pop("url")

        difficulty = d.pop("difficulty")

        like_count = d.pop("likeCount")

        progress = d.pop("progress")

        tasks_completed = d.pop("tasksCompleted")

        tasks_total = d.pop("tasksTotal")

        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type")

        user_dashboard_track = cls(
            avatar=avatar,
            avatar_url=avatar_url,
            url=url,
            difficulty=difficulty,
            like_count=like_count,
            progress=progress,
            tasks_completed=tasks_completed,
            tasks_total=tasks_total,
            id=id,
            name=name,
            type_=type_,
        )

        user_dashboard_track.additional_properties = d
        return user_dashboard_track

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
