from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MachineChangeLogItem")


@_attrs_define
class MachineChangeLogItem:
    """
    Attributes:
        created_at (str | Unset):
        description (str | Unset):
        id (int | Unset):
        machine_id (int | Unset):
        released (int | Unset):
        title (str | Unset):
        type_ (str | Unset):
        updated_at (str | Unset):
        user_id (int | Unset):
    """

    created_at: str | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    machine_id: int | Unset = UNSET
    released: int | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    user_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        description = self.description

        id = self.id

        machine_id = self.machine_id

        released = self.released

        title = self.title

        type_ = self.type_

        updated_at = self.updated_at

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if machine_id is not UNSET:
            field_dict["machine_id"] = machine_id
        if released is not UNSET:
            field_dict["released"] = released
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        machine_id = d.pop("machine_id", UNSET)

        released = d.pop("released", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        user_id = d.pop("user_id", UNSET)

        machine_change_log_item = cls(
            created_at=created_at,
            description=description,
            id=id,
            machine_id=machine_id,
            released=released,
            title=title,
            type_=type_,
            updated_at=updated_at,
            user_id=user_id,
        )

        machine_change_log_item.additional_properties = d
        return machine_change_log_item

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
