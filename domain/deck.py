"""Card deck — port of ``com.orka.taropro.domain.CardDeck``.

The Android activities called ``taro.cardHelper.cardDeck.shuffle()`` when a
new reading type was entered.  The same behaviour lives here: a 78 card
deck that can be shuffled and dealt from the top.
"""

from __future__ import annotations

import random
from typing import List, Optional

from .card import Card


class CardDeck:
    """A 78-card tarot deck with a draw pile."""

    def __init__(self, cards: Optional[List[Card]] = None) -> None:
        if cards is None:
            # Lazy import avoids the circular module dependency
            from data.tarot_data import build_full_deck
            cards = build_full_deck()
        self._cards: List[Card] = list(cards)
        self._pile: List[Card] = list(self._cards)
        self.shuffled: bool = False

    # ------------------------------------------------------------------ #
    def shuffle(self) -> None:
        """Shuffle the full deck and reset the draw pile (like the original)."""
        random.shuffle(self._pile)
        self.shuffled = True

    def deal(self, count: int) -> List[Card]:
        """Deal ``count`` cards from the top of the pile."""
        if count > len(self._pile):
            count = len(self._pile)
        dealt = self._pile[:count]
        del self._pile[:count]
        return dealt

    def reset(self) -> None:
        """Return every card to the pile (deck becomes complete again)."""
        self._pile = list(self._cards)
        self.shuffled = False

    # ------------------------------------------------------------------ #
    @property
    def cards(self) -> List[Card]:
        return list(self._cards)

    @property
    def remaining(self) -> int:
        return len(self._pile)

    @property
    def size(self) -> int:
        return len(self._cards)
