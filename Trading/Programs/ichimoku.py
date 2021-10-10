import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


fin = "SPY7d1m07_21.csv"
fout = "IM_SPY7d1m07_21.csv"


spdf = pd.read_csv(fin)

print(spdf.head())

print(spdf.columns)

del spdf["Volume"]
del spdf["Dividends"]
del spdf["Stock Splits"]

print(spdf.head())

IMshort = spdf.rolling(9)
IMmed = spdf.rolling(26)
IMlong = spdf.rolling(52)

# print(spdf.Open.head(15))

spdf["TKS"] = 1/2 * (IMshort.High.max() + IMshort.Low.min() )
spdf["KJS"] = 1/2 * (IMmed.High.max() + IMmed.Low.min())

spdf["SKA"] = 1/2 * (spdf.TKS + spdf.KJS)
spdf["SKB"] = 1/2 * (IMlong.High.max() + IMlong.Low.min())

spdf["CKS"] = spdf.Close.shift(26)

spdf = spdf.dropna()

print(spdf.head())

spdf.to_csv(fout)