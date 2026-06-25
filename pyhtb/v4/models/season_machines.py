from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_machines_data_item import SeasonMachinesDataItem


T = TypeVar("T", bound="SeasonMachines")


@_attrs_define
class SeasonMachines:
    """Schema definition for Season Machines

    Attributes:
        data (list[SeasonMachinesDataItem] | Unset):
    """

    data: list[SeasonMachinesDataItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for componentsschemas_season_machines_data_items_item_data in self.data:
                componentsschemas_season_machines_data_items_item = (
                    componentsschemas_season_machines_data_items_item_data.to_dict()
                )
                data.append(componentsschemas_season_machines_data_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.season_machines_data_item import SeasonMachinesDataItem

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[SeasonMachinesDataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for componentsschemas_season_machines_data_items_item_data in _data:
                componentsschemas_season_machines_data_items_item = (
                    SeasonMachinesDataItem.from_dict(
                        componentsschemas_season_machines_data_items_item_data
                    )
                )

                data.append(componentsschemas_season_machines_data_items_item)

        season_machines = cls(
            data=data,
        )

        season_machines.additional_properties = d
        return season_machines

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
