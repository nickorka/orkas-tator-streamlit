"""Full reading summary — port of ``ReadingActivity``.

Once every card in the spread is face up, this weaves the position
meanings and card interpretations into one flowing, position-by-position
interpretation, closes with a synthesis of the deck's tone (how many
Major Arcana, how many reversals) and the advice of the final card.
"""

from __future__ import annotations

from datetime import date

import streamlit as st

from domain.reading import Reading
from spreads.base import Spread


def _orientation_phrase(is_reversed: bool) -> str:
    return "falls reversed" if is_reversed else "stands upright"


def build_summary(reading: Reading, spread: Spread, question: str) -> str:
    lines: list[str] = []

    # ---------------------------------------------------------- opening
    title = spread.title
    lines.append(f"### The {title} Reading")
    if question:
        lines.append(f"*You asked:* **{question}**")
    lines.append(f"*Cast on* {date.today().strftime('%B %d, %Y')} "
                 f"· *spread:* {spread.title} "
                 f"({spread.card_count} card{'s' if spread.card_count != 1 else ''})")
    lines.append("")

    # ------------------------------------------------- position by position
    lines.append("#### The cards, position by position")
    for i, sc in enumerate(reading.spread_cards):
        pos = spread.positions[i]
        orientation = _orientation_phrase(sc.is_reversed)
        interpretation = sc.card.orientation_reading(sc.is_reversed)
        lines.append(
            f"**{i + 1}. {pos.name} — {sc.card.name}** "
            f"({orientation}).  \n{pos.description} Here, {sc.card.name} "
            f"speaks of {sc.card.keywords.split('·')[0].strip().lower()}: "
            f"{interpretation}"
        )
        lines.append("")

    # --------------------------------------------------------- synthesis
    majors = [sc for sc in reading.spread_cards if sc.card.is_major]
    reversals = [sc for sc in reading.spread_cards if sc.is_reversed]
    lines.append("#### The shape of the reading")
    if len(majors) >= spread.card_count / 2:
        tone = ("Fate dominates this cast — more than half the cards are Major Arcana, "
                "so the situation is being driven by forces larger than daily habit. "
                "Work *with* the current rather than against it.")
    elif majors:
        tone = (f"{len(majors)} Major Arcana anchor the cast while the remaining "
                f"minor cards fill in the everyday detail: destiny sets the theme, "
                f"but your daily choices still steer the road.")
    else:
        tone = ("No Major Arcana appear — this is a reading of the everyday, where "
                "ordinary decisions, habits and conversations carry the outcome.")
    lines.append(tone)

    if len(reversals) >= spread.card_count / 2 and spread.card_count > 1:
        lines.append("Half or more of the cards arrive reversed: much of this matter is "
                     "internal — resistance, delays and unwritten feelings. Progress "
                     "begins with honest inner work before outer action.")
    elif reversals:
        lines.append(f"{len(reversals)} of {spread.card_count} cards are reversed, "
                     "marking the corners of the situation where energy is held back or "
                     "turned inward; treat those positions with extra patience.")
    else:
        if spread.card_count > 1:
            lines.append("Every card stands upright: the energy of the matter flows "
                         "outward and unblocked — a good moment to act.")

    # ------------------------------------------------------ final advice
    final_sc = reading.spread_cards[-1]
    final_pos = spread.positions[-1]
    lines.append(
        f"**In closing, {final_pos.name}** — the {final_sc.card.name} "
        f"{_orientation_phrase(final_sc.is_reversed)}: "
        f"{final_sc.card.orientation_reading(final_sc.is_reversed)}"
    )
    return "\n".join(lines)


def render_summary(reading: Reading, spread: Spread) -> None:
    question = st.session_state.get("question", "")
    st.markdown('<div class="t-ornament">· · ✦ · ·</div>', unsafe_allow_html=True)
    with st.expander("Full Reading Interpretation", expanded=True):
        st.markdown(build_summary(reading, spread, question))
