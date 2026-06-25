from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recommended_card import RecommendedCard


T = TypeVar("T", bound="ChallengeRecommendedResponse")


@_attrs_define
class ChallengeRecommendedResponse:
    """Schema definition for Challenge Recommended Response

    Attributes:
        card1 (RecommendedCard | Unset): Schema definition for Recommended Card
        card2 (RecommendedCard | Unset): Schema definition for Recommended Card
        state (list[None | str] | None | Unset):
    """

    card1: RecommendedCard | Unset = UNSET
    card2: RecommendedCard | Unset = UNSET
    state: list[None | str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card1: dict[str, Any] | Unset = UNSET
        if not isinstance(self.card1, Unset):
            card1 = self.card1.to_dict()

        card2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.card2, Unset):
            card2 = self.card2.to_dict()

        state: list[None | str] | None | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, list):
            state = []
            for componentsschemas_string_array_type_0_item_data in self.state:
                componentsschemas_string_array_type_0_item: None | str
                componentsschemas_string_array_type_0_item = (
                    componentsschemas_string_array_type_0_item_data
                )
                state.append(componentsschemas_string_array_type_0_item)

        else:
            state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if card1 is not UNSET:
            field_dict["card1"] = card1
        if card2 is not UNSET:
            field_dict["card2"] = card2
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recommended_card import RecommendedCard

        d = dict(src_dict)
        _card1 = d.pop("card1", UNSET)
        card1: RecommendedCard | Unset
        if isinstance(_card1, Unset):
            card1 = UNSET
        else:
            card1 = RecommendedCard.from_dict(_card1)

        _card2 = d.pop("card2", UNSET)
        card2: RecommendedCard | Unset
        if isinstance(_card2, Unset):
            card2 = UNSET
        else:
            card2 = RecommendedCard.from_dict(_card2)

        def _parse_state(data: object) -> list[None | str] | None | Unset:
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

        state = _parse_state(d.pop("state", UNSET))

        challenge_recommended_response = cls(
            card1=card1,
            card2=card2,
            state=state,
        )

        challenge_recommended_response.additional_properties = d
        return challenge_recommended_response

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
