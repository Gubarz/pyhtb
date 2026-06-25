from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserDashboardFortress")


@_attrs_define
class UserDashboardFortress:
    """Summary information for fortress cards surfaced on dashboard views.

    Attributes:
        points (int): Points available for the fortress.
        avatar_url (str): Absolute URL for the fortress avatar.
        solves_count (int): Number of user solves recorded.
        tasks_completed (int): Completed fortress tasks.
        tasks_total (int): Total fortress tasks.
        progress (int): Completion percentage for the fortress.
        id (int): Fortress identifier.
        name (str): Fortress display name.
        type_ (str): Resource type label (e.g., Fortress).
    """

    points: int
    avatar_url: str
    solves_count: int
    tasks_completed: int
    tasks_total: int
    progress: int
    id: int
    name: str
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        points = self.points

        avatar_url = self.avatar_url

        solves_count = self.solves_count

        tasks_completed = self.tasks_completed

        tasks_total = self.tasks_total

        progress = self.progress

        id = self.id

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "points": points,
                "avatarUrl": avatar_url,
                "solvesCount": solves_count,
                "tasksCompleted": tasks_completed,
                "tasksTotal": tasks_total,
                "progress": progress,
                "id": id,
                "name": name,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        points = d.pop("points")

        avatar_url = d.pop("avatarUrl")

        solves_count = d.pop("solvesCount")

        tasks_completed = d.pop("tasksCompleted")

        tasks_total = d.pop("tasksTotal")

        progress = d.pop("progress")

        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type")

        user_dashboard_fortress = cls(
            points=points,
            avatar_url=avatar_url,
            solves_count=solves_count,
            tasks_completed=tasks_completed,
            tasks_total=tasks_total,
            progress=progress,
            id=id,
            name=name,
            type_=type_,
        )

        user_dashboard_fortress.additional_properties = d
        return user_dashboard_fortress

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
