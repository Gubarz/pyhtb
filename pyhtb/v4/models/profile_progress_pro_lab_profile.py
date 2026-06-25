from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_progress_prolab_item import ProfileProgressProlabItem


T = TypeVar("T", bound="ProfileProgressProLabProfile")


@_attrs_define
class ProfileProgressProLabProfile:
    """
    Attributes:
        prolabs (list[ProfileProgressProlabItem] | Unset):
    """

    prolabs: list[ProfileProgressProlabItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prolabs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.prolabs, Unset):
            prolabs = []
            for (
                componentsschemas_profile_progress_prolab_items_item_data
            ) in self.prolabs:
                componentsschemas_profile_progress_prolab_items_item = (
                    componentsschemas_profile_progress_prolab_items_item_data.to_dict()
                )
                prolabs.append(componentsschemas_profile_progress_prolab_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prolabs is not UNSET:
            field_dict["prolabs"] = prolabs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_progress_prolab_item import ProfileProgressProlabItem

        d = dict(src_dict)
        _prolabs = d.pop("prolabs", UNSET)
        prolabs: list[ProfileProgressProlabItem] | Unset = UNSET
        if _prolabs is not UNSET:
            prolabs = []
            for componentsschemas_profile_progress_prolab_items_item_data in _prolabs:
                componentsschemas_profile_progress_prolab_items_item = (
                    ProfileProgressProlabItem.from_dict(
                        componentsschemas_profile_progress_prolab_items_item_data
                    )
                )

                prolabs.append(componentsschemas_profile_progress_prolab_items_item)

        profile_progress_pro_lab_profile = cls(
            prolabs=prolabs,
        )

        profile_progress_pro_lab_profile.additional_properties = d
        return profile_progress_pro_lab_profile

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
