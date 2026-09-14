"""Card entity — port of ``com.orka.taropro.domain.Card``.

The original Java card exposed: ``getCardId()`` (used for the
``card_%02d`` drawable lookup), ``getName()``, ``getMeaning()`` and
``setDirect(boolean)`` / ``getReading()`` which returned either the
upright or the reversed interpretation.  The same fields and API are
kept here so the port stays recognizable next to the Java sources.
"""

from __future__ import annotations

from dataclasses import dataclass, field

SUITS = ("Wands", "Cups", "Swords", "Pentacles")
ARCANA_MAJOR = "Major Arcana"


@dataclass(frozen=True)
class Card:
    """A single tarot card out of the 78-card deck."""

    card_id: int                 # 1..78 -> drawable "card_%02d" in the Android app
    name: str                    # e.g. "The Fool", "Ace of Wands"
    arcana: str                  # "Major Arcana" or one of SUITS
    rank: str                    # roman numeral for majors, "Ace".."King" for minors
    keywords: str                # short keyword line
    meaning: str                 # short meaning (original ``getMeaning()``)
    upright: str                 # upright interpretation
    reversed_meaning: str        # reversed interpretation

    # ------------------------------------------------------------------ #
    # Parity helpers with the original Java API
    # ------------------------------------------------------------------ #
    @property
    def image_ref(self) -> str:
        """Original drawable resource name, e.g. ``card_07``."""
        return f"card_{self.card_id:02d}"

    def reading(self, direct: bool = True) -> str:
        """Port of ``setDirect(...)`` + ``getReading()``.

        Because the Streamlit cards are shared singletons we never mutate
        stored state; the orientation is passed explicitly instead.
        """
        return self.upright if direct else self.reversed_meaning

    # ------------------------------------------------------------------ #
    # Convenience properties
    # ------------------------------------------------------------------ #
    @property
    def is_major(self) -> bool:
        return self.arcana == ARCANA_MAJOR

    @property
    def suit(self) -> str | None:
        return None if self.is_major else self.arcana

    @property
    def numeral(self) -> str:
        """Display numeral: roman numerals for majors, rank for minors."""
        return self.rank

    def orientation_reading(self, is_reversed: bool) -> str:
        return self.reversed_meaning if is_reversed else self.upright
