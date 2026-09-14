"""Card rendering — placeholder art shared across the app.

The original app resolved card images via ``card_%02d`` drawables; the
drawables were not part of the recovered source, so every card is drawn
as a parchment plate: numeral on top, a typographic emblem in the
middle and the card name as an overlay banner.  One shared burgundy
card-back design is used wherever a card is face down.
"""

from __future__ import annotations

import html
from typing import Optional

import streamlit as st

from components.htmlutil import show_html
from domain.card import Card

SUIT_COLORS = {
    "Major Arcana": "#7a2e22",
    "Wands": "#8a3a2c",
    "Cups": "#2c5a7a",
    "Swords": "#4a5468",
    "Pentacles": "#a87b2e",
}

# size presets: (width, height) in px
SIZES = {
    "mini": (96, 155),
    "spread": (110, 178),
    "detail": (184, 297),
}


def _esc(text: str) -> str:
    return html.escape(text, quote=True)


# --------------------------------------------------------------------- #
# Back
# --------------------------------------------------------------------- #
def card_back_html(size: str = "spread") -> str:
    """The single shared card-back design."""
    w, h = SIZES.get(size, SIZES["spread"])
    return f"""
    <div class="card-frame"><div class="card-inner"><div class="card-flipper">
      <div class="card-back" style="--cw:{w}px;--ch:{h}px;position:relative;">
        <span class="back-corner tl">✧</span>
        <span class="back-corner br">✧</span>
        <div class="back-emblem">✦</div>
      </div>
    </div></div></div>"""


# --------------------------------------------------------------------- #
# Face
# --------------------------------------------------------------------- #
def card_face_html(card: Card, size: str = "spread") -> str:
    """Parchment face plate with numeral, emblem and name overlay."""
    w, h = SIZES.get(size, SIZES["spread"])
    suit_color = SUIT_COLORS.get(card.arcana, "#7a2e22")
    emblem = "✦" if card.is_major else card.suit[0].upper()
    return f"""
    <div class="card-face" style="--cw:{w}px;--ch:{h}px;--suit:{suit_color};">
      <div class="face-numeral">{_esc(card.numeral)}</div>
      <div class="face-emblem">{_esc(emblem)}</div>
      <div class="face-name">{_esc(card.name)}</div>
    </div>"""


# --------------------------------------------------------------------- #
# Slot (badge + card + orientation + label)
# --------------------------------------------------------------------- #
def card_slot_html(
    index: int,
    position_name: str,
    card: Optional[Card] = None,
    is_reversed: bool = False,
    flipped: bool = False,
    animate: bool = False,
    size: str = "spread",
    extra_style: str = "",
    show_label: bool = True,
) -> str:
    """One slot in any spread: back when hidden, face when flipped."""
    badge = f'<div class="pos-badge">{index + 1}</div>' if card is not None else ""
    if not flipped or card is None:
        inner = card_back_html(size)
        label_cls = ""
        label = f"Card {index + 1} · {position_name}"
    else:
        flip_cls = " reversed" if is_reversed else ""
        anim = " flip-in" if animate else ""
        inner = (
            f'<div class="card-frame"><div class="card-inner{flip_cls}{anim}">'
            f'<div class="card-flipper">{card_face_html(card, size)}</div></div></div>'
        )
        label_cls = "flipped"
        label = f"{position_name}"
    label_html = (
        f'<div class="pos-label {label_cls}">{_esc(label)}</div>' if show_label else ""
    )
    rev_badge = (
        '<div class="reversed-badge">Reversed</div>'
        if (flipped and card is not None and is_reversed)
        else ""
    )
    return f"""
    <div class="card-slot" style="{extra_style}">
      {badge}
      {inner}
      {rev_badge}
      {label_html}
    </div>"""


# --------------------------------------------------------------------- #
# Card detail — port of CardActivity
# --------------------------------------------------------------------- #
def render_card_detail(card: Card, is_reversed: bool = False) -> None:
    """The old ``CardActivity`` screen: image, name, meaning, readings."""
    col_img, col_txt = st.columns([0.34, 0.66], gap="medium")

    with col_img:
        orientation_badge = (
            '<div style="text-align:center;margin-top:6px;">'
            '<span class="reversed-badge" style="position:static;display:inline-block;">'
            "Dealt Reversed</span></div>"
            if is_reversed
            else '<div style="text-align:center;margin-top:6px;">'
            '<span class="pos-label flipped" style="display:inline-block;">Dealt Upright</span></div>'
        )
        show_html(
            f'<div style="display:flex;flex-direction:column;align-items:center;">'
            f'<div class="card-frame"><div class="card-inner">'
            f'{card_face_html(card, "detail")}</div></div>{orientation_badge}</div>'
        )

    with col_txt:
        show_html(
            f'<div class="detail-text">'
            f"<h3>{_esc(card.name)}</h3>"
            f'<div class="detail-kw">{_esc(card.keywords)} · {_esc(card.arcana)}</div>'
        )
        show_html(
            '<div class="detail-section"><div class="ds-title">Card Meaning:</div>'
            f"{_esc(card.meaning)}</div>"
        )
        show_html(
            '<div class="detail-section"><div class="ds-title">Upright Reading:</div>'
            f"{_esc(card.upright)}</div>"
        )
        show_html(
            '<div class="detail-section"><div class="ds-title">Reverse Reading:</div>'
            f"{_esc(card.reversed_meaning)}</div>"
        )
        show_html("</div>")
