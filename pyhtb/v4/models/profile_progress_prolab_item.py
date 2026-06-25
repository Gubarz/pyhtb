from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileProgressProlabItem")


@_attrs_define
class ProfileProgressProlabItem:
    """
    Attributes:
        average_ratings (float | None | Unset):
        completion_percentage (int | Unset):
        name (str | Unset):
        owned_flags (int | Unset):
        total_flags (int | Unset):
        total_machines (int | Unset):
        mini (bool | Unset):
        avatar (str | Unset):
        id (int | Unset):
        identifier (str | Unset):
    """

    average_ratings: float | None | Unset = UNSET
    completion_percentage: int | Unset = UNSET
    name: str | Unset = UNSET
    owned_flags: int | Unset = UNSET
    total_flags: int | Unset = UNSET
    total_machines: int | Unset = UNSET
    mini: bool | Unset = UNSET
    avatar: str | Unset = UNSET
    id: int | Unset = UNSET
    identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        average_ratings: float | None | Unset
        if isinstance(self.average_ratings, Unset):
            average_ratings = UNSET
        else:
            average_ratings = self.average_ratings

        completion_percentage = self.completion_percentage

        name = self.name

        owned_flags = self.owned_flags

        total_flags = self.total_flags

        total_machines = self.total_machines

        mini = self.mini

        avatar = self.avatar

        id = self.id

        identifier = self.identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if average_ratings is not UNSET:
            field_dict["average_ratings"] = average_ratings
        if completion_percentage is not UNSET:
            field_dict["completion_percentage"] = completion_percentage
        if name is not UNSET:
            field_dict["name"] = name
        if owned_flags is not UNSET:
            field_dict["owned_flags"] = owned_flags
        if total_flags is not UNSET:
            field_dict["total_flags"] = total_flags
        if total_machines is not UNSET:
            field_dict["total_machines"] = total_machines
        if mini is not UNSET:
            field_dict["mini"] = mini
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_average_ratings(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        average_ratings = _parse_average_ratings(d.pop("average_ratings", UNSET))

        completion_percentage = d.pop("completion_percentage", UNSET)

        name = d.pop("name", UNSET)

        owned_flags = d.pop("owned_flags", UNSET)

        total_flags = d.pop("total_flags", UNSET)

        total_machines = d.pop("total_machines", UNSET)

        mini = d.pop("mini", UNSET)

        avatar = d.pop("avatar", UNSET)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        profile_progress_prolab_item = cls(
            average_ratings=average_ratings,
            completion_percentage=completion_percentage,
            name=name,
            owned_flags=owned_flags,
            total_flags=total_flags,
            total_machines=total_machines,
            mini=mini,
            avatar=avatar,
            id=id,
            identifier=identifier,
        )

        profile_progress_prolab_item.additional_properties = d
        return profile_progress_prolab_item

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
