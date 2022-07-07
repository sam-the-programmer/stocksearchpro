import streamlit as st

st.set_page_config(
    page_title="Stock Search Pro • Forecasting",
    page_icon="📈",
    layout="wide",
)

from stocksearchpro.data import get as get_data
from stocksearchpro.data import tickers
from stocksearchpro.helpers import ui

ui.ui()

st.title("Forecasting")
st.write("Forecast stocks with machine learning.")

stockname = st.selectbox("Choose Stock", tickers)
stockinfo = {
    "name": stockname.split("-")[1].strip(),
    "symbol": stockname.split("-")[0].strip(),
}

cols = st.columns([3, 1])
with cols[0]:
    period = st.select_slider(
        "Select Time Period", ["1d", "5d", "1mo", "3mo", "1y", "5y", "10y", "ytd"], "1d"
    )

with cols[1]:
    types = ["Open", "Close", "High", "Low", "Adj Close", "Volume"]
    boxes = [False for _ in range(len(types))]
    for i, type_ in enumerate(types):
        boxes[i] = st.checkbox(type_)
