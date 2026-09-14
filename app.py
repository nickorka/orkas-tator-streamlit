"""Orka's Tarot Pro — Streamlit edition.

Entry point.  Sets up the page chrome, injects the parchment theme,
initialises session state, renders the sidebar menu (the web
replacement for the Android launcher menu) and routes between pages
via ``st.navigation``.

Run with:
    streamlit run app.py
"""

import streamlit as st

st.set_page_config(
    page_title="Orka's Tarot Pro",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------------ theme
from styles import inject_global_css  # noqa: E402

inject_global_css()

# ------------------------------------------------------------------ state
from state import get_question, init_state  # noqa: E402

init_state()

# ------------------------------------------------------------------ pages
pages = [
    st.Page("views/home.py", title="Ask the Cards", icon=":material/auto_awesome:", default=True),
    st.Page("views/one_card.py", title="One Card", icon=":material/filter_1:"),
    st.Page("views/three_card.py", title="Three Card", icon=":material/filter_3:"),
    st.Page("views/horseshoe.py", title="Horseshoe", icon=":material/architecture:"),
    st.Page("views/celtic_cross.py", title="Celtic Cross", icon=":material/grid_on:"),
    st.Page("views/mirror.py", title="Mirror", icon=":material/flip:"),
    st.Page("views/deck_browse.py", title="Deck Browser", icon=":material/style:"),
    st.Page("views/about.py", title="About & Help", icon=":material/info:"),
]

page = st.navigation(pages)
page.run()

# ------------------------------------------------------------------ sidebar
with st.sidebar:
    st.markdown(
        """
        <div style="text-align:center;margin-bottom:0.2rem;">
          <div style="width:64px;height:64px;margin:0 auto;border-radius:50%;
                      border:2px solid #c9a227;display:flex;align-items:center;justify-content:center;
                      background:linear-gradient(160deg,#7d2f22,#5c1f16);
                      color:#e3c56b;font-size:26px;box-shadow:0 3px 10px rgba(60,40,10,.3);">✦</div>
          <div style="font-family:Cinzel,Georgia,serif;font-weight:700;font-size:1.02rem;
                      color:#5c1f16;margin-top:8px;">Orka's Tarot Pro</div>
          <div style="font-style:italic;font-size:.8rem;color:#6b5741;">Streamlit edition</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="t-ornament" style="margin:0.4rem 0;">· · ✦ · ·</div>',
        unsafe_allow_html=True,
    )

    question = get_question()
    if question:
        st.markdown(
            f'<div class="t-panel" style="padding:.7rem .9rem;font-size:.92rem;">'
            '<b style="font-family:Cinzel,Georgia,serif;font-size:.72rem;'
            'letter-spacing:.12em;color:#7a2e22;">YOUR QUESTION</b><br>'
            f'<span style="font-style:italic;">“{question}”</span></div>',
            unsafe_allow_html=True,
        )
    else:
        st.page_link("views/home.py", label="Set your question first", icon=":material/edit_note:")

    st.markdown(
        '<div class="t-panel" style="padding:.7rem .9rem;font-size:.9rem;">'
        '<b style="font-family:Cinzel,Georgia,serif;font-size:.72rem;letter-spacing:.12em;'
        'color:#7a2e22;">THE DECK</b><br>'
        '78 cards · 22 Major Arcana<br>56 Minor Arcana · upright & reversed'
        '</div>',
        unsafe_allow_html=True,
    )

    st.caption("Switching between spreads reshuffles the deck — "
               "just as the original Android app did.")
