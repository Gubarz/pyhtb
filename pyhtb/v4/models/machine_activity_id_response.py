from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.machine_activity_info import MachineActivityInfo


T = TypeVar("T", bound="MachineActivityIdResponse")


@_attrs_define
class MachineActivityIdResponse:
    """Schema definition for Machine Activity Id Response

    Attributes:
        info (MachineActivityInfo | Unset):
    """

    info: MachineActivityInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.machine_activity_info import MachineActivityInfo

        d = dict(src_dict)
        _info = d.pop("info", UNSET)
        info: MachineActivityInfo | Unset
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = MachineActivityInfo.from_dict(_info)

        machine_activity_id_response = cls(
            info=info,
        )

        machine_activity_id_response.additional_properties = d
        return machine_activity_id_response

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
