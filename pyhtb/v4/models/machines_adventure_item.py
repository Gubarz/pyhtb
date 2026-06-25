from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_type import TaskType


T = TypeVar("T", bound="MachinesAdventureItem")


@_attrs_define
class MachinesAdventureItem:
    """
    Attributes:
        completed (bool | Unset):
        description (None | str | Unset):
        flag_rating (float | None | Unset):
        hint (None | str | Unset):
        id (int | None | Unset):
        masked_flag (str | Unset):
        title (str | Unset):
        type_ (TaskType | Unset):
    """

    completed: bool | Unset = UNSET
    description: None | str | Unset = UNSET
    flag_rating: float | None | Unset = UNSET
    hint: None | str | Unset = UNSET
    id: int | None | Unset = UNSET
    masked_flag: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: TaskType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        completed = self.completed

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        flag_rating: float | None | Unset
        if isinstance(self.flag_rating, Unset):
            flag_rating = UNSET
        else:
            flag_rating = self.flag_rating

        hint: None | str | Unset
        if isinstance(self.hint, Unset):
            hint = UNSET
        else:
            hint = self.hint

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        masked_flag = self.masked_flag

        title = self.title

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completed is not UNSET:
            field_dict["completed"] = completed
        if description is not UNSET:
            field_dict["description"] = description
        if flag_rating is not UNSET:
            field_dict["flag_rating"] = flag_rating
        if hint is not UNSET:
            field_dict["hint"] = hint
        if id is not UNSET:
            field_dict["id"] = id
        if masked_flag is not UNSET:
            field_dict["masked_flag"] = masked_flag
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_type import TaskType

        d = dict(src_dict)
        completed = d.pop("completed", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_flag_rating(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        flag_rating = _parse_flag_rating(d.pop("flag_rating", UNSET))

        def _parse_hint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hint = _parse_hint(d.pop("hint", UNSET))

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        masked_flag = d.pop("masked_flag", UNSET)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: TaskType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TaskType.from_dict(_type_)

        machines_adventure_item = cls(
            completed=completed,
            description=description,
            flag_rating=flag_rating,
            hint=hint,
            id=id,
            masked_flag=masked_flag,
            title=title,
            type_=type_,
        )

        machines_adventure_item.additional_properties = d
        return machines_adventure_item

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
