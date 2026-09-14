"""Deck Browser — port of ``DeckBrowseActivity``.

Lets the visitor filter and browse all seventy-eight cards of the
deck and open any card in the full detail view (name, meaning,
upright reading, reverse reading) that ``CardActivity`` provided.
"""

from __future__ import annotations

import html

import streamlit as st

from components.card_view import SUIT_COLORS, card_face_html, render_card_detail
from components.htmlutil import show_html
from data.tarot_data import build_full_deck
from state import init_state

init_state()

show_html("""
    <div class="t-hero">
      <h1>Deck Browser</h1>
      <div class="t-tagline">All seventy-eight cards, face up and at leisure</div>
    </div>
    <div class="t-ornament">✦ ─── ❖ ─── ✦</div>
    """)

deck = build_full_deck()

# ------------------------------------------------------------------ filter
st.radio(
    "Filter the deck",
    options=["All", "Major Arcana", "Wands", "Cups", "Swords", "Pentacles"],
    key="deck_browse_filter",
    horizontal=True,
)
flt = st.session_state["deck_browse_filter"]

if flt == "All":
    cards = deck
elif flt == "Major Arcana":
    cards = [c for c in deck if c.is_major]
else:
    cards = [c for c in deck if c.suit == flt]

st.caption(f"{len(cards)} cards shown")

# ------------------------------------------------------------------ grid
faces = []
for c in cards:
    color = SUIT_COLORS.get(c.arcana, "#7a2e22")
    faces.append(
        f'<div style="text-align:center;">{card_face_html(c, "mini")}</div>'
    )
show_html(f'<div class="deck-grid">{"".join(faces)}</div>')

# ------------------------------------------------------------------ detail
show_html('<div class="t-ornament">· · ✦ · ·</div>')
st.markdown("#### Inspect a card")

by_name = {c.name: c for c in deck}
sorted_names = sorted(by_name)
choice = st.selectbox("Card", sorted_names, index=None,
                      placeholder="Choose a card to read its full meaning…")
if choice:
    render_card_detail(by_name[choice], is_reversed=False)
