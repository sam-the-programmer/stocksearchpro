import pathlib
from stocksearchpro.data.yahoo import get

tickers = pathlib.Path("stocksearchpro/data/tickers_names.txt").read_text().split("\n")