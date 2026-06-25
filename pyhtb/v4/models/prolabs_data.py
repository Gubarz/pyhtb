from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prolab import Prolab


T = TypeVar("T", bound="ProlabsData")


@_attrs_define
class ProlabsData:
    """Inner container for Prolabs response

    Attributes:
        count (int | Unset):  Example: 6.
        labs (list[Prolab] | Unset):
    """

    count: int | Unset = UNSET
    labs: list[Prolab] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        labs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labs, Unset):
            labs = []
            for componentsschemas_prolab_data_items_item_data in self.labs:
                componentsschemas_prolab_data_items_item = (
                    componentsschemas_prolab_data_items_item_data.to_dict()
                )
                labs.append(componentsschemas_prolab_data_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if labs is not UNSET:
            field_dict["labs"] = labs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prolab import Prolab

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        _labs = d.pop("labs", UNSET)
        labs: list[Prolab] | Unset = UNSET
        if _labs is not UNSET:
            labs = []
            for componentsschemas_prolab_data_items_item_data in _labs:
                componentsschemas_prolab_data_items_item = Prolab.from_dict(
                    componentsschemas_prolab_data_items_item_data
                )

                labs.append(componentsschemas_prolab_data_items_item)

        prolabs_data = cls(
            count=count,
            labs=labs,
        )

        prolabs_data.additional_properties = d
        return prolabs_data

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
