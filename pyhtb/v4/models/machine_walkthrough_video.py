from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MachineWalkthroughVideo")


@_attrs_define
class MachineWalkthroughVideo:
    """
    Attributes:
        creator_avatar (str | Unset):
        creator_id (int | Unset):
        creator_name (str | Unset):
        youtube_id (str | Unset):
    """

    creator_avatar: str | Unset = UNSET
    creator_id: int | Unset = UNSET
    creator_name: str | Unset = UNSET
    youtube_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creator_avatar = self.creator_avatar

        creator_id = self.creator_id

        creator_name = self.creator_name

        youtube_id = self.youtube_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creator_avatar is not UNSET:
            field_dict["creator_avatar"] = creator_avatar
        if creator_id is not UNSET:
            field_dict["creator_id"] = creator_id
        if creator_name is not UNSET:
            field_dict["creator_name"] = creator_name
        if youtube_id is not UNSET:
            field_dict["youtube_id"] = youtube_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator_avatar = d.pop("creator_avatar", UNSET)

        creator_id = d.pop("creator_id", UNSET)

        creator_name = d.pop("creator_name", UNSET)

        youtube_id = d.pop("youtube_id", UNSET)

        machine_walkthrough_video = cls(
            creator_avatar=creator_avatar,
            creator_id=creator_id,
            creator_name=creator_name,
            youtube_id=youtube_id,
        )

        machine_walkthrough_video.additional_properties = d
        return machine_walkthrough_video

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
