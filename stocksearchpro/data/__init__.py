import pathlib


tickers = pathlib.Path("stocksearchpro/data/tickers_names.txt").read_text().split("\n")