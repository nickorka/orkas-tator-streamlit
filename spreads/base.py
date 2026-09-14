"""Spread definitions.

Each spread mirrors one Android spread activity (OneCardActivity,
ThreeCardActivity, HorseshoeActivity, CelticCrossActivity — the original
layout used 7 grid rows — and MirrorActivity, which used 11 grid rows).
A spread declares its positions, their meanings and a layout kind that
the web renderer uses to draw the cards.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from domain.reading import CardReadingType


@dataclass(frozen=True)
class SpreadPosition:
    """One slot in a spread."""

    index: int                 # 0-based deal order
    name: str                  # e.g. "The Heart of the Matter"
    description: str           # what this position asks the card

    # --- optional layout hints (used by the renderers) ----------------
    grid_col: Optional[int] = None
    grid_row: Optional[int] = None
    rotation: float = 0.0      # degrees (crossing card = 90)
    arc_rise: float = 0.0      # px the card is lifted in arc layouts
    mirror_row: Optional[int] = None
    mirror_side: Optional[str] = None   # "left" | "right" | "key"


@dataclass(frozen=True)
class Spread:
    """A complete spread definition."""

    key: str                              # url-ish key, e.g. "celtic-cross"
    title: str
    tagline: str
    reading_type: CardReadingType
    card_count: int
    layout: str                           # single | row | arc | cross | mirror
    positions: List[SpreadPosition] = field(default_factory=list)
    description: str = ""

    @property
    def position_names(self) -> List[str]:
        return [p.name for p in self.positions]


def _build(key, title, tagline, reading_type, layout, description, position_specs):
    positions = [SpreadPosition(index=i, name=n, description=d, **hints)
                 for i, (n, d, hints) in enumerate(position_specs)]
    return Spread(key=key, title=title, tagline=tagline, reading_type=reading_type,
                  card_count=len(positions), layout=layout, positions=positions,
                  description=description)


def _default_spreads() -> Dict[CardReadingType, Spread]:
    spreads: Dict[CardReadingType, Spread] = {}

    # ---------------------------------------------------------- one card
    spreads[CardReadingType.ONE_CARD] = _build(
        "one-card", "One Card", "A single, focused answer",
        CardReadingType.ONE_CARD, "single",
        "The quickest reading in the app: one card drawn for one question. Ideal for daily "
        "guidance or a simple yes-or-no nudge in the right direction.",
        [("The Answer", "The single message the cards hold for your question right now.", {})],
    )

    # ------------------------------------------------------- three cards
    spreads[CardReadingType.THREE_CARD] = _build(
        "three-card", "Three Card", "Past, present and future",
        CardReadingType.THREE_CARD, "row",
        "A classic narrative reading: the root of the matter, where things stand now and "
        "where the current path leads if nothing changes.",
        [
            ("The Past", "Roots and events that shaped the situation.", {}),
            ("The Present", "The current state of affairs and its dominant energy.", {}),
            ("The Future", "Where the present path is leading.", {}),
        ],
    )

    # --------------------------------------------------------- horseshoe
    horseshoe_offsets = [64, 26, 6, 0, 6, 26, 64]
    horseshoe_rots = [-16, -11, -6, 0, 6, 11, 16]
    horseshoe_positions = [
        ("The Past", "Events and influences that brought you here.", {}),
        ("The Present", "Where you stand at this moment.", {}),
        ("Hidden Influences", "Forces working beneath the surface.", {}),
        ("The Querent", "You — your stance and your role in events.", {}),
        ("Attitudes of Others", "How the people around you affect the matter.", {}),
        ("What To Do", "The course of action the cards recommend.", {}),
        ("Likely Outcome", "Where things head if the advice is followed.", {}),
    ]
    spreads[CardReadingType.HORSESHOE] = _build(
        "horseshoe", "Horseshoe", "Seven cards fanned in a lucky arc",
        CardReadingType.HORSESHOE, "arc",
        "Seven cards arranged in the shape of a horseshoe. It gives a rounded view of the "
        "situation — past, present and hidden forces — and ends with practical advice and a "
        "likely outcome.",
        [(n, d, {"arc_rise": horseshoe_offsets[i], "rotation": horseshoe_rots[i]})
         for i, (n, d, _h) in enumerate(horseshoe_positions)],
    )

    # ----------------------------------------------------- celtic cross
    cc_positions = [
        ("The Heart of the Matter", "The core of the situation as it truly is.",
         {"grid_col": 2, "grid_row": 2}),
        ("The Crossing", "What crosses you — the helping or hindering force.",
         {"grid_col": 2, "grid_row": 2, "rotation": 90.0}),
        ("The Foundation", "Subconscious roots; the ground you stand on.",
         {"grid_col": 2, "grid_row": 3}),
        ("The Recent Past", "What is just now passing out of influence.",
         {"grid_col": 1, "grid_row": 2}),
        ("The Crown", "Conscious goal, ideal, or what crowns the matter.",
         {"grid_col": 2, "grid_row": 1}),
        ("The Near Future", "What approaches next along the current path.",
         {"grid_col": 3, "grid_row": 2}),
        ("Yourself", "How you see yourself in this matter.", {"grid_col": 4, "grid_row": 1}),
        ("The Environment", "People and surroundings shaping events.", {"grid_col": 4, "grid_row": 2}),
        ("Hopes and Fears", "What you long for and what you dread.", {"grid_col": 4, "grid_row": 3}),
        ("The Outcome", "The culmination if the path holds.", {"grid_col": 4, "grid_row": 4}),
    ]
    spreads[CardReadingType.CELTIC_CROSS] = _build(
        "celtic-cross", "Celtic Cross", "The classic ten-card reading",
        CardReadingType.CELTIC_CROSS, "cross",
        "The most famous tarot spread: a cross of six cards that maps the heart of the matter, "
        "its challenge and its trajectory, plus a staff of four cards that reveals you, your "
        "world and the likely outcome.",
        [(n, d, hints) for n, d, hints in cc_positions],
    )

    # ------------------------------------------------------------- mirror
    mirror_positions = [
        ("How You See Yourself", "Your self-image at the heart of the question.", {"side": "left", "row": 1}),
        ("How Others See You", "The reflection the world sends back.", {"side": "right", "row": 1}),
        ("What You Reveal", "The face you choose to show.", {"side": "left", "row": 2}),
        ("What You Conceal", "What stays behind the glass.", {"side": "right", "row": 2}),
        ("Your Strength", "What carries you forward.", {"side": "left", "row": 3}),
        ("Your Challenge", "What tests and tempers you.", {"side": "right", "row": 3}),
        ("What Uplifts You", "The light you can always draw on.", {"side": "left", "row": 4}),
        ("What Weighs on You", "The shadow you keep carrying.", {"side": "right", "row": 4}),
        ("The Path Behind", "What made you who you are.", {"side": "left", "row": 5}),
        ("The Path Ahead", "Where the reflection is leading.", {"side": "right", "row": 5}),
        ("The Mirror's Truth", "The synthesis — what the whole reflection says.", {"side": "key", "row": 6}),
    ]
    mirror_specs = [
        (n, d, {"mirror_row": h["row"], "mirror_side": h["side"]})
        for n, d, h in mirror_positions
    ]
    spreads[CardReadingType.MIRROR] = _build(
        "mirror", "Mirror", "Eleven cards reflected across the glass",
        CardReadingType.MIRROR, "mirror",
        "A spread of self-knowledge laid out across an imaginary mirror. Five paired positions "
        "reflect inner truth against outer appearance, and a single key card condenses the "
        "whole reflection into one message.",
        mirror_specs,
    )

    return spreads


SPREADS: Dict[CardReadingType, Spread] = _default_spreads()


def get_spread(reading_type: CardReadingType) -> Spread:
    return SPREADS[reading_type]


def spread_by_key(key: str) -> Optional[Spread]:
    for spread in SPREADS.values():
        if spread.key == key:
            return spread
    return None
