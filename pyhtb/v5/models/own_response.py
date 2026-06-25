from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.own_response_own_type import OwnResponseOwnType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rank_update import RankUpdate


T = TypeVar("T", bound="OwnResponse")


@_attrs_define
class OwnResponse:
    """Schema definition for Machine Own Response

    Attributes:
        blood_points (int):
        blood_taken (int):
        id (int):  Example: 665.
        is_starting_point (bool):
        machine_completed (bool):
        machine_pwned (bool):
        machine_state (str):  Example: open.
        message (str):  Example: You pwned the User Flag!.
        own_type (OwnResponseOwnType):  Example: User.
        points (int):  Example: 50.
        status (int):  Example: 200.
        success (bool):  Example: True.
        league_rank (RankUpdate | Unset):
        user_rank (RankUpdate | Unset):
    """

    blood_points: int
    blood_taken: int
    id: int
    is_starting_point: bool
    machine_completed: bool
    machine_pwned: bool
    machine_state: str
    message: str
    own_type: OwnResponseOwnType
    points: int
    status: int
    success: bool
    league_rank: RankUpdate | Unset = UNSET
    user_rank: RankUpdate | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blood_points = self.blood_points

        blood_taken = self.blood_taken

        id = self.id

        is_starting_point = self.is_starting_point

        machine_completed = self.machine_completed

        machine_pwned = self.machine_pwned

        machine_state = self.machine_state

        message = self.message

        own_type = self.own_type.value

        points = self.points

        status = self.status

        success = self.success

        league_rank: dict[str, Any] | Unset = UNSET
        if not isinstance(self.league_rank, Unset):
            league_rank = self.league_rank.to_dict()

        user_rank: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_rank, Unset):
            user_rank = self.user_rank.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blood_points": blood_points,
                "blood_taken": blood_taken,
                "id": id,
                "is_starting_point": is_starting_point,
                "machine_completed": machine_completed,
                "machine_pwned": machine_pwned,
                "machine_state": machine_state,
                "message": message,
                "own_type": own_type,
                "points": points,
                "status": status,
                "success": success,
            }
        )
        if league_rank is not UNSET:
            field_dict["league_rank"] = league_rank
        if user_rank is not UNSET:
            field_dict["user_rank"] = user_rank

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rank_update import RankUpdate

        d = dict(src_dict)
        blood_points = d.pop("blood_points")

        blood_taken = d.pop("blood_taken")

        id = d.pop("id")

        is_starting_point = d.pop("is_starting_point")

        machine_completed = d.pop("machine_completed")

        machine_pwned = d.pop("machine_pwned")

        machine_state = d.pop("machine_state")

        message = d.pop("message")

        own_type = OwnResponseOwnType(d.pop("own_type"))

        points = d.pop("points")

        status = d.pop("status")

        success = d.pop("success")

        _league_rank = d.pop("league_rank", UNSET)
        league_rank: RankUpdate | Unset
        if isinstance(_league_rank, Unset):
            league_rank = UNSET
        else:
            league_rank = RankUpdate.from_dict(_league_rank)

        _user_rank = d.pop("user_rank", UNSET)
        user_rank: RankUpdate | Unset
        if isinstance(_user_rank, Unset):
            user_rank = UNSET
        else:
            user_rank = RankUpdate.from_dict(_user_rank)

        own_response = cls(
            blood_points=blood_points,
            blood_taken=blood_taken,
            id=id,
            is_starting_point=is_starting_point,
            machine_completed=machine_completed,
            machine_pwned=machine_pwned,
            machine_state=machine_state,
            message=message,
            own_type=own_type,
            points=points,
            status=status,
            success=success,
            league_rank=league_rank,
            user_rank=user_rank,
        )

        own_response.additional_properties = d
        return own_response

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
