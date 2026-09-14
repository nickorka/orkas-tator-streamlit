"""Reading state — port of ``com.orka.taropro.domain.Reading`` and
``com.orka.taropro.domain.CardReadingType``.

The original enum held the five spread types (``ONE_CARD``, ``THREE_CARD``,
``HORSESHOE``, ``CELTIC_CROSS``, ``MIRROR``).  Each spread activity's
``onResume()`` compared ``taro.reading.getReadingType()`` with its own type
and, when they differed, cleared the reading, set the new type and
shuffled the deck.  ``Reading`` mirrors that lifecycle.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from .card import Card
from .deck import CardDeck


class CardReadingType(str, Enum):
    """Port of the original ``CardReadingType`` enum."""

    ONE_CARD = "ONE_CARD"
    THREE_CARD = "THREE_CARD"
    HORSESHOE = "HORSESHOE"
    CELTIC_CROSS = "CELTIC_CROSS"
    MIRROR = "MIRROR"


REVERSAL_CHANCE = 0.5  # half of the drawn cards may appear reversed


@dataclass
class SpreadCard:
    """A card as it sits in a spread: orientation + flip state."""

    card: Card
    is_reversed: bool = False
    flipped: bool = False
    position_index: int = 0

    @property
    def orientation_label(self) -> str:
        return "Reversed" if self.is_reversed else "Upright"


@dataclass
class Reading:
    """The in-progress reading (deck + dealt cards for one spread)."""

    reading_type: CardReadingType
    deck: CardDeck = field(default_factory=CardDeck)
    spread_cards: List[SpreadCard] = field(default_factory=list)

    # ------------------------------------------------------------------ #
    def clear(self) -> None:
        """Port of ``Reading.clear()`` — drop dealt cards, reset deck."""
        self.spread_cards = []
        self.deck.reset()

    def set_reading_type(self, reading_type: CardReadingType) -> None:
        """Port of ``Reading.setReadingType(...)``."""
        self.clear()
        self.reading_type = reading_type

    # ------------------------------------------------------------------ #
    def deal(self, count: int) -> List[SpreadCard]:
        """Deal ``count`` cards from the shuffled deck into the spread."""
        if self.spread_cards:
            return list(self.spread_cards)
        cards = self.deck.deal(count)
        self.spread_cards = [
            SpreadCard(
                card=card,
                is_reversed=random.random() < REVERSAL_CHANCE,
                flipped=False,
                position_index=i,
            )
            for i, card in enumerate(cards)
        ]
        return list(self.spread_cards)

    def flip(self, index: int) -> None:
        """Turn one card face up (the old 3D flip animation's trigger)."""
        if 0 <= index < len(self.spread_cards):
            self.spread_cards[index].flipped = True

    def flip_all(self) -> None:
        for sc in self.spread_cards:
            sc.flipped = True

    # ------------------------------------------------------------------ #
    @property
    def dealt(self) -> bool:
        return bool(self.spread_cards)

    @property
    def card_count(self) -> int:
        return len(self.spread_cards)

    @property
    def all_flipped(self) -> bool:
        return bool(self.spread_cards) and all(sc.flipped for sc in self.spread_cards)

    @property
    def flipped_count(self) -> int:
        return sum(1 for sc in self.spread_cards if sc.flipped)
