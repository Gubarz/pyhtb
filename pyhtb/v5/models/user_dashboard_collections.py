from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_dashboard_challenge import UserDashboardChallenge
    from ..models.user_dashboard_fortress import UserDashboardFortress
    from ..models.user_dashboard_machine import UserDashboardMachine
    from ..models.user_dashboard_prolab import UserDashboardProlab
    from ..models.user_dashboard_sherlock import UserDashboardSherlock
    from ..models.user_dashboard_starting_point import UserDashboardStartingPoint
    from ..models.user_dashboard_track import UserDashboardTrack


T = TypeVar("T", bound="UserDashboardCollections")


@_attrs_define
class UserDashboardCollections:
    """Collections returned by dashboard endpoints such as favorites, in progress, and recommended.

    Attributes:
        machines (list[UserDashboardMachine]): Machines relevant to the dashboard section.
        starting_points (list[UserDashboardStartingPoint]): Starting Point tiers associated with the user.
        challenges (list[UserDashboardChallenge]): Challenge cards curated for the user.
        sherlocks (list[UserDashboardSherlock]): Sherlock investigations that match the dashboard filter.
        pro_labs (list[UserDashboardProlab]): Pro Lab recommendations or progress items.
        tracks (list[UserDashboardTrack]): Tracks highlighted for the user.
        fortresses (list[UserDashboardFortress]): Fortresses relevant to the dashboard view.
    """

    machines: list[UserDashboardMachine]
    starting_points: list[UserDashboardStartingPoint]
    challenges: list[UserDashboardChallenge]
    sherlocks: list[UserDashboardSherlock]
    pro_labs: list[UserDashboardProlab]
    tracks: list[UserDashboardTrack]
    fortresses: list[UserDashboardFortress]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        machines = []
        for machines_item_data in self.machines:
            machines_item = machines_item_data.to_dict()
            machines.append(machines_item)

        starting_points = []
        for starting_points_item_data in self.starting_points:
            starting_points_item = starting_points_item_data.to_dict()
            starting_points.append(starting_points_item)

        challenges = []
        for challenges_item_data in self.challenges:
            challenges_item = challenges_item_data.to_dict()
            challenges.append(challenges_item)

        sherlocks = []
        for sherlocks_item_data in self.sherlocks:
            sherlocks_item = sherlocks_item_data.to_dict()
            sherlocks.append(sherlocks_item)

        pro_labs = []
        for pro_labs_item_data in self.pro_labs:
            pro_labs_item = pro_labs_item_data.to_dict()
            pro_labs.append(pro_labs_item)

        tracks = []
        for tracks_item_data in self.tracks:
            tracks_item = tracks_item_data.to_dict()
            tracks.append(tracks_item)

        fortresses = []
        for fortresses_item_data in self.fortresses:
            fortresses_item = fortresses_item_data.to_dict()
            fortresses.append(fortresses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "machines": machines,
                "startingPoints": starting_points,
                "challenges": challenges,
                "sherlocks": sherlocks,
                "proLabs": pro_labs,
                "tracks": tracks,
                "fortresses": fortresses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_dashboard_challenge import UserDashboardChallenge
        from ..models.user_dashboard_fortress import UserDashboardFortress
        from ..models.user_dashboard_machine import UserDashboardMachine
        from ..models.user_dashboard_prolab import UserDashboardProlab
        from ..models.user_dashboard_sherlock import UserDashboardSherlock
        from ..models.user_dashboard_starting_point import UserDashboardStartingPoint
        from ..models.user_dashboard_track import UserDashboardTrack

        d = dict(src_dict)
        machines = []
        _machines = d.pop("machines")
        for machines_item_data in _machines:
            machines_item = UserDashboardMachine.from_dict(machines_item_data)

            machines.append(machines_item)

        starting_points = []
        _starting_points = d.pop("startingPoints")
        for starting_points_item_data in _starting_points:
            starting_points_item = UserDashboardStartingPoint.from_dict(
                starting_points_item_data
            )

            starting_points.append(starting_points_item)

        challenges = []
        _challenges = d.pop("challenges")
        for challenges_item_data in _challenges:
            challenges_item = UserDashboardChallenge.from_dict(challenges_item_data)

            challenges.append(challenges_item)

        sherlocks = []
        _sherlocks = d.pop("sherlocks")
        for sherlocks_item_data in _sherlocks:
            sherlocks_item = UserDashboardSherlock.from_dict(sherlocks_item_data)

            sherlocks.append(sherlocks_item)

        pro_labs = []
        _pro_labs = d.pop("proLabs")
        for pro_labs_item_data in _pro_labs:
            pro_labs_item = UserDashboardProlab.from_dict(pro_labs_item_data)

            pro_labs.append(pro_labs_item)

        tracks = []
        _tracks = d.pop("tracks")
        for tracks_item_data in _tracks:
            tracks_item = UserDashboardTrack.from_dict(tracks_item_data)

            tracks.append(tracks_item)

        fortresses = []
        _fortresses = d.pop("fortresses")
        for fortresses_item_data in _fortresses:
            fortresses_item = UserDashboardFortress.from_dict(fortresses_item_data)

            fortresses.append(fortresses_item)

        user_dashboard_collections = cls(
            machines=machines,
            starting_points=starting_points,
            challenges=challenges,
            sherlocks=sherlocks,
            pro_labs=pro_labs,
            tracks=tracks,
            fortresses=fortresses,
        )

        user_dashboard_collections.additional_properties = d
        return user_dashboard_collections

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
