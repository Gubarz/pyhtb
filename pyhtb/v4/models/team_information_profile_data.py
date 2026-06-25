from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lab_master import LabMaster


T = TypeVar("T", bound="TeamInformationProfileData")


@_attrs_define
class TeamInformationProfileData:
    """
    Attributes:
        active (int | Unset):
        captain (LabMaster | Unset): Schema definition for Lab Master
        country_code (str | Unset):  Example: NL.
        country_name (str | Unset):  Example: Netherlands.
        cover_image_url (None | str | Unset):
        description (str | Unset):  Example: Open for anyone who is polite, honest, nice, and willing to help others..
        discord (None | str | Unset):
        facebook (None | str | Unset):
        has_auto_generated_logo (int | Unset):
        id (int | Unset):  Example: 2102.
        is_respected (bool | Unset):  Example: True.
        join_request_sent (bool | Unset):
        logo_url (None | str | Unset):
        motto (None | str | Unset):  Example: Hacking for the fun of it! Learning it as a bonus.
        name (str | Unset):  Example: CommandlineKings.
        points (int | Unset):  Example: 1839.
        twitter (None | str | Unset):
        url (str | Unset):
    """

    active: int | Unset = UNSET
    captain: LabMaster | Unset = UNSET
    country_code: str | Unset = UNSET
    country_name: str | Unset = UNSET
    cover_image_url: None | str | Unset = UNSET
    description: str | Unset = UNSET
    discord: None | str | Unset = UNSET
    facebook: None | str | Unset = UNSET
    has_auto_generated_logo: int | Unset = UNSET
    id: int | Unset = UNSET
    is_respected: bool | Unset = UNSET
    join_request_sent: bool | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    motto: None | str | Unset = UNSET
    name: str | Unset = UNSET
    points: int | Unset = UNSET
    twitter: None | str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        captain: dict[str, Any] | Unset = UNSET
        if not isinstance(self.captain, Unset):
            captain = self.captain.to_dict()

        country_code = self.country_code

        country_name = self.country_name

        cover_image_url: None | str | Unset
        if isinstance(self.cover_image_url, Unset):
            cover_image_url = UNSET
        else:
            cover_image_url = self.cover_image_url

        description = self.description

        discord: None | str | Unset
        if isinstance(self.discord, Unset):
            discord = UNSET
        else:
            discord = self.discord

        facebook: None | str | Unset
        if isinstance(self.facebook, Unset):
            facebook = UNSET
        else:
            facebook = self.facebook

        has_auto_generated_logo = self.has_auto_generated_logo

        id = self.id

        is_respected = self.is_respected

        join_request_sent = self.join_request_sent

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        motto: None | str | Unset
        if isinstance(self.motto, Unset):
            motto = UNSET
        else:
            motto = self.motto

        name = self.name

        points = self.points

        twitter: None | str | Unset
        if isinstance(self.twitter, Unset):
            twitter = UNSET
        else:
            twitter = self.twitter

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if captain is not UNSET:
            field_dict["captain"] = captain
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if country_name is not UNSET:
            field_dict["country_name"] = country_name
        if cover_image_url is not UNSET:
            field_dict["cover_image_url"] = cover_image_url
        if description is not UNSET:
            field_dict["description"] = description
        if discord is not UNSET:
            field_dict["discord"] = discord
        if facebook is not UNSET:
            field_dict["facebook"] = facebook
        if has_auto_generated_logo is not UNSET:
            field_dict["has_auto_generated_logo"] = has_auto_generated_logo
        if id is not UNSET:
            field_dict["id"] = id
        if is_respected is not UNSET:
            field_dict["is_respected"] = is_respected
        if join_request_sent is not UNSET:
            field_dict["join_request_sent"] = join_request_sent
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if motto is not UNSET:
            field_dict["motto"] = motto
        if name is not UNSET:
            field_dict["name"] = name
        if points is not UNSET:
            field_dict["points"] = points
        if twitter is not UNSET:
            field_dict["twitter"] = twitter
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lab_master import LabMaster

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        _captain = d.pop("captain", UNSET)
        captain: LabMaster | Unset
        if isinstance(_captain, Unset):
            captain = UNSET
        else:
            captain = LabMaster.from_dict(_captain)

        country_code = d.pop("country_code", UNSET)

        country_name = d.pop("country_name", UNSET)

        def _parse_cover_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover_image_url = _parse_cover_image_url(d.pop("cover_image_url", UNSET))

        description = d.pop("description", UNSET)

        def _parse_discord(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        discord = _parse_discord(d.pop("discord", UNSET))

        def _parse_facebook(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facebook = _parse_facebook(d.pop("facebook", UNSET))

        has_auto_generated_logo = d.pop("has_auto_generated_logo", UNSET)

        id = d.pop("id", UNSET)

        is_respected = d.pop("is_respected", UNSET)

        join_request_sent = d.pop("join_request_sent", UNSET)

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        def _parse_motto(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        motto = _parse_motto(d.pop("motto", UNSET))

        name = d.pop("name", UNSET)

        points = d.pop("points", UNSET)

        def _parse_twitter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        twitter = _parse_twitter(d.pop("twitter", UNSET))

        url = d.pop("url", UNSET)

        team_information_profile_data = cls(
            active=active,
            captain=captain,
            country_code=country_code,
            country_name=country_name,
            cover_image_url=cover_image_url,
            description=description,
            discord=discord,
            facebook=facebook,
            has_auto_generated_logo=has_auto_generated_logo,
            id=id,
            is_respected=is_respected,
            join_request_sent=join_request_sent,
            logo_url=logo_url,
            motto=motto,
            name=name,
            points=points,
            twitter=twitter,
            url=url,
        )

        team_information_profile_data.additional_properties = d
        return team_information_profile_data

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
