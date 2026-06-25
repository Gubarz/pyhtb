from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.machine_walkthroughs_language_list_item import (
        MachineWalkthroughsLanguageListItem,
    )


T = TypeVar("T", bound="MachineWalkthroughsLanguageListResponse")


@_attrs_define
class MachineWalkthroughsLanguageListResponse:
    """Schema definition for Machine Walkthroughs Language List Response

    Attributes:
        info (list[MachineWalkthroughsLanguageListItem] | Unset):
    """

    info: list[MachineWalkthroughsLanguageListItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.info, Unset):
            info = []
            for (
                componentsschemas_machine_walkthroughs_language_list_items_item_data
            ) in self.info:
                componentsschemas_machine_walkthroughs_language_list_items_item = componentsschemas_machine_walkthroughs_language_list_items_item_data.to_dict()
                info.append(
                    componentsschemas_machine_walkthroughs_language_list_items_item
                )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.machine_walkthroughs_language_list_item import (
            MachineWalkthroughsLanguageListItem,
        )

        d = dict(src_dict)
        _info = d.pop("info", UNSET)
        info: list[MachineWalkthroughsLanguageListItem] | Unset = UNSET
        if _info is not UNSET:
            info = []
            for (
                componentsschemas_machine_walkthroughs_language_list_items_item_data
            ) in _info:
                componentsschemas_machine_walkthroughs_language_list_items_item = MachineWalkthroughsLanguageListItem.from_dict(
                    componentsschemas_machine_walkthroughs_language_list_items_item_data
                )

                info.append(
                    componentsschemas_machine_walkthroughs_language_list_items_item
                )

        machine_walkthroughs_language_list_response = cls(
            info=info,
        )

        machine_walkthroughs_language_list_response.additional_properties = d
        return machine_walkthroughs_language_list_response

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
