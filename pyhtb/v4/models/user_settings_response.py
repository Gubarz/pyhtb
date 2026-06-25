from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSettingsResponse")


@_attrs_define
class UserSettingsResponse:
    """Schema definition for User Settings Response

    Attributes:
        email (str | Unset):
        hide_machine_tags (int | Unset):
        name_change_delay (bool | None | Unset):
        public (int | Unset):
    """

    email: str | Unset = UNSET
    hide_machine_tags: int | Unset = UNSET
    name_change_delay: bool | None | Unset = UNSET
    public: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        hide_machine_tags = self.hide_machine_tags

        name_change_delay: bool | None | Unset
        if isinstance(self.name_change_delay, Unset):
            name_change_delay = UNSET
        else:
            name_change_delay = self.name_change_delay

        public = self.public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if hide_machine_tags is not UNSET:
            field_dict["hide_machine_tags"] = hide_machine_tags
        if name_change_delay is not UNSET:
            field_dict["name_change_delay"] = name_change_delay
        if public is not UNSET:
            field_dict["public"] = public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        hide_machine_tags = d.pop("hide_machine_tags", UNSET)

        def _parse_name_change_delay(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        name_change_delay = _parse_name_change_delay(d.pop("name_change_delay", UNSET))

        public = d.pop("public", UNSET)

        user_settings_response = cls(
            email=email,
            hide_machine_tags=hide_machine_tags,
            name_change_delay=name_change_delay,
            public=public,
        )

        user_settings_response.additional_properties = d
        return user_settings_response

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
