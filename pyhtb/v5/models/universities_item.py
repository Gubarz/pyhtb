from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UniversitiesItem")


@_attrs_define
class UniversitiesItem:
    """Schema definition for a University list item

    Attributes:
        id (int):
        name (str):
        avatar (None | str):
        country_code (str):
        country_name (str):
        users_count (int):
        respected_by_count (int):
        created_at (datetime.datetime):
    """

    id: int
    name: str
    avatar: None | str
    country_code: str
    country_name: str
    users_count: int
    respected_by_count: int
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        avatar: None | str
        avatar = self.avatar

        country_code = self.country_code

        country_name = self.country_name

        users_count = self.users_count

        respected_by_count = self.respected_by_count

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "avatar": avatar,
                "country_code": country_code,
                "country_name": country_name,
                "users_count": users_count,
                "respected_by_count": respected_by_count,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_avatar(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        avatar = _parse_avatar(d.pop("avatar"))

        country_code = d.pop("country_code")

        country_name = d.pop("country_name")

        users_count = d.pop("users_count")

        respected_by_count = d.pop("respected_by_count")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        universities_item = cls(
            id=id,
            name=name,
            avatar=avatar,
            country_code=country_code,
            country_name=country_name,
            users_count=users_count,
            respected_by_count=respected_by_count,
            created_at=created_at,
        )

        universities_item.additional_properties = d
        return universities_item

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
