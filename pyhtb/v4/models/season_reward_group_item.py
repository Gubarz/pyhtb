from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_reward_item import SeasonRewardItem


T = TypeVar("T", bound="SeasonRewardGroupItem")


@_attrs_define
class SeasonRewardGroupItem:
    """
    Attributes:
        description (None | str | Unset):
        id (int | Unset):
        image (None | str | Unset):
        name (str | Unset):
        order (int | Unset):
        reward_type_id (int | Unset):
        rewards (list[SeasonRewardItem] | Unset):
        subtitle (None | str | Unset):
        rank_up_requirement (str | Unset):
        flags_needed (int | Unset):
    """

    description: None | str | Unset = UNSET
    id: int | Unset = UNSET
    image: None | str | Unset = UNSET
    name: str | Unset = UNSET
    order: int | Unset = UNSET
    reward_type_id: int | Unset = UNSET
    rewards: list[SeasonRewardItem] | Unset = UNSET
    subtitle: None | str | Unset = UNSET
    rank_up_requirement: str | Unset = UNSET
    flags_needed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id = self.id

        image: None | str | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        name = self.name

        order = self.order

        reward_type_id = self.reward_type_id

        rewards: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rewards, Unset):
            rewards = []
            for componentsschemas_season_rewards_items_item_data in self.rewards:
                componentsschemas_season_rewards_items_item = (
                    componentsschemas_season_rewards_items_item_data.to_dict()
                )
                rewards.append(componentsschemas_season_rewards_items_item)

        subtitle: None | str | Unset
        if isinstance(self.subtitle, Unset):
            subtitle = UNSET
        else:
            subtitle = self.subtitle

        rank_up_requirement = self.rank_up_requirement

        flags_needed = self.flags_needed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if reward_type_id is not UNSET:
            field_dict["reward_type_id"] = reward_type_id
        if rewards is not UNSET:
            field_dict["rewards"] = rewards
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if rank_up_requirement is not UNSET:
            field_dict["rank_up_requirement"] = rank_up_requirement
        if flags_needed is not UNSET:
            field_dict["flags_needed"] = flags_needed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.season_reward_item import SeasonRewardItem

        d = dict(src_dict)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        id = d.pop("id", UNSET)

        def _parse_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image = _parse_image(d.pop("image", UNSET))

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        reward_type_id = d.pop("reward_type_id", UNSET)

        _rewards = d.pop("rewards", UNSET)
        rewards: list[SeasonRewardItem] | Unset = UNSET
        if _rewards is not UNSET:
            rewards = []
            for componentsschemas_season_rewards_items_item_data in _rewards:
                componentsschemas_season_rewards_items_item = (
                    SeasonRewardItem.from_dict(
                        componentsschemas_season_rewards_items_item_data
                    )
                )

                rewards.append(componentsschemas_season_rewards_items_item)

        def _parse_subtitle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subtitle = _parse_subtitle(d.pop("subtitle", UNSET))

        rank_up_requirement = d.pop("rank_up_requirement", UNSET)

        flags_needed = d.pop("flags_needed", UNSET)

        season_reward_group_item = cls(
            description=description,
            id=id,
            image=image,
            name=name,
            order=order,
            reward_type_id=reward_type_id,
            rewards=rewards,
            subtitle=subtitle,
            rank_up_requirement=rank_up_requirement,
            flags_needed=flags_needed,
        )

        season_reward_group_item.additional_properties = d
        return season_reward_group_item

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
