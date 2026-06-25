from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserDashboardStartingPoint")


@_attrs_define
class UserDashboardStartingPoint:
    """Summary information for a Starting Point tier card.

    Attributes:
        description (str): Short tier description shown in the dashboard.
        completion_percentage (int): Overall completion percentage for the tier.
        free_machine_completion_percentage (int): Completion percentage for free machines within the tier.
        avatar (str): Relative asset path for the tier avatar.
        avatar_url (str): Absolute URL to the tier avatar.
        progress (int): Percentage progress toward finishing the tier.
        tasks_completed (int): Number of tasks completed.
        tasks_total (int): Total number of tasks available.
        id (int): Tier identifier.
        name (str): Tier display name.
        type_ (str): Resource type label (e.g., Starting Point).
    """

    description: str
    completion_percentage: int
    free_machine_completion_percentage: int
    avatar: str
    avatar_url: str
    progress: int
    tasks_completed: int
    tasks_total: int
    id: int
    name: str
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        completion_percentage = self.completion_percentage

        free_machine_completion_percentage = self.free_machine_completion_percentage

        avatar = self.avatar

        avatar_url = self.avatar_url

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
                "description": description,
                "completionPercentage": completion_percentage,
                "freeMachineCompletionPercentage": free_machine_completion_percentage,
                "avatar": avatar,
                "avatarUrl": avatar_url,
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
        description = d.pop("description")

        completion_percentage = d.pop("completionPercentage")

        free_machine_completion_percentage = d.pop("freeMachineCompletionPercentage")

        avatar = d.pop("avatar")

        avatar_url = d.pop("avatarUrl")

        progress = d.pop("progress")

        tasks_completed = d.pop("tasksCompleted")

        tasks_total = d.pop("tasksTotal")

        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type")

        user_dashboard_starting_point = cls(
            description=description,
            completion_percentage=completion_percentage,
            free_machine_completion_percentage=free_machine_completion_percentage,
            avatar=avatar,
            avatar_url=avatar_url,
            progress=progress,
            tasks_completed=tasks_completed,
            tasks_total=tasks_total,
            id=id,
            name=name,
            type_=type_,
        )

        user_dashboard_starting_point.additional_properties = d
        return user_dashboard_starting_point

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
