from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.review_user import ReviewUser
    from ..models.user_achievement_machine_type_user import (
        UserAchievementMachineTypeUser,
    )
    from ..models.user_achievement_tar_type_user_own import (
        UserAchievementTarTypeUserOwn,
    )


T = TypeVar("T", bound="UserAchievementTargetTypeUserIdTargetIdResponse")


@_attrs_define
class UserAchievementTargetTypeUserIdTargetIdResponse:
    """Schema definition for User Achievement Target Type User Id Target

    Attributes:
        machine (UserAchievementMachineTypeUser | Unset):
        own (UserAchievementTarTypeUserOwn | Unset):
        user (None | ReviewUser | Unset):
    """

    machine: UserAchievementMachineTypeUser | Unset = UNSET
    own: UserAchievementTarTypeUserOwn | Unset = UNSET
    user: None | ReviewUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.review_user import ReviewUser

        machine: dict[str, Any] | Unset = UNSET
        if not isinstance(self.machine, Unset):
            machine = self.machine.to_dict()

        own: dict[str, Any] | Unset = UNSET
        if not isinstance(self.own, Unset):
            own = self.own.to_dict()

        user: dict[str, Any] | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, ReviewUser):
            user = self.user.to_dict()
        else:
            user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if machine is not UNSET:
            field_dict["machine"] = machine
        if own is not UNSET:
            field_dict["own"] = own
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.review_user import ReviewUser
        from ..models.user_achievement_machine_type_user import (
            UserAchievementMachineTypeUser,
        )
        from ..models.user_achievement_tar_type_user_own import (
            UserAchievementTarTypeUserOwn,
        )

        d = dict(src_dict)
        _machine = d.pop("machine", UNSET)
        machine: UserAchievementMachineTypeUser | Unset
        if isinstance(_machine, Unset):
            machine = UNSET
        else:
            machine = UserAchievementMachineTypeUser.from_dict(_machine)

        _own = d.pop("own", UNSET)
        own: UserAchievementTarTypeUserOwn | Unset
        if isinstance(_own, Unset):
            own = UNSET
        else:
            own = UserAchievementTarTypeUserOwn.from_dict(_own)

        def _parse_user(data: object) -> None | ReviewUser | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_basic_info_type_0 = ReviewUser.from_dict(data)

                return componentsschemas_user_basic_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReviewUser | Unset, data)

        user = _parse_user(d.pop("user", UNSET))

        user_achievement_target_type_user_id_target_id_response = cls(
            machine=machine,
            own=own,
            user=user,
        )

        user_achievement_target_type_user_id_target_id_response.additional_properties = d
        return user_achievement_target_type_user_id_target_id_response

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
