from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ranking_data_team_properties import RankingDataTeamProperties
    from ..models.ranking_data_user_properties import RankingDataUserProperties


T = TypeVar("T", bound="RankingsData")


@_attrs_define
class RankingsData:
    """
    Attributes:
        team (RankingDataTeamProperties | Unset):
        user (RankingDataUserProperties | Unset):
    """

    team: RankingDataTeamProperties | Unset = UNSET
    user: RankingDataUserProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team: dict[str, Any] | Unset = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team is not UNSET:
            field_dict["team"] = team
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ranking_data_team_properties import RankingDataTeamProperties
        from ..models.ranking_data_user_properties import RankingDataUserProperties

        d = dict(src_dict)
        _team = d.pop("team", UNSET)
        team: RankingDataTeamProperties | Unset
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = RankingDataTeamProperties.from_dict(_team)

        _user = d.pop("user", UNSET)
        user: RankingDataUserProperties | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RankingDataUserProperties.from_dict(_user)

        rankings_data = cls(
            team=team,
            user=user,
        )

        rankings_data.additional_properties = d
        return rankings_data

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
