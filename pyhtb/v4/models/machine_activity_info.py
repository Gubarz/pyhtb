from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.machine_acitivty_item import MachineAcitivtyItem


T = TypeVar("T", bound="MachineActivityInfo")


@_attrs_define
class MachineActivityInfo:
    """
    Attributes:
        activity (list[MachineAcitivtyItem] | Unset):
        server (str | Unset):
    """

    activity: list[MachineAcitivtyItem] | Unset = UNSET
    server: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.activity, Unset):
            activity = []
            for componentsschemas_machine_activity_items_item_data in self.activity:
                componentsschemas_machine_activity_items_item = (
                    componentsschemas_machine_activity_items_item_data.to_dict()
                )
                activity.append(componentsschemas_machine_activity_items_item)

        server = self.server

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity is not UNSET:
            field_dict["activity"] = activity
        if server is not UNSET:
            field_dict["server"] = server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.machine_acitivty_item import MachineAcitivtyItem

        d = dict(src_dict)
        _activity = d.pop("activity", UNSET)
        activity: list[MachineAcitivtyItem] | Unset = UNSET
        if _activity is not UNSET:
            activity = []
            for componentsschemas_machine_activity_items_item_data in _activity:
                componentsschemas_machine_activity_items_item = (
                    MachineAcitivtyItem.from_dict(
                        componentsschemas_machine_activity_items_item_data
                    )
                )

                activity.append(componentsschemas_machine_activity_items_item)

        server = d.pop("server", UNSET)

        machine_activity_info = cls(
            activity=activity,
            server=server,
        )

        machine_activity_info.additional_properties = d
        return machine_activity_info

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
