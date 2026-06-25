from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_rank import NewRank


T = TypeVar("T", bound="UserRank")


@_attrs_define
class UserRank:
    """
    Attributes:
        changed (bool | Unset):
        newrank (NewRank | Unset):
    """

    changed: bool | Unset = UNSET
    newrank: NewRank | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed = self.changed

        newrank: dict[str, Any] | Unset = UNSET
        if not isinstance(self.newrank, Unset):
            newrank = self.newrank.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changed is not UNSET:
            field_dict["changed"] = changed
        if newrank is not UNSET:
            field_dict["newrank"] = newrank

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_rank import NewRank

        d = dict(src_dict)
        changed = d.pop("changed", UNSET)

        _newrank = d.pop("newrank", UNSET)
        newrank: NewRank | Unset
        if isinstance(_newrank, Unset):
            newrank = UNSET
        else:
            newrank = NewRank.from_dict(_newrank)

        user_rank = cls(
            changed=changed,
            newrank=newrank,
        )

        user_rank.additional_properties = d
        return user_rank

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
