from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MachineWalkthroughsLanguageListItem")


@_attrs_define
class MachineWalkthroughsLanguageListItem:
    """
    Attributes:
        full_name (str | Unset):
        id (int | Unset):
        short_name (str | Unset):
    """

    full_name: str | Unset = UNSET
    id: int | Unset = UNSET
    short_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_name = self.full_name

        id = self.id

        short_name = self.short_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if id is not UNSET:
            field_dict["id"] = id
        if short_name is not UNSET:
            field_dict["short_name"] = short_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        full_name = d.pop("full_name", UNSET)

        id = d.pop("id", UNSET)

        short_name = d.pop("short_name", UNSET)

        machine_walkthroughs_language_list_item = cls(
            full_name=full_name,
            id=id,
            short_name=short_name,
        )

        machine_walkthroughs_language_list_item.additional_properties = d
        return machine_walkthroughs_language_list_item

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
