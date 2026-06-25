from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination_link import PaginationLink


T = TypeVar("T", bound="Meta")


@_attrs_define
class Meta:
    """Schema definition for Meta

    Attributes:
        current_page (int | Unset):  Example: 1.
        from_ (int | Unset):  Example: 1.
        last_page (int | Unset):  Example: 11.
        links (list[PaginationLink] | Unset):
        path (str | Unset):  Example: https://labs.hackthebox.com/api/v4/prolab/1/reviews.
        per_page (int | Unset):  Example: 15.
        to (int | Unset):  Example: 15.
        total (int | Unset):  Example: 162.
    """

    current_page: int | Unset = UNSET
    from_: int | Unset = UNSET
    last_page: int | Unset = UNSET
    links: list[PaginationLink] | Unset = UNSET
    path: str | Unset = UNSET
    per_page: int | Unset = UNSET
    to: int | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        from_ = self.from_

        last_page = self.last_page

        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for componentsschemas_pagination_links_item_data in self.links:
                componentsschemas_pagination_links_item = (
                    componentsschemas_pagination_links_item_data.to_dict()
                )
                links.append(componentsschemas_pagination_links_item)

        path = self.path

        per_page = self.per_page

        to = self.to

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_page is not UNSET:
            field_dict["current_page"] = current_page
        if from_ is not UNSET:
            field_dict["from"] = from_
        if last_page is not UNSET:
            field_dict["last_page"] = last_page
        if links is not UNSET:
            field_dict["links"] = links
        if path is not UNSET:
            field_dict["path"] = path
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if to is not UNSET:
            field_dict["to"] = to
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination_link import PaginationLink

        d = dict(src_dict)
        current_page = d.pop("current_page", UNSET)

        from_ = d.pop("from", UNSET)

        last_page = d.pop("last_page", UNSET)

        _links = d.pop("links", UNSET)
        links: list[PaginationLink] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for componentsschemas_pagination_links_item_data in _links:
                componentsschemas_pagination_links_item = PaginationLink.from_dict(
                    componentsschemas_pagination_links_item_data
                )

                links.append(componentsschemas_pagination_links_item)

        path = d.pop("path", UNSET)

        per_page = d.pop("per_page", UNSET)

        to = d.pop("to", UNSET)

        total = d.pop("total", UNSET)

        meta = cls(
            current_page=current_page,
            from_=from_,
            last_page=last_page,
            links=links,
            path=path,
            per_page=per_page,
            to=to,
            total=total,
        )

        meta.additional_properties = d
        return meta

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
