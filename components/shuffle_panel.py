"""Shared deck shuffle widget.

One generic panel used by every spread page (One Card, Three Card,
Horseshoe, Celtic Cross and Mirror).  It mirrors the Android lifecycle:
entering a spread with a different reading type clears the reading,
sets the new type and shuffles the deck (see the original
``onResume()`` implementations), after which the reader shuffles and
deals from this panel.
"""

from __future__ import annotations

import streamlit as st

from components.htmlutil import show_html
from domain.reading import CardReadingType, Reading
from spreads.base import Spread

QUESTIONS_KEY = "question"


def _question_row(reading_key: str) -> None:
    """Compact question editor shown inside the shuffle panel."""
    current = st.session_state.get(QUESTIONS_KEY, "")
    with st.expander("Your question", expanded=(current == "")):
        new_q = st.text_area(
            "Focus your mind on a single question — the cards answer best to clarity.",
            value=current,
            key=f"q_input_{reading_key}",
            height=72,
            placeholder="e.g. What should I focus on in my career this season?",
        )
        c1, c2 = st.columns([0.25, 0.75])
        if c1.button("Save question", key=f"q_save_{reading_key}", type="primary"):
            st.session_state[QUESTIONS_KEY] = new_q.strip()
            st.rerun()
        if current:
            c2.markdown(f"*Current question:* {current}")


def render_shuffle_panel(reading: Reading, spread: Spread) -> None:
    """Deck status + shuffle / deal / clear actions, shared by all spreads."""
    show_html('<div class="t-panel">')
    _question_row(spread.key)

    left, mid = st.columns([0.3, 0.7], gap="large", vertical_alignment="center")

    with left:
        show_html(
            f"""
            <div style="display:flex;justify-content:center;">
              <div class="deck-stack">
                <div class="card-back"></div>
                <div class="card-back"></div>
                <div class="card-back"></div>
                <div class="deck-count">
                  <span class="n">{reading.deck.remaining}</span>
                  <span class="u">REMAIN</span>
                </div>
              </div>
            </div>
            """
        )

    with mid:
        st.markdown(
            f"**{spread.title}** — {spread.tagline}.  \n"
            f"{spread.description}"
        )
        st.caption(
            f"78-card deck · {reading.card_count} of {spread.card_count} cards dealt · "
            f"{reading.flipped_count} turned"
        )

        btn1, btn2, btn3 = st.columns([0.42, 0.33, 0.25])
        if not reading.dealt:
            if btn1.button(
                f"Shuffle & deal {spread.card_count} cards",
                key=f"deal_{spread.key}",
                type="primary",
            ):
                reading.deck.shuffle()
                reading.deal(spread.card_count)
                st.session_state["last_flipped"] = None
                st.rerun()
        else:
            if btn1.button(
                "Reshuffle & redeal", key=f"reshuffle_{spread.key}"
            ):
                reading.deck.reset()
                reading.deck.shuffle()
                reading.spread_cards = []
                reading.deal(spread.card_count)
                st.session_state["last_flipped"] = None
                st.rerun()
            if btn2.button("Turn all cards", key=f"flipall_{spread.key}",
                           disabled=reading.all_flipped):
                reading.flip_all()
                st.session_state["last_flipped"] = None
                st.rerun()
            if btn3.button("Clear spread", key=f"clear_{spread.key}"):
                reading.clear()
                st.session_state["last_flipped"] = None
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)