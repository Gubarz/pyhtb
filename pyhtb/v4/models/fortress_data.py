from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company import Company
    from ..models.flag import Flag
    from ..models.user_availability import UserAvailability


T = TypeVar("T", bound="FortressData")


@_attrs_define
class FortressData:
    """Schema definition for Fortress Data

    Attributes:
        company (Company | Unset): Schema definition for Company
        completion_message (None | str | Unset):
        cover_image_url (str | Unset):  Example:
            https://labs.hackthebox.com/storage/fortresses/c4ca4238a0b923820dcc509a6f75849b_cover_full.png.
        description (str | Unset):  Example: Lift off with this introductory fortress from Jet! Featuring interesting
            web vectors and challenges, this fortress is perfect for those getting started..
        flags (list[Flag] | Unset):
        has_completion_message (bool | Unset):
        id (int | Unset):  Example: 1.
        image (str | Unset):  Example:
            https://labs.hackthebox.com/storage/fortresses/c4ca4238a0b923820dcc509a6f75849b_logo.svg.
        ip (str | Unset):  Example: 10.13.37.10.
        name (str | Unset):  Example: Jet.
        players_completed (int | Unset):  Example: 2504.
        points (str | Unset):  Example: 100.
        progress_percent (float | Unset):
        reset_votes (int | Unset):
        user_availability (UserAvailability | Unset): Schema definition for User Availability
    """

    company: Company | Unset = UNSET
    completion_message: None | str | Unset = UNSET
    cover_image_url: str | Unset = UNSET
    description: str | Unset = UNSET
    flags: list[Flag] | Unset = UNSET
    has_completion_message: bool | Unset = UNSET
    id: int | Unset = UNSET
    image: str | Unset = UNSET
    ip: str | Unset = UNSET
    name: str | Unset = UNSET
    players_completed: int | Unset = UNSET
    points: str | Unset = UNSET
    progress_percent: float | Unset = UNSET
    reset_votes: int | Unset = UNSET
    user_availability: UserAvailability | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company: dict[str, Any] | Unset = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        completion_message: None | str | Unset
        if isinstance(self.completion_message, Unset):
            completion_message = UNSET
        else:
            completion_message = self.completion_message

        cover_image_url = self.cover_image_url

        description = self.description

        flags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = []
            for componentsschemas_flags_items_item_data in self.flags:
                componentsschemas_flags_items_item = (
                    componentsschemas_flags_items_item_data.to_dict()
                )
                flags.append(componentsschemas_flags_items_item)

        has_completion_message = self.has_completion_message

        id = self.id

        image = self.image

        ip = self.ip

        name = self.name

        players_completed = self.players_completed

        points = self.points

        progress_percent = self.progress_percent

        reset_votes = self.reset_votes

        user_availability: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_availability, Unset):
            user_availability = self.user_availability.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company is not UNSET:
            field_dict["company"] = company
        if completion_message is not UNSET:
            field_dict["completion_message"] = completion_message
        if cover_image_url is not UNSET:
            field_dict["cover_image_url"] = cover_image_url
        if description is not UNSET:
            field_dict["description"] = description
        if flags is not UNSET:
            field_dict["flags"] = flags
        if has_completion_message is not UNSET:
            field_dict["has_completion_message"] = has_completion_message
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if ip is not UNSET:
            field_dict["ip"] = ip
        if name is not UNSET:
            field_dict["name"] = name
        if players_completed is not UNSET:
            field_dict["players_completed"] = players_completed
        if points is not UNSET:
            field_dict["points"] = points
        if progress_percent is not UNSET:
            field_dict["progress_percent"] = progress_percent
        if reset_votes is not UNSET:
            field_dict["reset_votes"] = reset_votes
        if user_availability is not UNSET:
            field_dict["user_availability"] = user_availability

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company import Company
        from ..models.flag import Flag
        from ..models.user_availability import UserAvailability

        d = dict(src_dict)
        _company = d.pop("company", UNSET)
        company: Company | Unset
        if isinstance(_company, Unset):
            company = UNSET
        else:
            company = Company.from_dict(_company)

        def _parse_completion_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completion_message = _parse_completion_message(
            d.pop("completion_message", UNSET)
        )

        cover_image_url = d.pop("cover_image_url", UNSET)

        description = d.pop("description", UNSET)

        _flags = d.pop("flags", UNSET)
        flags: list[Flag] | Unset = UNSET
        if _flags is not UNSET:
            flags = []
            for componentsschemas_flags_items_item_data in _flags:
                componentsschemas_flags_items_item = Flag.from_dict(
                    componentsschemas_flags_items_item_data
                )

                flags.append(componentsschemas_flags_items_item)

        has_completion_message = d.pop("has_completion_message", UNSET)

        id = d.pop("id", UNSET)

        image = d.pop("image", UNSET)

        ip = d.pop("ip", UNSET)

        name = d.pop("name", UNSET)

        players_completed = d.pop("players_completed", UNSET)

        points = d.pop("points", UNSET)

        progress_percent = d.pop("progress_percent", UNSET)

        reset_votes = d.pop("reset_votes", UNSET)

        _user_availability = d.pop("user_availability", UNSET)
        user_availability: UserAvailability | Unset
        if isinstance(_user_availability, Unset):
            user_availability = UNSET
        else:
            user_availability = UserAvailability.from_dict(_user_availability)

        fortress_data = cls(
            company=company,
            completion_message=completion_message,
            cover_image_url=cover_image_url,
            description=description,
            flags=flags,
            has_completion_message=has_completion_message,
            id=id,
            image=image,
            ip=ip,
            name=name,
            players_completed=players_completed,
            points=points,
            progress_percent=progress_percent,
            reset_votes=reset_votes,
            user_availability=user_availability,
        )

        fortress_data.additional_properties = d
        return fortress_data

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
