from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.designated_level import DesignatedLevel
    from ..models.lab_master import LabMaster
    from ..models.social_links import SocialLinks


T = TypeVar("T", bound="ProlabOverviewData")


@_attrs_define
class ProlabOverviewData:
    """Schema definition for Prolab Overview Data

    Attributes:
        content_id (str | Unset):
        designated_level (DesignatedLevel | Unset): Schema definition for Designated Level
        excerpt (None | str | Unset):
        id (int | Unset):  Example: 1.
        identifier (str | Unset):
        lab_masters (list[LabMaster] | Unset):
        mini (bool | Unset):
        name (str | Unset):  Example: RastaLabs.
        new_version (bool | Unset):
        overview_image_url (None | str | Unset):
        pro_flags_count (int | Unset):  Example: 22.
        pro_machines_count (int | Unset):  Example: 15.
        skill_level (str | Unset):  Example: INTERMEDIATE.
        social_links (SocialLinks | Unset): Schema definition for Social Links
        state (str | Unset):
        user_eligible_to_play (bool | Unset):
        version (str | Unset):  Example: 1.3.
        cover_image_url (str | Unset):
    """

    content_id: str | Unset = UNSET
    designated_level: DesignatedLevel | Unset = UNSET
    excerpt: None | str | Unset = UNSET
    id: int | Unset = UNSET
    identifier: str | Unset = UNSET
    lab_masters: list[LabMaster] | Unset = UNSET
    mini: bool | Unset = UNSET
    name: str | Unset = UNSET
    new_version: bool | Unset = UNSET
    overview_image_url: None | str | Unset = UNSET
    pro_flags_count: int | Unset = UNSET
    pro_machines_count: int | Unset = UNSET
    skill_level: str | Unset = UNSET
    social_links: SocialLinks | Unset = UNSET
    state: str | Unset = UNSET
    user_eligible_to_play: bool | Unset = UNSET
    version: str | Unset = UNSET
    cover_image_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_id = self.content_id

        designated_level: dict[str, Any] | Unset = UNSET
        if not isinstance(self.designated_level, Unset):
            designated_level = self.designated_level.to_dict()

        excerpt: None | str | Unset
        if isinstance(self.excerpt, Unset):
            excerpt = UNSET
        else:
            excerpt = self.excerpt

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

        mini = self.mini

        name = self.name

        new_version = self.new_version

        overview_image_url: None | str | Unset
        if isinstance(self.overview_image_url, Unset):
            overview_image_url = UNSET
        else:
            overview_image_url = self.overview_image_url

        pro_flags_count = self.pro_flags_count

        pro_machines_count = self.pro_machines_count

        skill_level = self.skill_level

        social_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.social_links, Unset):
            social_links = self.social_links.to_dict()

        state = self.state

        user_eligible_to_play = self.user_eligible_to_play

        version = self.version

        cover_image_url = self.cover_image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_id is not UNSET:
            field_dict["content_id"] = content_id
        if designated_level is not UNSET:
            field_dict["designated_level"] = designated_level
        if excerpt is not UNSET:
            field_dict["excerpt"] = excerpt
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if lab_masters is not UNSET:
            field_dict["lab_masters"] = lab_masters
        if mini is not UNSET:
            field_dict["mini"] = mini
        if name is not UNSET:
            field_dict["name"] = name
        if new_version is not UNSET:
            field_dict["new_version"] = new_version
        if overview_image_url is not UNSET:
            field_dict["overview_image_url"] = overview_image_url
        if pro_flags_count is not UNSET:
            field_dict["pro_flags_count"] = pro_flags_count
        if pro_machines_count is not UNSET:
            field_dict["pro_machines_count"] = pro_machines_count
        if skill_level is not UNSET:
            field_dict["skill_level"] = skill_level
        if social_links is not UNSET:
            field_dict["social_links"] = social_links
        if state is not UNSET:
            field_dict["state"] = state
        if user_eligible_to_play is not UNSET:
            field_dict["user_eligible_to_play"] = user_eligible_to_play
        if version is not UNSET:
            field_dict["version"] = version
        if cover_image_url is not UNSET:
            field_dict["cover_image_url"] = cover_image_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.designated_level import DesignatedLevel
        from ..models.lab_master import LabMaster
        from ..models.social_links import SocialLinks

        d = dict(src_dict)
        content_id = d.pop("content_id", UNSET)

        _designated_level = d.pop("designated_level", UNSET)
        designated_level: DesignatedLevel | Unset
        if isinstance(_designated_level, Unset):
            designated_level = UNSET
        else:
            designated_level = DesignatedLevel.from_dict(_designated_level)

        def _parse_excerpt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        excerpt = _parse_excerpt(d.pop("excerpt", UNSET))

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

        mini = d.pop("mini", UNSET)

        name = d.pop("name", UNSET)

        new_version = d.pop("new_version", UNSET)

        def _parse_overview_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overview_image_url = _parse_overview_image_url(
            d.pop("overview_image_url", UNSET)
        )

        pro_flags_count = d.pop("pro_flags_count", UNSET)

        pro_machines_count = d.pop("pro_machines_count", UNSET)

        skill_level = d.pop("skill_level", UNSET)

        _social_links = d.pop("social_links", UNSET)
        social_links: SocialLinks | Unset
        if isinstance(_social_links, Unset):
            social_links = UNSET
        else:
            social_links = SocialLinks.from_dict(_social_links)

        state = d.pop("state", UNSET)

        user_eligible_to_play = d.pop("user_eligible_to_play", UNSET)

        version = d.pop("version", UNSET)

        cover_image_url = d.pop("cover_image_url", UNSET)

        prolab_overview_data = cls(
            content_id=content_id,
            designated_level=designated_level,
            excerpt=excerpt,
            id=id,
            identifier=identifier,
            lab_masters=lab_masters,
            mini=mini,
            name=name,
            new_version=new_version,
            overview_image_url=overview_image_url,
            pro_flags_count=pro_flags_count,
            pro_machines_count=pro_machines_count,
            skill_level=skill_level,
            social_links=social_links,
            state=state,
            user_eligible_to_play=user_eligible_to_play,
            version=version,
            cover_image_url=cover_image_url,
        )

        prolab_overview_data.additional_properties = d
        return prolab_overview_data

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
