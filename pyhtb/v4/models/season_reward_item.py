from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeasonRewardItem")


@_attrs_define
class SeasonRewardItem:
    """
    Attributes:
        id (int | Unset):
        image (str | Unset):
        name (str | Unset):
        order (float | Unset):
        reward_group_id (int | Unset):
    """

    id: int | Unset = UNSET
    image: str | Unset = UNSET
    name: str | Unset = UNSET
    order: float | Unset = UNSET
    reward_group_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        image = self.image

        name = self.name

        order = self.order

        reward_group_id = self.reward_group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if reward_group_id is not UNSET:
            field_dict["reward_group_id"] = reward_group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        image = d.pop("image", UNSET)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        reward_group_id = d.pop("reward_group_id", UNSET)

        season_reward_item = cls(
            id=id,
            image=image,
            name=name,
            order=order,
            reward_group_id=reward_group_id,
        )

        season_reward_item.additional_properties = d
        return season_reward_item

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
