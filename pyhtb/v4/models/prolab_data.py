from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lab_master import LabMaster
    from ..models.pesentation_detail import PesentationDetail


T = TypeVar("T", bound="ProlabData")


@_attrs_define
class ProlabData:
    """Schema definition for Prolab Data

    Attributes:
        active_users (int | Unset):  Example: 15.
        can_interact (bool | Unset):
        cover_image_url (None | str | Unset):
        description (str | Unset):  Example: <h4>RastaLabs</h4>....
        entry_points (list[None | str] | None | Unset):
        id (int | Unset):  Example: 1.
        identifier (str | Unset):
        lab_masters (list[LabMaster] | Unset):
        lab_servers_count (int | Unset):  Example: 6.
        mini (bool | Unset):
        name (str | Unset):  Example: RastaLabs.
        pro_flags_count (int | Unset):  Example: 22.
        pro_machines_count (int | Unset):  Example: 15.
        state (str | Unset):
        version (str | Unset):  Example: 1.3.
        video_url (None | str | Unset):
        writeup (None | str | Unset):
        avatar_48_circle_url (str | Unset):
        avatar_48_url (str | Unset):
        avatar_url (str | Unset):
        presentation_detail (PesentationDetail | Unset):
        reviews_average (str | Unset):
        reviews_count (int | Unset):
        user_has_reviewed (bool | Unset):
    """

    active_users: int | Unset = UNSET
    can_interact: bool | Unset = UNSET
    cover_image_url: None | str | Unset = UNSET
    description: str | Unset = UNSET
    entry_points: list[None | str] | None | Unset = UNSET
    id: int | Unset = UNSET
    identifier: str | Unset = UNSET
    lab_masters: list[LabMaster] | Unset = UNSET
    lab_servers_count: int | Unset = UNSET
    mini: bool | Unset = UNSET
    name: str | Unset = UNSET
    pro_flags_count: int | Unset = UNSET
    pro_machines_count: int | Unset = UNSET
    state: str | Unset = UNSET
    version: str | Unset = UNSET
    video_url: None | str | Unset = UNSET
    writeup: None | str | Unset = UNSET
    avatar_48_circle_url: str | Unset = UNSET
    avatar_48_url: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    presentation_detail: PesentationDetail | Unset = UNSET
    reviews_average: str | Unset = UNSET
    reviews_count: int | Unset = UNSET
    user_has_reviewed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_users = self.active_users

        can_interact = self.can_interact

        cover_image_url: None | str | Unset
        if isinstance(self.cover_image_url, Unset):
            cover_image_url = UNSET
        else:
            cover_image_url = self.cover_image_url

        description = self.description

        entry_points: list[None | str] | None | Unset
        if isinstance(self.entry_points, Unset):
            entry_points = UNSET
        elif isinstance(self.entry_points, list):
            entry_points = []
            for componentsschemas_string_array_type_0_item_data in self.entry_points:
                componentsschemas_string_array_type_0_item: None | str
                componentsschemas_string_array_type_0_item = (
                    componentsschemas_string_array_type_0_item_data
                )
                entry_points.append(componentsschemas_string_array_type_0_item)

        else:
            entry_points = self.entry_points

        id = self.id

        identifier = self.identifier

        lab_masters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lab_masters, Unset):
            lab_masters = []
            for componentsschemas_lab_master_items_item_data in self.lab_masters:
                componentsschemas_lab_master_items_item = (
                    componentsschemas_lab_master_items_item_data.to_dict()
                )
                lab_masters.append(componentsschemas_lab_master_items_item)

        lab_servers_count = self.lab_servers_count

        mini = self.mini

        name = self.name

        pro_flags_count = self.pro_flags_count

        pro_machines_count = self.pro_machines_count

        state = self.state

        version = self.version

        video_url: None | str | Unset
        if isinstance(self.video_url, Unset):
            video_url = UNSET
        else:
            video_url = self.video_url

        writeup: None | str | Unset
        if isinstance(self.writeup, Unset):
            writeup = UNSET
        else:
            writeup = self.writeup

        avatar_48_circle_url = self.avatar_48_circle_url

        avatar_48_url = self.avatar_48_url

        avatar_url = self.avatar_url

        presentation_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.presentation_detail, Unset):
            presentation_detail = self.presentation_detail.to_dict()

        reviews_average = self.reviews_average

        reviews_count = self.reviews_count

        user_has_reviewed = self.user_has_reviewed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_users is not UNSET:
            field_dict["active_users"] = active_users
        if can_interact is not UNSET:
            field_dict["can_interact"] = can_interact
        if cover_image_url is not UNSET:
            field_dict["cover_image_url"] = cover_image_url
        if description is not UNSET:
            field_dict["description"] = description
        if entry_points is not UNSET:
            field_dict["entry_points"] = entry_points
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if lab_masters is not UNSET:
            field_dict["lab_masters"] = lab_masters
        if lab_servers_count is not UNSET:
            field_dict["lab_servers_count"] = lab_servers_count
        if mini is not UNSET:
            field_dict["mini"] = mini
        if name is not UNSET:
            field_dict["name"] = name
        if pro_flags_count is not UNSET:
            field_dict["pro_flags_count"] = pro_flags_count
        if pro_machines_count is not UNSET:
            field_dict["pro_machines_count"] = pro_machines_count
        if state is not UNSET:
            field_dict["state"] = state
        if version is not UNSET:
            field_dict["version"] = version
        if video_url is not UNSET:
            field_dict["video_url"] = video_url
        if writeup is not UNSET:
            field_dict["writeup"] = writeup
        if avatar_48_circle_url is not UNSET:
            field_dict["avatar_48_circle_url"] = avatar_48_circle_url
        if avatar_48_url is not UNSET:
            field_dict["avatar_48_url"] = avatar_48_url
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if presentation_detail is not UNSET:
            field_dict["presentation_detail"] = presentation_detail
        if reviews_average is not UNSET:
            field_dict["reviews_average"] = reviews_average
        if reviews_count is not UNSET:
            field_dict["reviews_count"] = reviews_count
        if user_has_reviewed is not UNSET:
            field_dict["user_has_reviewed"] = user_has_reviewed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lab_master import LabMaster
        from ..models.pesentation_detail import PesentationDetail

        d = dict(src_dict)
        active_users = d.pop("active_users", UNSET)

        can_interact = d.pop("can_interact", UNSET)

        def _parse_cover_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover_image_url = _parse_cover_image_url(d.pop("cover_image_url", UNSET))

        description = d.pop("description", UNSET)

        def _parse_entry_points(data: object) -> list[None | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_string_array_type_0 = []
                _componentsschemas_string_array_type_0 = data
                for (
                    componentsschemas_string_array_type_0_item_data
                ) in _componentsschemas_string_array_type_0:

                    def _parse_componentsschemas_string_array_type_0_item(
                        data: object,
                    ) -> None | str:
                        if data is None:
                            return data
                        return cast(None | str, data)

                    componentsschemas_string_array_type_0_item = (
                        _parse_componentsschemas_string_array_type_0_item(
                            componentsschemas_string_array_type_0_item_data
                        )
                    )

                    componentsschemas_string_array_type_0.append(
                        componentsschemas_string_array_type_0_item
                    )

                return componentsschemas_string_array_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | str] | None | Unset, data)

        entry_points = _parse_entry_points(d.pop("entry_points", UNSET))

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        _lab_masters = d.pop("lab_masters", UNSET)
        lab_masters: list[LabMaster] | Unset = UNSET
        if _lab_masters is not UNSET:
            lab_masters = []
            for componentsschemas_lab_master_items_item_data in _lab_masters:
                componentsschemas_lab_master_items_item = LabMaster.from_dict(
                    componentsschemas_lab_master_items_item_data
                )

                lab_masters.append(componentsschemas_lab_master_items_item)

        lab_servers_count = d.pop("lab_servers_count", UNSET)

        mini = d.pop("mini", UNSET)

        name = d.pop("name", UNSET)

        pro_flags_count = d.pop("pro_flags_count", UNSET)

        pro_machines_count = d.pop("pro_machines_count", UNSET)

        state = d.pop("state", UNSET)

        version = d.pop("version", UNSET)

        def _parse_video_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        video_url = _parse_video_url(d.pop("video_url", UNSET))

        def _parse_writeup(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        writeup = _parse_writeup(d.pop("writeup", UNSET))

        avatar_48_circle_url = d.pop("avatar_48_circle_url", UNSET)

        avatar_48_url = d.pop("avatar_48_url", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        _presentation_detail = d.pop("presentation_detail", UNSET)
        presentation_detail: PesentationDetail | Unset
        if isinstance(_presentation_detail, Unset):
            presentation_detail = UNSET
        else:
            presentation_detail = PesentationDetail.from_dict(_presentation_detail)

        reviews_average = d.pop("reviews_average", UNSET)

        reviews_count = d.pop("reviews_count", UNSET)

        user_has_reviewed = d.pop("user_has_reviewed", UNSET)

        prolab_data = cls(
            active_users=active_users,
            can_interact=can_interact,
            cover_image_url=cover_image_url,
            description=description,
            entry_points=entry_points,
            id=id,
            identifier=identifier,
            lab_masters=lab_masters,
            lab_servers_count=lab_servers_count,
            mini=mini,
            name=name,
            pro_flags_count=pro_flags_count,
            pro_machines_count=pro_machines_count,
            state=state,
            version=version,
            video_url=video_url,
            writeup=writeup,
            avatar_48_circle_url=avatar_48_circle_url,
            avatar_48_url=avatar_48_url,
            avatar_url=avatar_url,
            presentation_detail=presentation_detail,
            reviews_average=reviews_average,
            reviews_count=reviews_count,
            user_has_reviewed=user_has_reviewed,
        )

        prolab_data.additional_properties = d
        return prolab_data

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
