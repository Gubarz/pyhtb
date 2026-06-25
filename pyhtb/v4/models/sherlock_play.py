from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.maker import Maker
    from ..models.play_info_alt import PlayInfoAlt
    from ..models.sherlock_blood import SherlockBlood


T = TypeVar("T", bound="SherlockPlay")


@_attrs_define
class SherlockPlay:
    """
    Attributes:
        creators (list[Maker | None] | Unset):
        file_name (str | Unset):
        file_size (str | Unset):
        id (int | Unset):
        scenario (str | Unset):
        play_info (PlayInfoAlt | Unset): Alternate structure of PlayInfo used in Sherlocks and Challenges
        blood (SherlockBlood | Unset):
    """

    creators: list[Maker | None] | Unset = UNSET
    file_name: str | Unset = UNSET
    file_size: str | Unset = UNSET
    id: int | Unset = UNSET
    scenario: str | Unset = UNSET
    play_info: PlayInfoAlt | Unset = UNSET
    blood: SherlockBlood | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.maker import Maker

        creators: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.creators, Unset):
            creators = []
            for (
                componentsschemas_sherlock_play_creators_items_item_data
            ) in self.creators:
                componentsschemas_sherlock_play_creators_items_item: (
                    dict[str, Any] | None
                )
                if isinstance(
                    componentsschemas_sherlock_play_creators_items_item_data, Maker
                ):
                    componentsschemas_sherlock_play_creators_items_item = componentsschemas_sherlock_play_creators_items_item_data.to_dict()
                else:
                    componentsschemas_sherlock_play_creators_items_item = (
                        componentsschemas_sherlock_play_creators_items_item_data
                    )
                creators.append(componentsschemas_sherlock_play_creators_items_item)

        file_name = self.file_name

        file_size = self.file_size

        id = self.id

        scenario = self.scenario

        play_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.play_info, Unset):
            play_info = self.play_info.to_dict()

        blood: dict[str, Any] | Unset = UNSET
        if not isinstance(self.blood, Unset):
            blood = self.blood.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creators is not UNSET:
            field_dict["creators"] = creators
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if id is not UNSET:
            field_dict["id"] = id
        if scenario is not UNSET:
            field_dict["scenario"] = scenario
        if play_info is not UNSET:
            field_dict["play_info"] = play_info
        if blood is not UNSET:
            field_dict["blood"] = blood

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.maker import Maker
        from ..models.play_info_alt import PlayInfoAlt
        from ..models.sherlock_blood import SherlockBlood

        d = dict(src_dict)
        _creators = d.pop("creators", UNSET)
        creators: list[Maker | None] | Unset = UNSET
        if _creators is not UNSET:
            creators = []
            for componentsschemas_sherlock_play_creators_items_item_data in _creators:

                def _parse_componentsschemas_sherlock_play_creators_items_item(
                    data: object,
                ) -> Maker | None:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_maker_type_0 = Maker.from_dict(data)

                        return componentsschemas_maker_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(Maker | None, data)

                componentsschemas_sherlock_play_creators_items_item = (
                    _parse_componentsschemas_sherlock_play_creators_items_item(
                        componentsschemas_sherlock_play_creators_items_item_data
                    )
                )

                creators.append(componentsschemas_sherlock_play_creators_items_item)

        file_name = d.pop("file_name", UNSET)

        file_size = d.pop("file_size", UNSET)

        id = d.pop("id", UNSET)

        scenario = d.pop("scenario", UNSET)

        _play_info = d.pop("play_info", UNSET)
        play_info: PlayInfoAlt | Unset
        if isinstance(_play_info, Unset):
            play_info = UNSET
        else:
            play_info = PlayInfoAlt.from_dict(_play_info)

        _blood = d.pop("blood", UNSET)
        blood: SherlockBlood | Unset
        if isinstance(_blood, Unset):
            blood = UNSET
        else:
            blood = SherlockBlood.from_dict(_blood)

        sherlock_play = cls(
            creators=creators,
            file_name=file_name,
            file_size=file_size,
            id=id,
            scenario=scenario,
            play_info=play_info,
            blood=blood,
        )

        sherlock_play.additional_properties = d
        return sherlock_play

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
