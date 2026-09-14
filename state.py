"""Session state helpers.

The Android app kept a global ``TaroApplication`` object holding the
current deck and reading.  In Streamlit the same role is played by
``st.session_state``; the function :func:`ensure_reading` is a direct
port of the spread activities' ``onResume()`` logic:

    switch (taro.reading.getReadingType()) {
        case CELTIC_CROSS: break;          // same spread: keep going
        default:
            taro.reading.clear();          // different spread: wipe
            taro.reading.setReadingType(...);
            taro.cardHelper.cardDeck.shuffle();
    }
"""

from __future__ import annotations

import streamlit as st

from domain.reading import CardReadingType, Reading

STATE_KEYS = {
    "question": "",
    "reading": None,
    "last_flipped": None,
    "deck_browse_filter": "All",
}


def init_state() -> None:
    for key, default in STATE_KEYS.items():
        if key not in st.session_state:
            st.session_state[key] = default


def get_question() -> str:
    return st.session_state.get("question", "") or ""


def ensure_reading(reading_type: CardReadingType) -> Reading:
    """Port of the spread activities' ``onResume()`` reading check."""
    reading: Reading | None = st.session_state.get("reading")
    if reading is None or reading.reading_type != reading_type:
        from domain.deck import CardDeck

        deck = CardDeck()
        deck.shuffle()
        reading = Reading(reading_type=reading_type, deck=deck)
        st.session_state["reading"] = reading
        st.session_state["last_flipped"] = None
    return reading
