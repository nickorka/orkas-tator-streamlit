"""Three Card spread page — Streamlit port of ``ThreeCardActivity``."""

from components.spread_flow import run_spread_flow
from domain.reading import CardReadingType
from state import init_state

init_state()

run_spread_flow(CardReadingType.THREE_CARD)
