import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf


filename = "IM_SPY7d1m07_21.csv"

imDF = pd.read_csv(filename)

print(imDF.head())

# imDF.Index.rename("DateTimeIndex")

imDF.Datetime = pd.DatetimeIndex(imDF.Datetime)

imDF = imDF.set_index("Datetime")

print(imDF.head())


subDF = imDF[400:500]

# apdict = mpf.make_addplot(subDF[["SKA", "SKB", "TKS", "KJS", "CKS"]])

k = mpf.figure()

# ax1 = k.add_subplot(2, 1, 1)
# ax2 = ax1.twinx()
# ax4 = k.add_subplot(2, 1, 2)

# ap = mpf.make_addplot(subDF[["SKA"]])

# mpf.plot(subDF)

# mpf.show()

ax1 = k.subplot()
ax2 = ax1.twinx()

mpf.plot(subDF[["SKA"]], ax = ax1)
mpf.plot(subDF[["SKB"]], ax = ax2)

mpf.show()



# mpf.figure(subDF, addplot = apdict)


# mpf.plot(subDF, addplot = apdict).figure()
