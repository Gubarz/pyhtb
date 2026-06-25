from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_task import UserTask


T = TypeVar("T", bound="TaskFlagResponse")


@_attrs_define
class TaskFlagResponse:
    """Schema definition for Task Flag Response

    Attributes:
        message (str | Unset):  Example: Task flag owned!.
        user_task (UserTask | Unset):
    """

    message: str | Unset = UNSET
    user_task: UserTask | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        user_task: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_task, Unset):
            user_task = self.user_task.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if user_task is not UNSET:
            field_dict["user_task"] = user_task

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_task import UserTask

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _user_task = d.pop("user_task", UNSET)
        user_task: UserTask | Unset
        if isinstance(_user_task, Unset):
            user_task = UNSET
        else:
            user_task = UserTask.from_dict(_user_task)

        task_flag_response = cls(
            message=message,
            user_task=user_task,
        )

        task_flag_response.additional_properties = d
        return task_flag_response

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
