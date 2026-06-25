from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.meta_alt import MetaAlt
    from ..models.user_profile_activity_challenge import UserProfileActivityChallenge
    from ..models.user_profile_activity_fortress import UserProfileActivityFortress
    from ..models.user_profile_activity_machine_own import UserProfileActivityMachineOwn
    from ..models.user_profile_activity_prolab import UserProfileActivityProlab
    from ..models.user_profile_activity_sherlock import UserProfileActivitySherlock


T = TypeVar("T", bound="UserProfileActivityResponse")


@_attrs_define
class UserProfileActivityResponse:
    """Schema definition for User profile activity responses

    Attributes:
        data (list[UserProfileActivityChallenge | UserProfileActivityFortress | UserProfileActivityMachineOwn |
            UserProfileActivityProlab | UserProfileActivitySherlock]):
        meta (MetaAlt):
    """

    data: list[
        UserProfileActivityChallenge
        | UserProfileActivityFortress
        | UserProfileActivityMachineOwn
        | UserProfileActivityProlab
        | UserProfileActivitySherlock
    ]
    meta: MetaAlt
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_profile_activity_challenge import (
            UserProfileActivityChallenge,
        )
        from ..models.user_profile_activity_fortress import UserProfileActivityFortress
        from ..models.user_profile_activity_machine_own import (
            UserProfileActivityMachineOwn,
        )
        from ..models.user_profile_activity_sherlock import UserProfileActivitySherlock

        data = []
        for componentsschemas_user_profile_activity_data_item_data in self.data:
            componentsschemas_user_profile_activity_data_item: dict[str, Any]
            if isinstance(
                componentsschemas_user_profile_activity_data_item_data,
                UserProfileActivityFortress,
            ):
                componentsschemas_user_profile_activity_data_item = (
                    componentsschemas_user_profile_activity_data_item_data.to_dict()
                )
            elif isinstance(
                componentsschemas_user_profile_activity_data_item_data,
                UserProfileActivityMachineOwn,
            ):
                componentsschemas_user_profile_activity_data_item = (
                    componentsschemas_user_profile_activity_data_item_data.to_dict()
                )
            elif isinstance(
                componentsschemas_user_profile_activity_data_item_data,
                UserProfileActivityChallenge,
            ):
                componentsschemas_user_profile_activity_data_item = (
                    componentsschemas_user_profile_activity_data_item_data.to_dict()
                )
            elif isinstance(
                componentsschemas_user_profile_activity_data_item_data,
                UserProfileActivitySherlock,
            ):
                componentsschemas_user_profile_activity_data_item = (
                    componentsschemas_user_profile_activity_data_item_data.to_dict()
                )
            else:
                componentsschemas_user_profile_activity_data_item = (
                    componentsschemas_user_profile_activity_data_item_data.to_dict()
                )

            data.append(componentsschemas_user_profile_activity_data_item)

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meta_alt import MetaAlt
        from ..models.user_profile_activity_challenge import (
            UserProfileActivityChallenge,
        )
        from ..models.user_profile_activity_fortress import UserProfileActivityFortress
        from ..models.user_profile_activity_machine_own import (
            UserProfileActivityMachineOwn,
        )
        from ..models.user_profile_activity_prolab import UserProfileActivityProlab
        from ..models.user_profile_activity_sherlock import UserProfileActivitySherlock

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for componentsschemas_user_profile_activity_data_item_data in _data:

            def _parse_componentsschemas_user_profile_activity_data_item(
                data: object,
            ) -> (
                UserProfileActivityChallenge
                | UserProfileActivityFortress
                | UserProfileActivityMachineOwn
                | UserProfileActivityProlab
                | UserProfileActivitySherlock
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_profile_activity_item_type_0 = (
                        UserProfileActivityFortress.from_dict(data)
                    )

                    return componentsschemas_user_profile_activity_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_profile_activity_item_type_1 = (
                        UserProfileActivityMachineOwn.from_dict(data)
                    )

                    return componentsschemas_user_profile_activity_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_profile_activity_item_type_2 = (
                        UserProfileActivityChallenge.from_dict(data)
                    )

                    return componentsschemas_user_profile_activity_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_profile_activity_item_type_3 = (
                        UserProfileActivitySherlock.from_dict(data)
                    )

                    return componentsschemas_user_profile_activity_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_profile_activity_item_type_4 = (
                    UserProfileActivityProlab.from_dict(data)
                )

                return componentsschemas_user_profile_activity_item_type_4

            componentsschemas_user_profile_activity_data_item = (
                _parse_componentsschemas_user_profile_activity_data_item(
                    componentsschemas_user_profile_activity_data_item_data
                )
            )

            data.append(componentsschemas_user_profile_activity_data_item)

        meta = MetaAlt.from_dict(d.pop("meta"))

        user_profile_activity_response = cls(
            data=data,
            meta=meta,
        )

        user_profile_activity_response.additional_properties = d
        return user_profile_activity_response

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
