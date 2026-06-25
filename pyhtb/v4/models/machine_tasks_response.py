from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_task import BaseTask
    from ..models.flag_rating_task import FlagRatingTask


T = TypeVar("T", bound="MachineTasksResponse")


@_attrs_define
class MachineTasksResponse:
    """
    Attributes:
        data (list[BaseTask | FlagRatingTask] | Unset):
    """

    data: list[BaseTask | FlagRatingTask] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.base_task import BaseTask

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for componentsschemas_machine_tasks_data_item_data in self.data:
                componentsschemas_machine_tasks_data_item: dict[str, Any]
                if isinstance(componentsschemas_machine_tasks_data_item_data, BaseTask):
                    componentsschemas_machine_tasks_data_item = (
                        componentsschemas_machine_tasks_data_item_data.to_dict()
                    )
                else:
                    componentsschemas_machine_tasks_data_item = (
                        componentsschemas_machine_tasks_data_item_data.to_dict()
                    )

                data.append(componentsschemas_machine_tasks_data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_task import BaseTask
        from ..models.flag_rating_task import FlagRatingTask

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[BaseTask | FlagRatingTask] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for componentsschemas_machine_tasks_data_item_data in _data:

                def _parse_componentsschemas_machine_tasks_data_item(
                    data: object,
                ) -> BaseTask | FlagRatingTask:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_machine_tasks_data_item_type_0 = (
                            BaseTask.from_dict(data)
                        )

                        return componentsschemas_machine_tasks_data_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_machine_tasks_data_item_type_1 = (
                        FlagRatingTask.from_dict(data)
                    )

                    return componentsschemas_machine_tasks_data_item_type_1

                componentsschemas_machine_tasks_data_item = (
                    _parse_componentsschemas_machine_tasks_data_item(
                        componentsschemas_machine_tasks_data_item_data
                    )
                )

                data.append(componentsschemas_machine_tasks_data_item)

        machine_tasks_response = cls(
            data=data,
        )

        machine_tasks_response.additional_properties = d
        return machine_tasks_response

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
