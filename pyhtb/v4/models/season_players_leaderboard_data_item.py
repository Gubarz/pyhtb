from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeasonPlayersLeaderboardDataItem")


@_attrs_define
class SeasonPlayersLeaderboardDataItem:
    """
    Attributes:
        account_id (str | Unset):
        avatar_thumb (None | str | Unset):
        country (None | str | Unset):
        country_name (None | str | Unset):
        last_own (str | Unset):
        league_rank (str | Unset):
        name (str | Unset):
        points (int | Unset):
        positive_trend (bool | Unset):
        rank (int | Unset):
        rank_trend (float | Unset):
        resource_id (int | Unset):
        root_bloods (int | Unset):
        root_owns (int | Unset):
        user_bloods (int | Unset):
        user_owns (int | Unset):
    """

    account_id: str | Unset = UNSET
    avatar_thumb: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    country_name: None | str | Unset = UNSET
    last_own: str | Unset = UNSET
    league_rank: str | Unset = UNSET
    name: str | Unset = UNSET
    points: int | Unset = UNSET
    positive_trend: bool | Unset = UNSET
    rank: int | Unset = UNSET
    rank_trend: float | Unset = UNSET
    resource_id: int | Unset = UNSET
    root_bloods: int | Unset = UNSET
    root_owns: int | Unset = UNSET
    user_bloods: int | Unset = UNSET
    user_owns: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        avatar_thumb: None | str | Unset
        if isinstance(self.avatar_thumb, Unset):
            avatar_thumb = UNSET
        else:
            avatar_thumb = self.avatar_thumb

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        country_name: None | str | Unset
        if isinstance(self.country_name, Unset):
            country_name = UNSET
        else:
            country_name = self.country_name

        last_own = self.last_own

        league_rank = self.league_rank

        name = self.name

        points = self.points

        positive_trend = self.positive_trend

        rank = self.rank

        rank_trend = self.rank_trend

        resource_id = self.resource_id

        root_bloods = self.root_bloods

        root_owns = self.root_owns

        user_bloods = self.user_bloods

        user_owns = self.user_owns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if avatar_thumb is not UNSET:
            field_dict["avatar_thumb"] = avatar_thumb
        if country is not UNSET:
            field_dict["country"] = country
        if country_name is not UNSET:
            field_dict["country_name"] = country_name
        if last_own is not UNSET:
            field_dict["last_own"] = last_own
        if league_rank is not UNSET:
            field_dict["league_rank"] = league_rank
        if name is not UNSET:
            field_dict["name"] = name
        if points is not UNSET:
            field_dict["points"] = points
        if positive_trend is not UNSET:
            field_dict["positive_trend"] = positive_trend
        if rank is not UNSET:
            field_dict["rank"] = rank
        if rank_trend is not UNSET:
            field_dict["rank_trend"] = rank_trend
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if root_bloods is not UNSET:
            field_dict["root_bloods"] = root_bloods
        if root_owns is not UNSET:
            field_dict["root_owns"] = root_owns
        if user_bloods is not UNSET:
            field_dict["user_bloods"] = user_bloods
        if user_owns is not UNSET:
            field_dict["user_owns"] = user_owns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        def _parse_avatar_thumb(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_thumb = _parse_avatar_thumb(d.pop("avatar_thumb", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_country_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_name = _parse_country_name(d.pop("country_name", UNSET))

        last_own = d.pop("last_own", UNSET)

        league_rank = d.pop("league_rank", UNSET)

        name = d.pop("name", UNSET)

        points = d.pop("points", UNSET)

        positive_trend = d.pop("positive_trend", UNSET)

        rank = d.pop("rank", UNSET)

        rank_trend = d.pop("rank_trend", UNSET)

        resource_id = d.pop("resource_id", UNSET)

        root_bloods = d.pop("root_bloods", UNSET)

        root_owns = d.pop("root_owns", UNSET)

        user_bloods = d.pop("user_bloods", UNSET)

        user_owns = d.pop("user_owns", UNSET)

        season_players_leaderboard_data_item = cls(
            account_id=account_id,
            avatar_thumb=avatar_thumb,
            country=country,
            country_name=country_name,
            last_own=last_own,
            league_rank=league_rank,
            name=name,
            points=points,
            positive_trend=positive_trend,
            rank=rank,
            rank_trend=rank_trend,
            resource_id=resource_id,
            root_bloods=root_bloods,
            root_owns=root_owns,
            user_bloods=user_bloods,
            user_owns=user_owns,
        )

        season_players_leaderboard_data_item.additional_properties = d
        return season_players_leaderboard_data_item

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
