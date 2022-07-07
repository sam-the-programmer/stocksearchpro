import streamlit as st

st.set_page_config(
    page_title="Stock Search Pro • Home",
    page_icon="📈",
    layout="wide",
)

from stocksearchpro.helpers import ui
from stocksearchpro.helpers import legal

ui.ui()

st.markdown("""
<h1 style="text-align: center;">Stock Search Pro</h1>
<p style="text-align: center;">
    Stock Search Pro is an upgraded version of its predecessor, Stock Search. It
    provides improved models, more features and a more intuitive interface.
</p>
""",
    unsafe_allow_html=True
)

legal.disclaimer()
