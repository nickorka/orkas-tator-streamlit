"""Card data assembly — builds the full 78-card deck.

The original Android app resolved drawables as ``card_%02d`` where id 1..22
were the Major Arcana and 23..78 the four suits in order
Wands, Cups, Swords, Pentacles.  The same numbering is preserved here.
"""

from __future__ import annotations

from typing import List

from domain.card import Card
from data.major_arcana import MAJOR_ARCANA
from data.suits_wands import WANDS
from data.suits_cups import CUPS
from data.suits_swords import SWORDS
from data.suits_pentacles import PENTACLES

EXPECTED_DECK_SIZE = 78


def build_full_deck() -> List[Card]:
    """Return all 78 cards in the original ``card_%02d`` id order."""
    cards: List[Card] = []

    for card_id, name, numeral, keywords, meaning, upright, rev in MAJOR_ARCANA:
        cards.append(Card(
            card_id=card_id,
            name=name,
            arcana="Major Arcana",
            rank=numeral,
            keywords=keywords,
            meaning=meaning,
            upright=upright,
            reversed_meaning=rev,
        ))

    for suit, suit_data in (("Wands", WANDS), ("Cups", CUPS),
                            ("Swords", SWORDS), ("Pentacles", PENTACLES)):
        for card_id, rank, keywords, meaning, upright, rev in suit_data:
            cards.append(Card(
                card_id=card_id,
                name=f"{rank} of {suit}",
                arcana=suit,
                rank=rank,
                keywords=keywords,
                meaning=meaning,
                upright=upright,
                reversed_meaning=rev,
            ))

    if len(cards) != EXPECTED_DECK_SIZE:
        raise ValueError(
            f"Deck assembly error: expected {EXPECTED_DECK_SIZE} cards, got {len(cards)}")
    if len({c.card_id for c in cards}) != EXPECTED_DECK_SIZE:
        raise ValueError("Deck assembly error: duplicate card ids detected")

    return cards
