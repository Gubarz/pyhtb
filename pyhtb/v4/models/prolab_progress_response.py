from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prolab_progress_data import ProlabProgressData


T = TypeVar("T", bound="ProlabProgressResponse")


@_attrs_define
class ProlabProgressResponse:
    """
    Attributes:
        data (ProlabProgressData | Unset):
        status (bool | Unset):
    """

    data: ProlabProgressData | Unset = UNSET
    status: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

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
        from ..models.prolab_progress_data import ProlabProgressData

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: ProlabProgressData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ProlabProgressData.from_dict(_data)

        status = d.pop("status", UNSET)

        prolab_progress_response = cls(
            data=data,
            status=status,
        )

        prolab_progress_response.additional_properties = d
        return prolab_progress_response

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
