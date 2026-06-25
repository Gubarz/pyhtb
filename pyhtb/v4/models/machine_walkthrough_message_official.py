from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MachineWalkthroughMessageOfficial")


@_attrs_define
class MachineWalkthroughMessageOfficial:
    """
    Attributes:
        disliked_by_user (float | None | Unset):
        filename (str | Unset):
        liked_by_user (bool | None | Unset):
        rating (float | Unset):
        sha256 (str | Unset):
        threshold_for_display_reached (int | Unset):
        total_ratings (int | Unset):
    """

    disliked_by_user: float | None | Unset = UNSET
    filename: str | Unset = UNSET
    liked_by_user: bool | None | Unset = UNSET
    rating: float | Unset = UNSET
    sha256: str | Unset = UNSET
    threshold_for_display_reached: int | Unset = UNSET
    total_ratings: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disliked_by_user: float | None | Unset
        if isinstance(self.disliked_by_user, Unset):
            disliked_by_user = UNSET
        else:
            disliked_by_user = self.disliked_by_user

        filename = self.filename

        liked_by_user: bool | None | Unset
        if isinstance(self.liked_by_user, Unset):
            liked_by_user = UNSET
        else:
            liked_by_user = self.liked_by_user

        rating = self.rating

        sha256 = self.sha256

        threshold_for_display_reached = self.threshold_for_display_reached

        total_ratings = self.total_ratings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disliked_by_user is not UNSET:
            field_dict["dislikedByUser"] = disliked_by_user
        if filename is not UNSET:
            field_dict["filename"] = filename
        if liked_by_user is not UNSET:
            field_dict["likedByUser"] = liked_by_user
        if rating is not UNSET:
            field_dict["rating"] = rating
        if sha256 is not UNSET:
            field_dict["sha256"] = sha256
        if threshold_for_display_reached is not UNSET:
            field_dict["threshold_for_display_reached"] = threshold_for_display_reached
        if total_ratings is not UNSET:
            field_dict["total_ratings"] = total_ratings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_disliked_by_user(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        disliked_by_user = _parse_disliked_by_user(d.pop("dislikedByUser", UNSET))

        filename = d.pop("filename", UNSET)

        def _parse_liked_by_user(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        liked_by_user = _parse_liked_by_user(d.pop("likedByUser", UNSET))

        rating = d.pop("rating", UNSET)

        sha256 = d.pop("sha256", UNSET)

        threshold_for_display_reached = d.pop("threshold_for_display_reached", UNSET)

        total_ratings = d.pop("total_ratings", UNSET)

        machine_walkthrough_message_official = cls(
            disliked_by_user=disliked_by_user,
            filename=filename,
            liked_by_user=liked_by_user,
            rating=rating,
            sha256=sha256,
            threshold_for_display_reached=threshold_for_display_reached,
            total_ratings=total_ratings,
        )

        machine_walkthrough_message_official.additional_properties = d
        return machine_walkthrough_message_official

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
