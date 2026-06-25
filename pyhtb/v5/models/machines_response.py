from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.links import Links
    from ..models.machines_item import MachinesItem
    from ..models.meta import Meta


T = TypeVar("T", bound="MachinesResponse")


@_attrs_define
class MachinesResponse:
    """Schema definition for Machines list responses

    Attributes:
        data (list[MachinesItem]):
        links (Links): Schema definition for Links
        meta (Meta): Schema definition for Meta
    """

    data: list[MachinesItem]
    links: Links
    meta: Meta
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for componentsschemas_machines_data_item_data in self.data:
            componentsschemas_machines_data_item = (
                componentsschemas_machines_data_item_data.to_dict()
            )
            data.append(componentsschemas_machines_data_item)

        links = self.links.to_dict()

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "links": links,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links import Links
        from ..models.machines_item import MachinesItem
        from ..models.meta import Meta

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for componentsschemas_machines_data_item_data in _data:
            componentsschemas_machines_data_item = MachinesItem.from_dict(
                componentsschemas_machines_data_item_data
            )

            data.append(componentsschemas_machines_data_item)

        links = Links.from_dict(d.pop("links"))

        meta = Meta.from_dict(d.pop("meta"))

        machines_response = cls(
            data=data,
            links=links,
            meta=meta,
        )

        machines_response.additional_properties = d
        return machines_response

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
