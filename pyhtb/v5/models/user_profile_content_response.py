from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.meta_alt import MetaAlt
    from ..models.user_profile_content_item_challenge import (
        UserProfileContentItemChallenge,
    )
    from ..models.user_profile_content_item_machine import UserProfileContentItemMachine
    from ..models.user_profile_content_item_sherlock import (
        UserProfileContentItemSherlock,
    )


T = TypeVar("T", bound="UserProfileContentResponse")


@_attrs_define
class UserProfileContentResponse:
    """Schema definition for User profile content responses.

    Attributes:
        data (list[UserProfileContentItemChallenge | UserProfileContentItemMachine | UserProfileContentItemSherlock]):
            Collection of user profile content entries.
        meta (MetaAlt):
    """

    data: list[
        UserProfileContentItemChallenge
        | UserProfileContentItemMachine
        | UserProfileContentItemSherlock
    ]
    meta: MetaAlt
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_profile_content_item_challenge import (
            UserProfileContentItemChallenge,
        )
        from ..models.user_profile_content_item_machine import (
            UserProfileContentItemMachine,
        )

        data = []
        for componentsschemas_user_profile_content_data_item_data in self.data:
            componentsschemas_user_profile_content_data_item: dict[str, Any]
            if isinstance(
                componentsschemas_user_profile_content_data_item_data,
                UserProfileContentItemMachine,
            ):
                componentsschemas_user_profile_content_data_item = (
                    componentsschemas_user_profile_content_data_item_data.to_dict()
                )
            elif isinstance(
                componentsschemas_user_profile_content_data_item_data,
                UserProfileContentItemChallenge,
            ):
                componentsschemas_user_profile_content_data_item = (
                    componentsschemas_user_profile_content_data_item_data.to_dict()
                )
            else:
                componentsschemas_user_profile_content_data_item = (
                    componentsschemas_user_profile_content_data_item_data.to_dict()
                )

            data.append(componentsschemas_user_profile_content_data_item)

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
        from ..models.user_profile_content_item_challenge import (
            UserProfileContentItemChallenge,
        )
        from ..models.user_profile_content_item_machine import (
            UserProfileContentItemMachine,
        )
        from ..models.user_profile_content_item_sherlock import (
            UserProfileContentItemSherlock,
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for componentsschemas_user_profile_content_data_item_data in _data:

            def _parse_componentsschemas_user_profile_content_data_item(
                data: object,
            ) -> (
                UserProfileContentItemChallenge
                | UserProfileContentItemMachine
                | UserProfileContentItemSherlock
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_profile_content_item_type_0 = (
                        UserProfileContentItemMachine.from_dict(data)
                    )

                    return componentsschemas_user_profile_content_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_user_profile_content_item_type_1 = (
                        UserProfileContentItemChallenge.from_dict(data)
                    )

                    return componentsschemas_user_profile_content_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_profile_content_item_type_2 = (
                    UserProfileContentItemSherlock.from_dict(data)
                )

                return componentsschemas_user_profile_content_item_type_2

            componentsschemas_user_profile_content_data_item = (
                _parse_componentsschemas_user_profile_content_data_item(
                    componentsschemas_user_profile_content_data_item_data
                )
            )

            data.append(componentsschemas_user_profile_content_data_item)

        meta = MetaAlt.from_dict(d.pop("meta"))

        user_profile_content_response = cls(
            data=data,
            meta=meta,
        )

        user_profile_content_response.additional_properties = d
        return user_profile_content_response

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
