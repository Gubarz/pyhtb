from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.machine import Machine


T = TypeVar("T", bound="ProlabIdMachineResponse")


@_attrs_define
class ProlabIdMachineResponse:
    """Schema definition for Prolab Id Machine Response

    Attributes:
        data (list[Machine] | Unset):
        status (bool | Unset):  Example: True.
    """

    data: list[Machine] | Unset = UNSET
    status: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for componentsschemas_prolab_machine_data_item_data in self.data:
                componentsschemas_prolab_machine_data_item = (
                    componentsschemas_prolab_machine_data_item_data.to_dict()
                )
                data.append(componentsschemas_prolab_machine_data_item)

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.machine import Machine

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[Machine] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for componentsschemas_prolab_machine_data_item_data in _data:
                componentsschemas_prolab_machine_data_item = Machine.from_dict(
                    componentsschemas_prolab_machine_data_item_data
                )

                data.append(componentsschemas_prolab_machine_data_item)

        status = d.pop("status", UNSET)

        prolab_id_machine_response = cls(
            data=data,
            status=status,
        )

        prolab_id_machine_response.additional_properties = d
        return prolab_id_machine_response

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
