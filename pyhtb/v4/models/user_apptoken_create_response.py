from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserApptokenCreateResponse")


@_attrs_define
class UserApptokenCreateResponse:
    """
    Attributes:
        access_token (str | Unset):
        created_at (str | Unset):
        expires_at (str | Unset):
        name (str | Unset):
    """

    access_token: str | Unset = UNSET
    created_at: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        created_at = self.created_at

        expires_at = self.expires_at

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("access_token", UNSET)

        created_at = d.pop("created_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        name = d.pop("name", UNSET)

        user_apptoken_create_response = cls(
            access_token=access_token,
            created_at=created_at,
            expires_at=expires_at,
            name=name,
        )

        user_apptoken_create_response.additional_properties = d
        return user_apptoken_create_response

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
