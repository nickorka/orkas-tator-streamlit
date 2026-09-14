"""Celtic Cross spread page — Streamlit port of ``CelticCrossActivity``."""

from components.spread_flow import run_spread_flow
from domain.reading import CardReadingType
from state import init_state

init_state()

run_spread_flow(CardReadingType.CELTIC_CROSS)
