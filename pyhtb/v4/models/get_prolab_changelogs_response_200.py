from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_prolab_changelogs_response_200_data_item import (
        GetProlabChangelogsResponse200DataItem,
    )


T = TypeVar("T", bound="GetProlabChangelogsResponse200")


@_attrs_define
class GetProlabChangelogsResponse200:
    """
    Attributes:
        data (list[GetProlabChangelogsResponse200DataItem] | Unset):
        status (bool | Unset):
    """

    data: list[GetProlabChangelogsResponse200DataItem] | Unset = UNSET
    status: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

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
        from ..models.get_prolab_changelogs_response_200_data_item import (
            GetProlabChangelogsResponse200DataItem,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[GetProlabChangelogsResponse200DataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = GetProlabChangelogsResponse200DataItem.from_dict(
                    data_item_data
                )

                data.append(data_item)

        status = d.pop("status", UNSET)

        get_prolab_changelogs_response_200 = cls(
            data=data,
            status=status,
        )

        get_prolab_changelogs_response_200.additional_properties = d
        return get_prolab_changelogs_response_200

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
