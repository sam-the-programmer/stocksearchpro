"""
A script to convert the list of ticker symbols
to ones with the name of the company. Once run,
the file will update, and this file will not need
to be run again.
"""
import pathlib
from collections import deque
import threading

import yfinance as yf

tickers = list(set(pathlib.Path("stocksearchpro/data/tickers.txt").read_text().split("\n")))

names = deque()
def run(o, l):
    for j in tickers[o:l]:
        try:
            s = f"{j} - {yf.Ticker(j).get_info()['longName']}"
            print(s)
            names.append(s)
        except KeyError:
            print(f"ERROR: {j}")

threads = []
for i in range(12):
    t = threading.Thread(target=run, args=(i*len(tickers)//4, min((i+1)*len(tickers)//4, len(tickers))))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

pathlib.Path("stocksearchpro/data/tickers_names.txt").write_text("\n".join(names))
