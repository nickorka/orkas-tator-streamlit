"""Spread layout renderer.

Draws the dealt cards in the shape of the chosen spread and provides
the numbered flip buttons that replace the old Android 3D tap-to-flip
interaction.  When every card is face up, the full reading summary
(port of ReadingActivity) unfolds underneath.
"""

from __future__ import annotations

from typing import List, Optional

import streamlit as st

from components.card_view import card_slot_html
from components.htmlutil import show_html
from components.summary import render_summary
from domain.reading import CardReadingType, Reading
from spreads.base import Spread

CARD_W, CARD_H = 110, 178
CC_GAP_X, CC_GAP_Y = 130, 198          # celtic cross grid cell pitch
CC_STAFF_X = 425                        # staff column x offset
CC_STAFF_STEP = 152                     # vertical pitch of the staff stack


# --------------------------------------------------------------------- #
# HTML builders
# --------------------------------------------------------------------- #
def _slot(reading: Reading, spread: Spread, i: int, animate_idx: Optional[int],
          extra_style: str = "", show_label: bool = True) -> str:
    sc = reading.spread_cards[i]
    pos = spread.positions[i]
    return card_slot_html(
        index=i,
        position_name=pos.name,
        card=sc.card,
        is_reversed=sc.is_reversed,
        flipped=sc.flipped,
        animate=(animate_idx == i),
        size="spread",
        extra_style=extra_style,
        show_label=show_label,
    )


def _board(inner: str, canvas_style: str = "") -> str:
    return (
        f'<div class="spread-board"><div class="spread-canvas" style="{canvas_style}">'
        f"{inner}</div></div>"
    )


def _layout_single(reading, spread, animate_idx) -> str:
    inner = _slot(reading, spread, 0, animate_idx)
    return f'<div class="spread-single">{inner}</div>'


def _layout_row(reading, spread, animate_idx) -> str:
    slots = "".join(_slot(reading, spread, i, animate_idx)
                    for i in range(spread.card_count))
    return f'<div class="spread-row">{slots}</div>'


def _layout_arc(reading, spread, animate_idx) -> str:
    slots = []
    for i in range(spread.card_count):
        pos = spread.positions[i]
        style = f"transform:rotate({pos.rotation}deg);margin-bottom:{pos.arc_rise}px;"
        slots.append(_slot(reading, spread, i, animate_idx, extra_style=style))
    return f'<div class="arc-wrap">{"".join(slots)}</div>'


def _layout_cross(reading, spread, animate_idx) -> str:
    slots: List[str] = []
    staff_seen = 0
    for i, pos in enumerate(spread.positions):
        if pos.grid_col <= 3:
            x = (pos.grid_col - 1) * CC_GAP_X
            y = (pos.grid_row - 1) * CC_GAP_Y
            rot = f"transform:rotate({pos.rotation}deg);" if pos.rotation else ""
            z = 3 if pos.rotation else 2
            style = f"left:{x}px;top:{y}px;{rot}z-index:{z};"
        else:
            y = 8 + staff_seen * CC_STAFF_STEP
            staff_seen += 1
            style = f"left:{CC_STAFF_X}px;top:{y}px;z-index:1;"
        slots.append(_slot(reading, spread, i, animate_idx, extra_style=style))
    canvas_w = CC_STAFF_X + CARD_W + 10
    canvas_h = 8 + 3 * CC_STAFF_STEP + CARD_H + 46
    return _board("".join(slots),
                  canvas_style=f"width:{canvas_w}px;height:{canvas_h}px;")


def _layout_mirror(reading, spread, animate_idx) -> str:
    left_idx = {p.mirror_row: i for i, p in enumerate(spread.positions)
                if p.mirror_side == "left"}
    right_idx = {p.mirror_row: i for i, p in enumerate(spread.positions)
                 if p.mirror_side == "right"}
    key_idx = next(i for i, p in enumerate(spread.positions)
                   if p.mirror_side == "key")

    rows_html: List[str] = []
    for row in sorted(left_idx):
        li, ri = left_idx[row], right_idx[row]
        rows_html.append(
            f'<div class="mirror-row">'
            f"{_slot(reading, spread, li, animate_idx)}"
            f'<div class="mirror-glass"></div>'
            f"{_slot(reading, spread, ri, animate_idx)}"
            f"</div>"
        )
    key_html = (
        f'<div class="mirror-key">{_slot(reading, spread, key_idx, animate_idx)}</div>'
    )
    return f'<div class="mirror-board">{"".join(rows_html)}{key_html}</div>'


_LAYOUTS = {
    "single": _layout_single,
    "row": _layout_row,
    "arc": _layout_arc,
    "cross": _layout_cross,
    "mirror": _layout_mirror,
}


# --------------------------------------------------------------------- #
# Legend (for absolute layouts where labels would collide)
# --------------------------------------------------------------------- #
def _render_legend(reading: Reading, spread: Spread) -> None:
    items = []
    for i, pos in enumerate(spread.positions):
        sc = reading.spread_cards[i]
        if sc.flipped:
            items.append(f"<span><b>{i + 1}.</b> {pos.name} — {sc.card.name}</span>")
        else:
            items.append(f'<span class="dim"><b>{i + 1}.</b> {pos.name}</span>')
    show_html(f'<div class="spread-legend">{"".join(items)}</div>')


# --------------------------------------------------------------------- #
# Main entry
# --------------------------------------------------------------------- #
def render_spread(reading: Reading, spread: Spread) -> None:
    """Draw the spread board, flip controls, summary and card inspector."""
    animate_idx = st.session_state.get("last_flipped")

    builder = _LAYOUTS[spread.layout]
    show_html(builder(reading, spread, animate_idx))

    if spread.layout in ("cross", "mirror"):
        _render_legend(reading, spread)

    # ---------------- flip buttons (tap-to-flip port) ----------------
    show_html('<div class="t-ornament">· · ✦ · ·</div>')
    cols = st.columns(spread.card_count)
    for i in range(spread.card_count):
        with cols[i]:
            sc = reading.spread_cards[i]
            label = f"Turn {i + 1}"
            if st.button(label, key=f"flip_{spread.key}_{i}",
                         disabled=sc.flipped,
                         help=f"{spread.positions[i].name}"):
                reading.flip(i)
                st.session_state["last_flipped"] = i
                st.rerun()

    # ---------------- full reading summary (ReadingActivity) ----------
    if reading.all_flipped:
        render_summary(reading, spread)

    # ---------------- inspect a card (CardActivity port) --------------
    flipped_items = [
        (i, sc) for i, sc in enumerate(reading.spread_cards) if sc.flipped
    ]
    if flipped_items:
        show_html('<div class="t-ornament">· · ✦ · ·</div>')
        options = {
            f"Card {i + 1} — {sc.card.name} ({sc.orientation_label})": (i, sc)
            for i, sc in flipped_items
        }
        choice = st.selectbox(
            "Inspect a turned card", list(options.keys()),
            key=f"inspect_{spread.key}",
        )
        i, sc = options[choice]
        render_card_detail_inline(reading, spread, i, sc)
    else:
        st.caption("Turn the cards above to reveal the reading — each card can be "
                   "inspected in detail once face up.")


def render_card_detail_inline(reading: Reading, spread: Spread, i: int, sc) -> None:
    from components.card_view import render_card_detail

    show_html(
        f'<div class="t-panel"><b>{spread.positions[i].name}</b><br>'
        f'<span style="font-style:italic;color:var(--ink-soft);">'
        f"{spread.positions[i].description}</span></div>"
    )
    render_card_detail(sc.card, sc.is_reversed)
