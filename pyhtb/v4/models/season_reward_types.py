from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_reward_group_item import SeasonRewardGroupItem


T = TypeVar("T", bound="SeasonRewardTypes")


@_attrs_define
class SeasonRewardTypes:
    """
    Attributes:
        description (str | Unset):
        groups (list[SeasonRewardGroupItem] | Unset):
        id (int | Unset):
        name (str | Unset):
        order (float | Unset):
    """

    description: str | Unset = UNSET
    groups: list[SeasonRewardGroupItem] | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    order: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for componentsschemas_group_items_item_data in self.groups:
                componentsschemas_group_items_item = (
                    componentsschemas_group_items_item_data.to_dict()
                )
                groups.append(componentsschemas_group_items_item)

        id = self.id

        name = self.name

        order = self.order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if groups is not UNSET:
            field_dict["groups"] = groups
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.season_reward_group_item import SeasonRewardGroupItem

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _groups = d.pop("groups", UNSET)
        groups: list[SeasonRewardGroupItem] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for componentsschemas_group_items_item_data in _groups:
                componentsschemas_group_items_item = SeasonRewardGroupItem.from_dict(
                    componentsschemas_group_items_item_data
                )

                groups.append(componentsschemas_group_items_item)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        season_reward_types = cls(
            description=description,
            groups=groups,
            id=id,
            name=name,
            order=order,
        )

        season_reward_types.additional_properties = d
        return season_reward_types

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
