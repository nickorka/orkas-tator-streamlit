"""Domain model for Orka's Tarot Pro.

Python port of the original Android domain package
``com.orka.taropro.domain`` (Card, CardDeck, CardReadingType, Reading).
"""

from .card import Card
from .deck import CardDeck
from .reading import CardReadingType, Reading, SpreadCard

__all__ = ["Card", "CardDeck", "CardReadingType", "Reading", "SpreadCard"]
