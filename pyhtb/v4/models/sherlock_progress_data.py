from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SherlockProgressData")


@_attrs_define
class SherlockProgressData:
    """
    Attributes:
        is_owned (bool | Unset):
        own_rank (int | Unset):
        progress (int | Unset):
        tasks_answered (int | Unset):
        total_tasks (int | Unset):
    """

    is_owned: bool | Unset = UNSET
    own_rank: int | Unset = UNSET
    progress: int | Unset = UNSET
    tasks_answered: int | Unset = UNSET
    total_tasks: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_owned = self.is_owned

        own_rank = self.own_rank

        progress = self.progress

        tasks_answered = self.tasks_answered

        total_tasks = self.total_tasks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_owned is not UNSET:
            field_dict["is_owned"] = is_owned
        if own_rank is not UNSET:
            field_dict["own_rank"] = own_rank
        if progress is not UNSET:
            field_dict["progress"] = progress
        if tasks_answered is not UNSET:
            field_dict["tasks_answered"] = tasks_answered
        if total_tasks is not UNSET:
            field_dict["total_tasks"] = total_tasks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_owned = d.pop("is_owned", UNSET)

        own_rank = d.pop("own_rank", UNSET)

        progress = d.pop("progress", UNSET)

        tasks_answered = d.pop("tasks_answered", UNSET)

        total_tasks = d.pop("total_tasks", UNSET)

        sherlock_progress_data = cls(
            is_owned=is_owned,
            own_rank=own_rank,
            progress=progress,
            tasks_answered=tasks_answered,
            total_tasks=total_tasks,
        )

        sherlock_progress_data.additional_properties = d
        return sherlock_progress_data

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
