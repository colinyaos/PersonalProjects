import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import mplfinance as mpf


filename = "IM_SPY7d1m07_21.csv"

spdf = pd.read_csv(filename)
print(spdf.head())

k = mpf.make_mpf_style(base_mpf_style = "classic")


dtcopy = spdf.Datetime
spdf.Datetime = pd.DatetimeIndex(spdf.Datetime)
spdf = spdf.set_index("Datetime")

spdf = spdf.head(50)


fig = mpf.figure(style = k)
ax1 = fig.add_subplot()
ax2 = ax1.twinx()
ax3 = ax1.twinx()

# mpf.plot(spdf[["SKA"]], ax=ax1,type='ohlc',style='default')

dt = dtcopy.head(50)
ska = spdf.SKA
skb = spdf.SKB

print(dt.head())
print(ska.head())
print(skb.head())



ap = mpf.make_addplot(spdf[["SKA", "SKB", "TKS", "KJS", "CKS"]], ax = ax1, ylabel = "Ska")


ax3.plot(dt, ska, ".--")
ax3.plot(dt, skb, ".--")

ax3.fill_between(dt, ska, skb, where=(ska > skb), color = "C0", alpha = 0.2, interpolate = True)
ax3.fill_between(dt, ska, skb, where=(skb > ska), color = "C1", alpha = 0.2, interpolate = True)


mpf.plot(spdf, ax=ax2, addplot = ap, type='ohlc')

plt.xticks()

mpf.show()