"""Home page — port of the launcher ``TaroQuestionsActivity``.

Asks the visitor for their question, offers sample focuses, and links
into the five spreads (the role the old main menu played).
"""

import streamlit as st

from components.htmlutil import show_html
from state import get_question, init_state

init_state()

show_html(
    """
    <div class="t-hero">
      <h1>Orka's Tarot Pro</h1>
      <div class="t-tagline">Ask the cards — they answer those who ask clearly</div>
    </div>
    <div class="t-ornament">✦ ─── ❖ ─── ✦</div>
    """
)

show_html(
    """
    <div class="t-panel">
    <p>Welcome, seeker. This is the web edition of <b>Orka's Tarot Pro</b>, ported from
    the original Android application. The ritual is unchanged: hold one question in
    your mind, choose a spread, shuffle the seventy-eight cards, and turn each card
    by hand. Every card can be read upright or reversed, alone or woven into the full
    interpretation that appears once the spread is complete.</p>
    <p>A clear question is the single most important card on the table. Vague questions
    invite vague answers; name what you truly want to know, and choose the spread
    that fits its weight.</p>
    </div>
    """
)

st.markdown("#### Your question")
current = get_question()
question = st.text_area(
    "Focus your mind on a single question.",
    value=current,
    key="home_question",
    height=80,
    placeholder="e.g. What should I know about the path I am currently on?",
)
b1, b2 = st.columns([0.3, 0.7])
if b1.button("Save question", type="primary"):
    st.session_state["question"] = question.strip()
    st.rerun()
if current:
    st.markdown(f"*Saved question:* **{current}**")

st.markdown("#### Need a starting point?")
sample_cols = st.columns(3)
samples = [
    "What should I focus on this month?",
    "What does my heart need right now?",
    "How is my career truly unfolding?",
]
for col, sample in zip(sample_cols, samples):
    with col:
        if st.button(sample, key=f"sample_{sample[:16]}"):
            st.session_state["question"] = sample
            st.rerun()

st.markdown("#### Choose your spread")
show_html(
    """
    <div class="t-panel">
    <table style="width:100%;border-collapse:collapse;font-size:1.02rem;">
      <tr><td style="padding:6px 4px;color:var(--burgundy);font-family:Cinzel,Georgia,serif;white-space:nowrap;"><b>One Card</b></td>
          <td style="padding:6px 4px;">A single focused answer — daily guidance, quick clarity.</td></tr>
      <tr><td style="padding:6px 4px;color:var(--burgundy);font-family:Cinzel,Georgia,serif;white-space:nowrap;"><b>Three Card</b></td>
          <td style="padding:6px 4px;">Past, present, future — the classic narrative arc.</td></tr>
      <tr><td style="padding:6px 4px;color:var(--burgundy);font-family:Cinzel,Georgia,serif;white-space:nowrap;"><b>Horseshoe</b></td>
          <td style="padding:6px 4px;">Seven cards in a lucky arc — a rounded situation reading.</td></tr>
      <tr><td style="padding:6px 4px;color:var(--burgundy);font-family:Cinzel,Georgia,serif;white-space:nowrap;"><b>Celtic Cross</b></td>
          <td style="padding:6px 4px;">The famous ten-card spread for weighty questions.</td></tr>
      <tr><td style="padding:6px 4px;color:var(--burgundy);font-family:Cinzel,Georgia,serif;white-space:nowrap;"><b>Mirror</b></td>
          <td style="padding:6px 4px;">Eleven cards across the glass — self-knowledge and reflection.</td></tr>
    </table>
    </div>
    """
)

nav = st.columns(5)
links = [
    ("views/one_card.py", "One Card"),
    ("views/three_card.py", "Three Card"),
    ("views/horseshoe.py", "Horseshoe"),
    ("views/celtic_cross.py", "Celtic Cross"),
    ("views/mirror.py", "Mirror"),
]
for col, (path, label) in zip(nav, links):
    with col:
        st.page_link(path, label=label, use_container_width=True)

show_html(
    '<div class="t-footer">✦ Orka\'s Tarot Pro — a Streamlit port of the Android original ✦</div>'
)
