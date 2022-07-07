import streamlit as st

st.set_page_config(
    page_title="Stock Search Pro • Forecasting",
    page_icon="📈",
    layout="wide",
)

import yfinance as yf
from stocksearchpro.data import tickers
from stocksearchpro.helpers import ui

ui.ui()

st.title("Forecasting")
st.write("Forecast stocks with machine learning.")
st.selectbox("Choose Stock", tickers)
