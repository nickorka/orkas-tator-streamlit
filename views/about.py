"""About & Help."""

import streamlit as st

from components.htmlutil import show_html

show_html(
    """
    <div class="t-hero">
      <h1>About</h1>
      <div class="t-tagline">Orka's Tarot Pro — from Android to the web</div>
    </div>
    <div class="t-ornament">✦ ─── ❖ ─── ✦</div>
    """
)

show_html(
    """
    <div class="t-panel">
    <p><b>Orka's Tarot Pro</b> began life as an Android application
    (<i>com.orka.taropro</i>, v1.0.1) with five spreads, a browsable deck and a
    three-dimensional card flip animation. This edition is a faithful Python port of
    that application to <b>Streamlit</b>: the same five spreads, the same 78-card deck
    with upright and reversed readings, and the same reading flow — ask a question,
    shuffle, deal face-down cards, turn them one by one, then read the full
    interpretation.</p>
    <p>The original card artwork and the Google Ads / TapForTap integrations were not
    part of the recovered sources and are intentionally omitted. Cards are drawn as
    typographic parchment plates — one shared burgundy card back, a numeral, an emblem
    and the card name as an overlay banner.</p>
    </div>
    """
)

st.markdown("#### How to read the cards")
st.markdown(
    """
    1. **Ask a clear question** on the *Ask the Cards* page — one focus, no double-barrelled questions.
    2. **Choose a spread** from the sidebar. Entering a different spread reshuffles the deck, exactly as the original app did.
    3. **Shuffle & deal** inside the reading panel. Half the drawn cards may appear reversed — the deck honours both polarities.
    4. **Turn each card** with its numbered button. Turned cards can be inspected in detail at any time.
    5. Once the last card is face up, the **full reading interpretation** unfolds beneath the spread, position by position, ending with a synthesis of the deck's overall tone.
    """
)

st.markdown("#### Android activity → Streamlit page")
show_html(
    """
    <div class="t-panel">
    <table style="width:100%;border-collapse:collapse;font-size:0.98rem;">
      <tr style="font-family:Cinzel,Georgia,serif;color:var(--burgundy-deep);"><th style="text-align:left;padding:4px;">Android activity</th><th style="text-align:left;padding:4px;">Streamlit page</th></tr>
      <tr><td style="padding:3px 4px;">TaroQuestionsActivity <i>(launcher)</i></td><td style="padding:3px 4px;">Ask the Cards</td></tr>
      <tr><td style="padding:3px 4px;">OneCardActivity</td><td style="padding:3px 4px;">One Card</td></tr>
      <tr><td style="padding:3px 4px;">ThreeCardActivity</td><td style="padding:3px 4px;">Three Card</td></tr>
      <tr><td style="padding:3px 4px;">HorseshoeActivity</td><td style="padding:3px 4px;">Horseshoe</td></tr>
      <tr><td style="padding:3px 4px;">CelticCrossActivity</td><td style="padding:3px 4px;">Celtic Cross</td></tr>
      <tr><td style="padding:3px 4px;">MirrorActivity</td><td style="padding:3px 4px;">Mirror</td></tr>
      <tr><td style="padding:3px 4px;">CardActivity</td><td style="padding:3px 4px;">Card detail panels / Deck Browser</td></tr>
      <tr><td style="padding:3px 4px;">DeckBrowseActivity</td><td style="padding:3px 4px;">Deck Browser</td></tr>
      <tr><td style="padding:3px 4px;">ReadingActivity</td><td style="padding:3px 4px;">Full Reading Interpretation section</td></tr>
      <tr><td style="padding:3px 4px;">Flip3dAnimation / SwapViews</td><td style="padding:3px 4px;">CSS <i>flipIn</i> keyframes (rotateY −90°→0°, 500 ms)</td></tr>
      <tr><td style="padding:3px 4px;">AdActivity / TapForTapActivity</td><td style="padding:3px 4px;">— intentionally not ported —</td></tr>
    </table>
    </div>
    """
)

show_html('<div class="t-footer">✦ The cards do not predict; they illuminate. ✦</div>')
