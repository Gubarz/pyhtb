from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_array_item import ObjectArrayItem
    from ..models.task_type import TaskType


T = TypeVar("T", bound="FlagRatingTask")


@_attrs_define
class FlagRatingTask:
    """
    Attributes:
        flag_rating (int):
        completed (bool | Unset):
        description (str | Unset):
        hint (None | str | Unset):
        id (int | Unset):
        masked_flag (str | Unset):
        options (list[ObjectArrayItem] | Unset):
        prerequisite_id (int | None | Unset):
        task_type (TaskType | Unset):
        title (str | Unset):
        type_ (TaskType | Unset):
    """

    flag_rating: int
    completed: bool | Unset = UNSET
    description: str | Unset = UNSET
    hint: None | str | Unset = UNSET
    id: int | Unset = UNSET
    masked_flag: str | Unset = UNSET
    options: list[ObjectArrayItem] | Unset = UNSET
    prerequisite_id: int | None | Unset = UNSET
    task_type: TaskType | Unset = UNSET
    title: str | Unset = UNSET
    type_: TaskType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flag_rating = self.flag_rating

        completed = self.completed

        description = self.description

        hint: None | str | Unset
        if isinstance(self.hint, Unset):
            hint = UNSET
        else:
            hint = self.hint

        id = self.id

        masked_flag = self.masked_flag

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for componentsschemas_object_array_item_data in self.options:
                componentsschemas_object_array_item = (
                    componentsschemas_object_array_item_data.to_dict()
                )
                options.append(componentsschemas_object_array_item)

        prerequisite_id: int | None | Unset
        if isinstance(self.prerequisite_id, Unset):
            prerequisite_id = UNSET
        else:
            prerequisite_id = self.prerequisite_id

        task_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.to_dict()

        title = self.title

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "flag_rating": flag_rating,
            }
        )
        if completed is not UNSET:
            field_dict["completed"] = completed
        if description is not UNSET:
            field_dict["description"] = description
        if hint is not UNSET:
            field_dict["hint"] = hint
        if id is not UNSET:
            field_dict["id"] = id
        if masked_flag is not UNSET:
            field_dict["masked_flag"] = masked_flag
        if options is not UNSET:
            field_dict["options"] = options
        if prerequisite_id is not UNSET:
            field_dict["prerequisite_id"] = prerequisite_id
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_array_item import ObjectArrayItem
        from ..models.task_type import TaskType

        d = dict(src_dict)
        flag_rating = d.pop("flag_rating")

        completed = d.pop("completed", UNSET)

        description = d.pop("description", UNSET)

        def _parse_hint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hint = _parse_hint(d.pop("hint", UNSET))

        id = d.pop("id", UNSET)

        masked_flag = d.pop("masked_flag", UNSET)

        _options = d.pop("options", UNSET)
        options: list[ObjectArrayItem] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for componentsschemas_object_array_item_data in _options:
                componentsschemas_object_array_item = ObjectArrayItem.from_dict(
                    componentsschemas_object_array_item_data
                )

                options.append(componentsschemas_object_array_item)

        def _parse_prerequisite_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prerequisite_id = _parse_prerequisite_id(d.pop("prerequisite_id", UNSET))

        _task_type = d.pop("task_type", UNSET)
        task_type: TaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = TaskType.from_dict(_task_type)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: TaskType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TaskType.from_dict(_type_)

        flag_rating_task = cls(
            flag_rating=flag_rating,
            completed=completed,
            description=description,
            hint=hint,
            id=id,
            masked_flag=masked_flag,
            options=options,
            prerequisite_id=prerequisite_id,
            task_type=task_type,
            title=title,
            type_=type_,
        )

        flag_rating_task.additional_properties = d
        return flag_rating_task

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
