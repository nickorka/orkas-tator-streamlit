"""Global visual theme — "Elegant Parchment".

Cream parchment ground, burgundy & bronze accents, vintage print
typography.  The CSS below is injected once by ``app.py`` via
``inject_global_css()`` and is shared by every view.
"""

BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&display=swap');

:root {
  --parchment: #f4ead2;
  --parchment-light: #faf3e0;
  --parchment-deep: #e9dbb9;
  --ink: #3b2a1a;
  --ink-soft: #6b5741;
  --ink-faint: #8a7a63;
  --burgundy: #7a2e22;
  --burgundy-deep: #5c1f16;
  --bronze: #a87b2e;
  --bronze-soft: #c2a368;
  --gold: #c9a227;
  --gold-light: #e3c56b;
}

/* ------------------------------------------------------------------ */
/* Streamlit chrome                                                    */
/* ------------------------------------------------------------------ */
.stApp {
  background:
    radial-gradient(1400px 900px at 15% -5%, rgba(250, 243, 224, 0.9) 0%, rgba(250,243,224,0) 60%),
    radial-gradient(1200px 800px at 110% 110%, rgba(233, 219, 185, 0.9) 0%, rgba(233,219,185,0) 55%),
    linear-gradient(160deg, #f6eeda 0%, #f2e6c8 55%, #eddfba 100%);
  color: var(--ink);
}
h1, h2, h3, h4 { color: var(--burgundy-deep) !important; font-family: 'Cinzel', Georgia, 'Times New Roman', serif !important; letter-spacing: 0.02em; }
p, li, span, td, th { font-family: 'EB Garamond', Georgia, 'Times New Roman', serif; }
a { color: var(--burgundy) !important; }
hr { border: none; border-top: 1px solid rgba(168, 123, 46, 0.35) !important; }
section[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #f8f1de 0%, #efe2c4 100%);
  border-right: 1px solid #d8c69a;
}
section[data-testid="stSidebar"] * { color: var(--ink) !important; }

/* Streamlit buttons: parchment chips with bronze trim */
.stButton > button, .stDownloadButton > button, .stForm button {
  background: linear-gradient(180deg, #fdf8ea 0%, #f0e3c2 100%);
  color: var(--burgundy-deep);
  border: 1px solid #b99a4e;
  border-radius: 10px;
  font-family: 'Cinzel', Georgia, serif;
  font-weight: 600;
  letter-spacing: 0.04em;
  transition: all 0.25s ease;
  box-shadow: 0 1px 3px rgba(90, 60, 20, 0.15);
}
.stButton > button:hover, .stDownloadButton > button:hover {
  border-color: var(--burgundy);
  color: var(--burgundy);
  box-shadow: 0 4px 12px rgba(122, 46, 34, 0.22);
  transform: translateY(-1px);
}
.stButton > button[kind="primary"] {
  background: linear-gradient(180deg, #8a3a2c 0%, #5c1f16 100%);
  color: #f8ecd2;
  border-color: var(--burgundy-deep);
}
.stButton > button[kind="primary"]:hover { color: #fff6e0; box-shadow: 0 5px 14px rgba(92, 31, 22, 0.4); }
.stButton > button:disabled { opacity: 0.45; transform: none; }

/* Streamlit inputs on parchment */
.stTextInput input, .stTextArea textarea, .stSelectbox > div > div {
  background: rgba(255, 252, 240, 0.9) !important;
  color: var(--ink) !important;
  border: 1px solid #c9b584 !important;
  border-radius: 8px !important;
  font-family: 'EB Garamond', Georgia, serif !important;
  font-size: 1.02rem !important;
}
.stTextInput input:focus, .stTextArea textarea:focus { border-color: var(--bronze) !important; box-shadow: 0 0 0 2px rgba(168,123,46,.25) !important; }

/* Streamlit expanders / radio */
details[data-testid="stExpander"], details[data-testid="stExpander"] summary {
  background: rgba(255, 252, 240, 0.65);
  border-color: #d8c69a;
  font-family: 'EB Garamond', Georgia, serif;
}
div[role="radiogroup"] label { font-family: 'EB Garamond', Georgia, serif; color: var(--ink); }

/* ------------------------------------------------------------------ */
/* Headings & ornaments                                                */
/* ------------------------------------------------------------------ */
.t-hero { text-align: center; margin: 0.4rem 0 0.2rem 0; }
.t-hero h1 {
  font-size: 2.35rem; margin-bottom: 0.1rem;
  text-shadow: 0 1px 0 rgba(255,255,255,.6);
}
.t-hero .t-tagline { font-style: italic; color: var(--ink-soft); font-size: 1.12rem; }
.t-ornament {
  text-align: center; color: var(--bronze); font-size: 0.95rem;
  letter-spacing: 0.55em; margin: 0.35rem 0 0.9rem 0; user-select: none;
}
.t-sub { text-align: center; color: var(--ink-soft); font-style: italic; }

.t-panel {
  background: rgba(255, 252, 240, 0.72);
  border: 1px solid #d8c69a;
  border-radius: 14px;
  padding: 1.1rem 1.4rem;
  box-shadow: 0 2px 14px rgba(90, 60, 20, 0.08);
}
.t-quote { border-left: 3px solid var(--bronze-soft); padding: 0.4rem 1rem; font-style: italic; color: var(--ink-soft); }

/* ------------------------------------------------------------------ */
/* Cards                                                               */
/* ------------------------------------------------------------------ */
.card-slot { position: relative; text-align: center; }
.card-frame { perspective: 900px; display: inline-block; }
.card-inner { position: relative; transform-style: preserve-3d; }

/* Shared card back — the one "image" used everywhere */
.card-back {
  width: var(--cw, 110px); height: var(--ch, 178px);
  border-radius: 10px;
  background:
    radial-gradient(circle at 50% 50%, rgba(227,197,107,0.16) 0%, rgba(227,197,107,0) 62%),
    repeating-linear-gradient(45deg, rgba(227,197,107,0.07) 0 6px, rgba(0,0,0,0) 6px 12px),
    linear-gradient(160deg, #7d2f22 0%, #5c1f16 100%);
  border: 2px solid var(--gold-light);
  box-shadow: inset 0 0 0 3px #5c1f16, inset 0 0 0 4px rgba(227,197,107,0.75), 0 6px 16px rgba(60, 40, 10, 0.3);
  display: flex; align-items: center; justify-content: center;
}
.card-back .back-emblem {
  width: 46%; aspect-ratio: 1; border-radius: 50%;
  border: 1.5px solid rgba(227,197,107,0.8);
  display: flex; align-items: center; justify-content: center;
  color: var(--gold-light); font-size: calc(var(--cw, 110px) * 0.24);
  background: radial-gradient(circle, rgba(227,197,107,0.14) 0%, rgba(227,197,107,0) 70%);
  text-shadow: 0 1px 4px rgba(0,0,0,0.4);
}
.card-back .back-corner {
  position: absolute; color: rgba(227,197,107,0.65);
  font-size: calc(var(--cw, 110px) * 0.13);
}
.card-back .back-corner.tl { top: 4px; left: 7px; }
.card-back .back-corner.br { bottom: 4px; right: 7px; }

/* Card face — parchment plate with name overlay */
.card-face {
  width: var(--cw, 110px); height: var(--ch, 178px);
  border-radius: 10px;
  background: linear-gradient(170deg, #fdf8ea 0%, #f6ecd0 70%, #efe0bc 100%);
  border: 2px solid var(--gold);
  box-shadow: inset 0 0 0 3px rgba(253, 248, 234, 1), inset 0 0 0 4px rgba(201, 162, 39, 0.8), 0 6px 16px rgba(60, 40, 10, 0.25);
  display: flex; flex-direction: column; align-items: center; justify-content: space-between;
  overflow: hidden; position: relative;
}
.card-face .face-numeral {
  font-family: 'Cinzel', Georgia, serif; font-weight: 700;
  color: var(--bronze); font-size: calc(var(--cw, 110px) * 0.17);
  padding-top: 7px; line-height: 1;
}
.card-face .face-emblem {
  flex: 1; display: flex; align-items: center; justify-content: center;
  font-size: calc(var(--cw, 110px) * 0.42); color: var(--suit, var(--burgundy));
  opacity: 0.9; text-shadow: 0 1px 0 rgba(255,255,255,0.8);
}
.card-face .face-name {
  width: 100%; text-align: center;
  font-family: 'Cinzel', Georgia, serif; font-weight: 600;
  font-size: calc(var(--cw, 110px) * 0.105);
  line-height: 1.15; color: var(--burgundy-deep);
  background: linear-gradient(180deg, rgba(233, 219, 185, 0) 0%, rgba(233, 219, 185, 0.55) 30%);
  padding: 3px 2px 6px 2px; letter-spacing: 0.02em;
}

/* Reversal — the face itself is printed upside down */
.card-inner.reversed .card-flipper { transform: rotate(180deg); }
.card-flipper { width: 100%; height: 100%; transition: transform 0.4s ease; }

/* Flip-in animation — port of the Android SwapViews flip
   (Flip3dAnimation -90deg -> 0deg over 500ms, decelerating) */
.flip-in { animation: flipIn 500ms cubic-bezier(0.2, 0.7, 0.3, 1); }
@keyframes flipIn {
  0%   { transform: rotateY(-90deg); opacity: 0.35; }
  100% { transform: rotateY(0deg);   opacity: 1; }
}

/* Badges & labels */
.pos-badge {
  position: absolute; top: -9px; left: -9px; z-index: 5;
  width: 22px; height: 22px; border-radius: 50%;
  background: linear-gradient(180deg, #fdf8ea, #efe0bc);
  border: 1px solid var(--bronze); color: var(--burgundy-deep);
  font-family: 'Cinzel', Georgia, serif; font-weight: 700; font-size: 11.5px;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 2px 5px rgba(60, 40, 10, 0.3);
}
.reversed-badge {
  position: absolute; top: -9px; right: -9px; z-index: 5;
  padding: 1px 7px; border-radius: 8px;
  background: var(--burgundy-deep); color: #f3e6c8;
  font-family: 'Cinzel', Georgia, serif; font-size: 9px; letter-spacing: 0.08em;
  border: 1px solid var(--gold-light);
}
.pos-label {
  margin-top: 7px; font-family: 'Cinzel', Georgia, serif;
  font-size: 11px; font-weight: 600; color: var(--ink-soft);
  letter-spacing: 0.04em; line-height: 1.25;
  max-width: 150px; margin-left: auto; margin-right: auto;
}
.pos-label.flipped { color: var(--burgundy); }

/* Deck stack visual */
.deck-stack { position: relative; width: 74px; height: 118px; }
.deck-stack .card-back { position: absolute; top: 0; left: 0; --cw: 74px; --ch: 118px; }
.deck-stack .card-back:nth-child(1) { transform: translate(-6px, 6px) rotate(-4deg); opacity: 0.55; }
.deck-stack .deck-count {
  position: absolute; inset: 0; z-index: 4; display: flex; flex-direction: column;
  align-items: center; justify-content: center; color: var(--gold-light);
  font-family: 'Cinzel', Georgia, serif; font-weight: 700;
  text-shadow: 0 1px 4px rgba(0,0,0,0.55);
}
.deck-stack .deck-count .n { font-size: 1.5rem; line-height: 1; }
.deck-stack .deck-count .u { font-size: 0.55rem; letter-spacing: 0.2em; }

/* ------------------------------------------------------------------ */
/* Spread layouts                                                      */
/* ------------------------------------------------------------------ */
.spread-board { display: flex; justify-content: center; padding: 1.2rem 0 0.4rem 0; }
.spread-canvas { position: relative; margin: 0 auto; }
.spread-canvas .card-slot { position: absolute; }
.spread-row { display: flex; gap: 26px; justify-content: center; align-items: flex-start; flex-wrap: wrap; }
.spread-single { display: flex; justify-content: center; }

/* Arc (horseshoe) */
.arc-wrap { display: flex; gap: 18px; justify-content: center; align-items: flex-end; }

/* Mirror */
.mirror-board { display: flex; flex-direction: column; gap: 18px; align-items: center; }
.mirror-row { display: flex; align-items: center; gap: 22px; }
.mirror-glass {
  width: 2px; height: calc(var(--ch, 178px) + 22px); align-self: center;
  background: linear-gradient(180deg, rgba(168,123,46,0) 0%, rgba(168,123,46,0.85) 20%, rgba(168,123,46,0.85) 80%, rgba(168,123,46,0) 100%);
  position: relative;
}
.mirror-glass::after {
  content: '\\2739'; position: absolute; left: 50%; top: 50%;
  transform: translate(-50%, -50%); color: var(--bronze);
  background: rgba(250, 243, 224, 0.95); padding: 3px 1px;
  font-size: 15px; border-radius: 50%;
}
.mirror-key { margin-top: 4px; }

/* Legend under absolute layouts */
.spread-legend {
  display: flex; flex-wrap: wrap; gap: 6px 18px; justify-content: center;
  margin-top: 1.1rem; padding: 0.65rem 1rem;
  background: rgba(255, 252, 240, 0.55);
  border: 1px dashed #c9b584; border-radius: 10px;
  font-family: 'EB Garamond', Georgia, serif; font-size: 0.86rem; color: var(--ink-soft);
}
.spread-legend b { color: var(--burgundy); font-family: 'Cinzel', Georgia, serif; font-size: 0.78rem; }
.spread-legend .dim { opacity: 0.55; }

/* Card detail (port of CardActivity) */
.detail-wrap { display: flex; gap: 1.6rem; align-items: flex-start; flex-wrap: wrap; }
.detail-text { flex: 1; min-width: 260px; }
.detail-text h3 {
  margin: 0 0 0.35rem 0; text-decoration: underline; text-underline-offset: 4px;
  text-decoration-color: var(--bronze-soft); text-decoration-thickness: 1.5px;
}
.detail-section { margin-top: 0.85rem; }
.detail-section .ds-title {
  font-family: 'Cinzel', Georgia, serif; font-weight: 700; color: var(--burgundy-deep);
  text-decoration: underline; text-underline-offset: 4px;
  text-decoration-color: var(--bronze-soft); margin-bottom: 0.2rem;
}
.detail-kw { color: var(--ink-soft); font-style: italic; margin-bottom: 0.3rem; }

/* Deck browser grid */
.deck-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(108px, 1fr)); gap: 18px 14px; }

/* Footer */
.t-footer {
  text-align: center; color: var(--ink-faint); font-style: italic;
  font-size: 0.86rem; margin-top: 2.4rem;
}

/* Small screens: shrink the card size variable used everywhere */
@media (max-width: 780px) {
  .spread-canvas { transform: scale(0.78); transform-origin: top center; margin-bottom: -160px; }
  .spread-row, .arc-wrap { gap: 10px; }
  .arc-wrap .card-slot { --cw: 64px; --ch: 104px; }
}
"""


def inject_global_css() -> None:
    """Push the parchment theme into the running Streamlit app."""
    import streamlit as st

    st.markdown(f"<style>{BASE_CSS}</style>", unsafe_allow_html=True)

