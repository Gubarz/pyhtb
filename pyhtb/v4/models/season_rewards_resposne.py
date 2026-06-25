from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_rewards_data_item import SeasonRewardsDataItem


T = TypeVar("T", bound="SeasonRewardsResposne")


@_attrs_define
class SeasonRewardsResposne:
    """
    Attributes:
        data (list[SeasonRewardsDataItem] | Unset):
    """

    data: list[SeasonRewardsDataItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for componentsschemas_season_rewards_data_item_data in self.data:
                componentsschemas_season_rewards_data_item = (
                    componentsschemas_season_rewards_data_item_data.to_dict()
                )
                data.append(componentsschemas_season_rewards_data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.season_rewards_data_item import SeasonRewardsDataItem

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[SeasonRewardsDataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for componentsschemas_season_rewards_data_item_data in _data:
                componentsschemas_season_rewards_data_item = (
                    SeasonRewardsDataItem.from_dict(
                        componentsschemas_season_rewards_data_item_data
                    )
                )

                data.append(componentsschemas_season_rewards_data_item)

        season_rewards_resposne = cls(
            data=data,
        )

        season_rewards_resposne.additional_properties = d
        return season_rewards_resposne

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
