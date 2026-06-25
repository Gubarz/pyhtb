from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeasonListDataItem")


@_attrs_define
class SeasonListDataItem:
    """
    Attributes:
        active (bool | Unset):
        background_image (None | str | Unset):
        end_date (datetime.datetime | Unset):
        id (int | Unset):
        is_visible (bool | Unset):
        logo (None | str | Unset):
        name (str | Unset):
        start_date (datetime.datetime | Unset):
        state (str | Unset):
        subtitle (None | str | Unset):
        current_week (int | None | Unset):
        weeks (int | Unset):
        players (int | Unset):
        new_background_image (str | Unset):
        trailer (None | str | Unset):
    """

    active: bool | Unset = UNSET
    background_image: None | str | Unset = UNSET
    end_date: datetime.datetime | Unset = UNSET
    id: int | Unset = UNSET
    is_visible: bool | Unset = UNSET
    logo: None | str | Unset = UNSET
    name: str | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    state: str | Unset = UNSET
    subtitle: None | str | Unset = UNSET
    current_week: int | None | Unset = UNSET
    weeks: int | Unset = UNSET
    players: int | Unset = UNSET
    new_background_image: str | Unset = UNSET
    trailer: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        background_image: None | str | Unset
        if isinstance(self.background_image, Unset):
            background_image = UNSET
        else:
            background_image = self.background_image

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        id = self.id

        is_visible = self.is_visible

        logo: None | str | Unset
        if isinstance(self.logo, Unset):
            logo = UNSET
        else:
            logo = self.logo

        name = self.name

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        state = self.state

        subtitle: None | str | Unset
        if isinstance(self.subtitle, Unset):
            subtitle = UNSET
        else:
            subtitle = self.subtitle

        current_week: int | None | Unset
        if isinstance(self.current_week, Unset):
            current_week = UNSET
        else:
            current_week = self.current_week

        weeks = self.weeks

        players = self.players

        new_background_image = self.new_background_image

        trailer: None | str | Unset
        if isinstance(self.trailer, Unset):
            trailer = UNSET
        else:
            trailer = self.trailer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if background_image is not UNSET:
            field_dict["background_image"] = background_image
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if id is not UNSET:
            field_dict["id"] = id
        if is_visible is not UNSET:
            field_dict["is_visible"] = is_visible
        if logo is not UNSET:
            field_dict["logo"] = logo
        if name is not UNSET:
            field_dict["name"] = name
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if state is not UNSET:
            field_dict["state"] = state
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if current_week is not UNSET:
            field_dict["current_week"] = current_week
        if weeks is not UNSET:
            field_dict["weeks"] = weeks
        if players is not UNSET:
            field_dict["players"] = players
        if new_background_image is not UNSET:
            field_dict["new_background_image"] = new_background_image
        if trailer is not UNSET:
            field_dict["trailer"] = trailer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active", UNSET)

        def _parse_background_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        background_image = _parse_background_image(d.pop("background_image", UNSET))

        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.datetime | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = datetime.datetime.fromisoformat(_end_date)

        id = d.pop("id", UNSET)

        is_visible = d.pop("is_visible", UNSET)

        def _parse_logo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo = _parse_logo(d.pop("logo", UNSET))

        name = d.pop("name", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = datetime.datetime.fromisoformat(_start_date)

        state = d.pop("state", UNSET)

        def _parse_subtitle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subtitle = _parse_subtitle(d.pop("subtitle", UNSET))

        def _parse_current_week(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        current_week = _parse_current_week(d.pop("current_week", UNSET))

        weeks = d.pop("weeks", UNSET)

        players = d.pop("players", UNSET)

        new_background_image = d.pop("new_background_image", UNSET)

        def _parse_trailer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trailer = _parse_trailer(d.pop("trailer", UNSET))

        season_list_data_item = cls(
            active=active,
            background_image=background_image,
            end_date=end_date,
            id=id,
            is_visible=is_visible,
            logo=logo,
            name=name,
            start_date=start_date,
            state=state,
            subtitle=subtitle,
            current_week=current_week,
            weeks=weeks,
            players=players,
            new_background_image=new_background_image,
            trailer=trailer,
        )

        season_list_data_item.additional_properties = d
        return season_list_data_item

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
