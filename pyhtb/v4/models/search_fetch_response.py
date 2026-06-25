from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_challenge_item import SearchChallengeItem
    from ..models.search_fetch_machines_item import SearchFetchMachinesItem
    from ..models.search_sherlock_item import SearchSherlockItem
    from ..models.search_team_item import SearchTeamItem
    from ..models.search_user_item import SearchUserItem


T = TypeVar("T", bound="SearchFetchResponse")


@_attrs_define
class SearchFetchResponse:
    """Schema definition for Search Fetch Response

    Attributes:
        challenges (list[SearchChallengeItem] | Unset):
        machines (list[SearchFetchMachinesItem] | Unset):
        teams (list[SearchTeamItem] | Unset):
        users (list[SearchUserItem] | Unset):
        sherlocks (list[SearchSherlockItem] | Unset):
    """

    challenges: list[SearchChallengeItem] | Unset = UNSET
    machines: list[SearchFetchMachinesItem] | Unset = UNSET
    teams: list[SearchTeamItem] | Unset = UNSET
    users: list[SearchUserItem] | Unset = UNSET
    sherlocks: list[SearchSherlockItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.challenges, Unset):
            challenges = []
            for componentsschemas_search_challenges_items_item_data in self.challenges:
                componentsschemas_search_challenges_items_item = (
                    componentsschemas_search_challenges_items_item_data.to_dict()
                )
                challenges.append(componentsschemas_search_challenges_items_item)

        machines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.machines, Unset):
            machines = []
            for componentsschemas_search_machines_items_item_data in self.machines:
                componentsschemas_search_machines_items_item = (
                    componentsschemas_search_machines_items_item_data.to_dict()
                )
                machines.append(componentsschemas_search_machines_items_item)

        teams: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for componentsschemas_search_team_items_item_data in self.teams:
                componentsschemas_search_team_items_item = (
                    componentsschemas_search_team_items_item_data.to_dict()
                )
                teams.append(componentsschemas_search_team_items_item)

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for componentsschemas_search_users_items_item_data in self.users:
                componentsschemas_search_users_items_item = (
                    componentsschemas_search_users_items_item_data.to_dict()
                )
                users.append(componentsschemas_search_users_items_item)

        sherlocks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sherlocks, Unset):
            sherlocks = []
            for componentsschemas_search_sherlocks_items_item_data in self.sherlocks:
                componentsschemas_search_sherlocks_items_item = (
                    componentsschemas_search_sherlocks_items_item_data.to_dict()
                )
                sherlocks.append(componentsschemas_search_sherlocks_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if challenges is not UNSET:
            field_dict["challenges"] = challenges
        if machines is not UNSET:
            field_dict["machines"] = machines
        if teams is not UNSET:
            field_dict["teams"] = teams
        if users is not UNSET:
            field_dict["users"] = users
        if sherlocks is not UNSET:
            field_dict["sherlocks"] = sherlocks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_challenge_item import SearchChallengeItem
        from ..models.search_fetch_machines_item import SearchFetchMachinesItem
        from ..models.search_sherlock_item import SearchSherlockItem
        from ..models.search_team_item import SearchTeamItem
        from ..models.search_user_item import SearchUserItem

        d = dict(src_dict)
        _challenges = d.pop("challenges", UNSET)
        challenges: list[SearchChallengeItem] | Unset = UNSET
        if _challenges is not UNSET:
            challenges = []
            for componentsschemas_search_challenges_items_item_data in _challenges:
                componentsschemas_search_challenges_items_item = (
                    SearchChallengeItem.from_dict(
                        componentsschemas_search_challenges_items_item_data
                    )
                )

                challenges.append(componentsschemas_search_challenges_items_item)

        _machines = d.pop("machines", UNSET)
        machines: list[SearchFetchMachinesItem] | Unset = UNSET
        if _machines is not UNSET:
            machines = []
            for componentsschemas_search_machines_items_item_data in _machines:
                componentsschemas_search_machines_items_item = (
                    SearchFetchMachinesItem.from_dict(
                        componentsschemas_search_machines_items_item_data
                    )
                )

                machines.append(componentsschemas_search_machines_items_item)

        _teams = d.pop("teams", UNSET)
        teams: list[SearchTeamItem] | Unset = UNSET
        if _teams is not UNSET:
            teams = []
            for componentsschemas_search_team_items_item_data in _teams:
                componentsschemas_search_team_items_item = SearchTeamItem.from_dict(
                    componentsschemas_search_team_items_item_data
                )

                teams.append(componentsschemas_search_team_items_item)

        _users = d.pop("users", UNSET)
        users: list[SearchUserItem] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for componentsschemas_search_users_items_item_data in _users:
                componentsschemas_search_users_items_item = SearchUserItem.from_dict(
                    componentsschemas_search_users_items_item_data
                )

                users.append(componentsschemas_search_users_items_item)

        _sherlocks = d.pop("sherlocks", UNSET)
        sherlocks: list[SearchSherlockItem] | Unset = UNSET
        if _sherlocks is not UNSET:
            sherlocks = []
            for componentsschemas_search_sherlocks_items_item_data in _sherlocks:
                componentsschemas_search_sherlocks_items_item = (
                    SearchSherlockItem.from_dict(
                        componentsschemas_search_sherlocks_items_item_data
                    )
                )

                sherlocks.append(componentsschemas_search_sherlocks_items_item)

        search_fetch_response = cls(
            challenges=challenges,
            machines=machines,
            teams=teams,
            users=users,
            sherlocks=sherlocks,
        )

        search_fetch_response.additional_properties = d
        return search_fetch_response

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
