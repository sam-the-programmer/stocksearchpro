import streamlit as st

st.set_page_config(
    page_title="Stock Search Pro • Analysis",
    page_icon="📈",
    layout="wide",
)


from stocksearchpro.helpers import ui
ui.ui()

