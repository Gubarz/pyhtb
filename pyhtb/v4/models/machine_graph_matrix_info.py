from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matrix_info import MatrixInfo


T = TypeVar("T", bound="MachineGraphMatrixInfo")


@_attrs_define
class MachineGraphMatrixInfo:
    """
    Attributes:
        aggregate (MatrixInfo | Unset):
        maker (MatrixInfo | Unset):
        user (MatrixInfo | Unset):
    """

    aggregate: MatrixInfo | Unset = UNSET
    maker: MatrixInfo | Unset = UNSET
    user: MatrixInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aggregate, Unset):
            aggregate = self.aggregate.to_dict()

        maker: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maker, Unset):
            maker = self.maker.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregate is not UNSET:
            field_dict["aggregate"] = aggregate
        if maker is not UNSET:
            field_dict["maker"] = maker
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matrix_info import MatrixInfo

        d = dict(src_dict)
        _aggregate = d.pop("aggregate", UNSET)
        aggregate: MatrixInfo | Unset
        if isinstance(_aggregate, Unset):
            aggregate = UNSET
        else:
            aggregate = MatrixInfo.from_dict(_aggregate)

        _maker = d.pop("maker", UNSET)
        maker: MatrixInfo | Unset
        if isinstance(_maker, Unset):
            maker = UNSET
        else:
            maker = MatrixInfo.from_dict(_maker)

        _user = d.pop("user", UNSET)
        user: MatrixInfo | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = MatrixInfo.from_dict(_user)

        machine_graph_matrix_info = cls(
            aggregate=aggregate,
            maker=maker,
            user=user,
        )

        machine_graph_matrix_info.additional_properties = d
        return machine_graph_matrix_info

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
