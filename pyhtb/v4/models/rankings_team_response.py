from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rankings_team_item import RankingsTeamItem


T = TypeVar("T", bound="RankingsTeamResponse")


@_attrs_define
class RankingsTeamResponse:
    """Schema definition for Rankings Team Response

    Example:
        {'data': [{'Userbloods': 36, 'avatar_thumb_url':
            'https://www.hackthebox.eu/storage/teams/6a5dfac4be1502501489fc0f5a24b667_thumb.jpg', 'challenge_bloods': 28,
            'challenge_owns': 149, 'country': 'EU', 'fortress': 26, 'id': 1750, 'name': 'TheAteam', 'points': 2436, 'rank':
            1, 'ranks_diff': 0, 'root_bloods': 45, 'root_owns': 187, 'user_owns': 187}, {'Userbloods': 3,
            'avatar_thumb_url': 'https://www.hackthebox.eu/storage/teams/52d080a3e172c33fd6886a37e7288491_thumb.jpg',
            'challenge_bloods': 6, 'challenge_owns': 149, 'country': 'US', 'fortress': 26, 'id': 1709, 'name':
            'BirdsArentReal', 'points': 2190, 'rank': 2, 'ranks_diff': 0, 'root_bloods': 2, 'root_owns': 187, 'user_owns':
            187}], 'status': True}

    Attributes:
        data (list[RankingsTeamItem] | Unset):
        status (bool | Unset):
    """

    data: list[RankingsTeamItem] | Unset = UNSET
    status: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for componentsschemas_rankings_team_items_item_data in self.data:
                componentsschemas_rankings_team_items_item = (
                    componentsschemas_rankings_team_items_item_data.to_dict()
                )
                data.append(componentsschemas_rankings_team_items_item)

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
        from ..models.rankings_team_item import RankingsTeamItem

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[RankingsTeamItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for componentsschemas_rankings_team_items_item_data in _data:
                componentsschemas_rankings_team_items_item = RankingsTeamItem.from_dict(
                    componentsschemas_rankings_team_items_item_data
                )

                data.append(componentsschemas_rankings_team_items_item)

        status = d.pop("status", UNSET)

        rankings_team_response = cls(
            data=data,
            status=status,
        )

        rankings_team_response.additional_properties = d
        return rankings_team_response

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
