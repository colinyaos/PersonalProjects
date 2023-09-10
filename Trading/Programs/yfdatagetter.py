import yfinance as yf
import pandas as pd
import os.path

spy = yf.Ticker("AAPL")

superPeriod = "1d"
superInterval = "1m"

spdf = pd.DataFrame(spy.history(period = superPeriod, interval = superInterval))

filename = "SPY" + superPeriod + superInterval + "07_21" + ".csv"
abs_path = "C:/Users/user/folder/"

full_path_name = os.path.join(abs_path, filename)

spdf.to_csv(full_path_name)
