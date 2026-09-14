"""HTML rendering helpers.

Streamlit's ``st.markdown`` parses content as markdown first: an
indented line inside a multi-line HTML fragment is interpreted as a
code block and gets HTML-escaped in place.  Every layout fragment in
this app therefore goes through :func:`show_html`, which collapses the
fragment onto a single line before rendering.
"""

from __future__ import annotations

import re

import streamlit as st


def compact_html(html_text: str) -> str:
    """Collapse an HTML fragment onto a single line."""
    return re.sub(r"\s+", " ", html_text).strip()


def show_html(html_text: str) -> None:
    """Render an HTML fragment with all whitespace risks removed."""
    st.markdown(compact_html(html_text), unsafe_allow_html=True)
