from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyed_pro_lab_mile_stone import KeyedProLabMileStone


T = TypeVar("T", bound="ProlabProgressData")


@_attrs_define
class ProlabProgressData:
    """
    Attributes:
        keyed_pro_lab_mile_stone (list[KeyedProLabMileStone] | Unset):
        ownership (float | Unset):
        ownership_required_for_certification (float | Unset):
        user_eligible_for_certificate (bool | Unset):
    """

    keyed_pro_lab_mile_stone: list[KeyedProLabMileStone] | Unset = UNSET
    ownership: float | Unset = UNSET
    ownership_required_for_certification: float | Unset = UNSET
    user_eligible_for_certificate: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyed_pro_lab_mile_stone: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.keyed_pro_lab_mile_stone, Unset):
            keyed_pro_lab_mile_stone = []
            for (
                componentsschemas_keyed_prolab_mile_stone_items_item_data
            ) in self.keyed_pro_lab_mile_stone:
                componentsschemas_keyed_prolab_mile_stone_items_item = (
                    componentsschemas_keyed_prolab_mile_stone_items_item_data.to_dict()
                )
                keyed_pro_lab_mile_stone.append(
                    componentsschemas_keyed_prolab_mile_stone_items_item
                )

        ownership = self.ownership

        ownership_required_for_certification = self.ownership_required_for_certification

        user_eligible_for_certificate = self.user_eligible_for_certificate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keyed_pro_lab_mile_stone is not UNSET:
            field_dict["keyed_pro_lab_mile_stone"] = keyed_pro_lab_mile_stone
        if ownership is not UNSET:
            field_dict["ownership"] = ownership
        if ownership_required_for_certification is not UNSET:
            field_dict["ownership_required_for_certification"] = (
                ownership_required_for_certification
            )
        if user_eligible_for_certificate is not UNSET:
            field_dict["user_eligible_for_certificate"] = user_eligible_for_certificate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.keyed_pro_lab_mile_stone import KeyedProLabMileStone

        d = dict(src_dict)
        _keyed_pro_lab_mile_stone = d.pop("keyed_pro_lab_mile_stone", UNSET)
        keyed_pro_lab_mile_stone: list[KeyedProLabMileStone] | Unset = UNSET
        if _keyed_pro_lab_mile_stone is not UNSET:
            keyed_pro_lab_mile_stone = []
            for (
                componentsschemas_keyed_prolab_mile_stone_items_item_data
            ) in _keyed_pro_lab_mile_stone:
                componentsschemas_keyed_prolab_mile_stone_items_item = (
                    KeyedProLabMileStone.from_dict(
                        componentsschemas_keyed_prolab_mile_stone_items_item_data
                    )
                )

                keyed_pro_lab_mile_stone.append(
                    componentsschemas_keyed_prolab_mile_stone_items_item
                )

        ownership = d.pop("ownership", UNSET)

        ownership_required_for_certification = d.pop(
            "ownership_required_for_certification", UNSET
        )

        user_eligible_for_certificate = d.pop("user_eligible_for_certificate", UNSET)

        prolab_progress_data = cls(
            keyed_pro_lab_mile_stone=keyed_pro_lab_mile_stone,
            ownership=ownership,
            ownership_required_for_certification=ownership_required_for_certification,
            user_eligible_for_certificate=user_eligible_for_certificate,
        )

        prolab_progress_data.additional_properties = d
        return prolab_progress_data

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
