from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.academy_difficulty import AcademyDifficulty
    from ..models.academy_tiers import AcademyTiers


T = TypeVar("T", bound="AcademyModule")


@_attrs_define
class AcademyModule:
    """Academy Module Item

    Attributes:
        avatar (str | Unset):  Example: https://academy.hackthebox.com/storage/modules/19/avatar.png.
        difficulty (AcademyDifficulty | Unset):
        id (int | Unset):  Example: 19.
        logo (str | Unset):  Example: https://academy.hackthebox.com/storage/modules/19/avatar.png.
        name (str | Unset):  Example: Network Enumeration with Nmap.
        tier (AcademyTiers | Unset):
        url (str | Unset):  Example: https://academy.hackthebox.com/course/preview/network-enumeration-with-nmap.
    """

    avatar: str | Unset = UNSET
    difficulty: AcademyDifficulty | Unset = UNSET
    id: int | Unset = UNSET
    logo: str | Unset = UNSET
    name: str | Unset = UNSET
    tier: AcademyTiers | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar = self.avatar

        difficulty: dict[str, Any] | Unset = UNSET
        if not isinstance(self.difficulty, Unset):
            difficulty = self.difficulty.to_dict()

        id = self.id

        logo = self.logo

        name = self.name

        tier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tier, Unset):
            tier = self.tier.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if difficulty is not UNSET:
            field_dict["difficulty"] = difficulty
        if id is not UNSET:
            field_dict["id"] = id
        if logo is not UNSET:
            field_dict["logo"] = logo
        if name is not UNSET:
            field_dict["name"] = name
        if tier is not UNSET:
            field_dict["tier"] = tier
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.academy_difficulty import AcademyDifficulty
        from ..models.academy_tiers import AcademyTiers

        d = dict(src_dict)
        avatar = d.pop("avatar", UNSET)

        _difficulty = d.pop("difficulty", UNSET)
        difficulty: AcademyDifficulty | Unset
        if isinstance(_difficulty, Unset):
            difficulty = UNSET
        else:
            difficulty = AcademyDifficulty.from_dict(_difficulty)

        id = d.pop("id", UNSET)

        logo = d.pop("logo", UNSET)

        name = d.pop("name", UNSET)

        _tier = d.pop("tier", UNSET)
        tier: AcademyTiers | Unset
        if isinstance(_tier, Unset):
            tier = UNSET
        else:
            tier = AcademyTiers.from_dict(_tier)

        url = d.pop("url", UNSET)

        academy_module = cls(
            avatar=avatar,
            difficulty=difficulty,
            id=id,
            logo=logo,
            name=name,
            tier=tier,
            url=url,
        )

        academy_module.additional_properties = d
        return academy_module

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
