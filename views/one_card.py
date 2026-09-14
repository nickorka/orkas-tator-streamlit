"""One Card spread page — Streamlit port of ``OneCardActivity``."""

from components.spread_flow import run_spread_flow
from domain.reading import CardReadingType
from state import init_state

init_state()

run_spread_flow(CardReadingType.ONE_CARD)
