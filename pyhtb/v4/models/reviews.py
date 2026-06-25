from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links import Links
    from ..models.meta import Meta
    from ..models.review_message_item import ReviewMessageItem


T = TypeVar("T", bound="Reviews")


@_attrs_define
class Reviews:
    """Schema definition for Reviews Response

    Attributes:
        average (float | Unset):  Example: 3.3.
        count (int | Unset):  Example: 118.
        data (list[ReviewMessageItem] | Unset): Schema definition for Review Message
        links (Links | Unset): Schema definition for Links
        meta (Meta | Unset): Schema definition for Meta
    """

    average: float | Unset = UNSET
    count: int | Unset = UNSET
    data: list[ReviewMessageItem] | Unset = UNSET
    links: Links | Unset = UNSET
    meta: Meta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        average = self.average

        count = self.count

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for componentsschemas_review_message_item_data in self.data:
                componentsschemas_review_message_item = (
                    componentsschemas_review_message_item_data.to_dict()
                )
                data.append(componentsschemas_review_message_item)

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if average is not UNSET:
            field_dict["average"] = average
        if count is not UNSET:
            field_dict["count"] = count
        if data is not UNSET:
            field_dict["data"] = data
        if links is not UNSET:
            field_dict["links"] = links
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.links import Links
        from ..models.meta import Meta
        from ..models.review_message_item import ReviewMessageItem

        d = dict(src_dict)
        average = d.pop("average", UNSET)

        count = d.pop("count", UNSET)

        _data = d.pop("data", UNSET)
        data: list[ReviewMessageItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for componentsschemas_review_message_item_data in _data:
                componentsschemas_review_message_item = ReviewMessageItem.from_dict(
                    componentsschemas_review_message_item_data
                )

                data.append(componentsschemas_review_message_item)

        _links = d.pop("links", UNSET)
        links: Links | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        _meta = d.pop("meta", UNSET)
        meta: Meta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = Meta.from_dict(_meta)

        reviews = cls(
            average=average,
            count=count,
            data=data,
            links=links,
            meta=meta,
        )

        reviews.additional_properties = d
        return reviews

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
