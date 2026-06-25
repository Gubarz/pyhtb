from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.academy_module import AcademyModule


T = TypeVar("T", bound="SherlockDetail")


@_attrs_define
class SherlockDetail:
    """
    Attributes:
        academy_modules (list[AcademyModule] | None | Unset):
        description (str | Unset):
        id (int | Unset):
        user_owns_count (int | Unset):
    """

    academy_modules: list[AcademyModule] | None | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    user_owns_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        academy_modules: list[dict[str, Any]] | None | Unset
        if isinstance(self.academy_modules, Unset):
            academy_modules = UNSET
        elif isinstance(self.academy_modules, list):
            academy_modules = []
            for (
                componentsschemas_academy_modules_items_type_0_item_data
            ) in self.academy_modules:
                componentsschemas_academy_modules_items_type_0_item = (
                    componentsschemas_academy_modules_items_type_0_item_data.to_dict()
                )
                academy_modules.append(
                    componentsschemas_academy_modules_items_type_0_item
                )

        else:
            academy_modules = self.academy_modules

        description = self.description

        id = self.id

        user_owns_count = self.user_owns_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if academy_modules is not UNSET:
            field_dict["academyModules"] = academy_modules
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if user_owns_count is not UNSET:
            field_dict["user_owns_count"] = user_owns_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.academy_module import AcademyModule

        d = dict(src_dict)

        def _parse_academy_modules(data: object) -> list[AcademyModule] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_academy_modules_items_type_0 = []
                _componentsschemas_academy_modules_items_type_0 = data
                for (
                    componentsschemas_academy_modules_items_type_0_item_data
                ) in _componentsschemas_academy_modules_items_type_0:
                    componentsschemas_academy_modules_items_type_0_item = (
                        AcademyModule.from_dict(
                            componentsschemas_academy_modules_items_type_0_item_data
                        )
                    )

                    componentsschemas_academy_modules_items_type_0.append(
                        componentsschemas_academy_modules_items_type_0_item
                    )

                return componentsschemas_academy_modules_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AcademyModule] | None | Unset, data)

        academy_modules = _parse_academy_modules(d.pop("academyModules", UNSET))

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        user_owns_count = d.pop("user_owns_count", UNSET)

        sherlock_detail = cls(
            academy_modules=academy_modules,
            description=description,
            id=id,
            user_owns_count=user_owns_count,
        )

        sherlock_detail.additional_properties = d
        return sherlock_detail

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
