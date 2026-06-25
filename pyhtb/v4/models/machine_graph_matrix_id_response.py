from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.machine_graph_matrix_info import MachineGraphMatrixInfo


T = TypeVar("T", bound="MachineGraphMatrixIdResponse")


@_attrs_define
class MachineGraphMatrixIdResponse:
    """Schema definition for Machine Graph Matrix Id Response

    Attributes:
        info (MachineGraphMatrixInfo | Unset):
    """

    info: MachineGraphMatrixInfo | Unset = UNSET
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
        from ..models.machine_graph_matrix_info import MachineGraphMatrixInfo

        d = dict(src_dict)
        _info = d.pop("info", UNSET)
        info: MachineGraphMatrixInfo | Unset
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = MachineGraphMatrixInfo.from_dict(_info)

        machine_graph_matrix_id_response = cls(
            info=info,
        )

        machine_graph_matrix_id_response.additional_properties = d
        return machine_graph_matrix_id_response

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
