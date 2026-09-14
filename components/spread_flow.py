"""Shared spread page flow.

Every spread page (One Card, Three Card, Horseshoe, Celtic Cross,
Mirror) is a thin wrapper around :func:`run_spread_flow`, exactly as
each Android spread activity was a thin subclass of
``BaseSpreadActivity``.
"""

from __future__ import annotations

import streamlit as st

from components.htmlutil import show_html
from components.shuffle_panel import render_shuffle_panel
from components.spread_layout import render_spread
from domain.reading import CardReadingType
from spreads.base import get_spread
from state import ensure_reading, get_question


def run_spread_flow(reading_type: CardReadingType) -> None:
    spread = get_spread(reading_type)
    reading = ensure_reading(reading_type)

    show_html(
        f'<div class="t-hero"><h1>{spread.title}</h1>'
        f'<div class="t-tagline">{spread.tagline}</div></div>'
        '<div class="t-ornament">✦ ─── ❖ ─── ✦</div>'
    )

    question = get_question()
    if question:
        show_html(f'<div class="t-sub">“{question}”</div>')
    else:
        st.caption("No question has been asked yet — visit *Ask the Cards* in the menu, "
                   "or set one inside the panel below. A focused question sharpens any reading.")

    render_shuffle_panel(reading, spread)
    show_html('<div class="t-ornament">· · ✦ · ·</div>')

    if reading.dealt:
        render_spread(reading, spread)
    else:
        show_html(
            '<div class="t-panel" style="text-align:center;font-style:italic;color:var(--ink-soft);">'
            "The deck is shuffled and waiting. When you are ready, deal the cards — "
            "each one starts face down and is turned by hand, one question at a time."
            "</div>"
        )
