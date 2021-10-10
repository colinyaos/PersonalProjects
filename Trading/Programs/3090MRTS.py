import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import yahoo_finance as yf
import yfinance as yf

spy = yf.Ticker("CAT")

superPeriod = "60d"
superInterval = "15m"

longPeriod = 5 * 7 * 4
shortPeriod = 2 * 7 * 4

superEntry = 1
superExit = 0


# bladf = spy.history(period = "1mo", interval = "60m")

# print(bladf)

# print(msft.info)

# df = spy.history(period = "5y")

twt = yf.Ticker("TWTR")
fb = yf.Ticker("FB")

twtdf = twt.history(period = superPeriod, interval = superInterval)
fbdf = fb.history(period = superPeriod, interval = superInterval)

# ser = df.Open
# df = pd.DataFrame(ser)


twtdf = pd.DataFrame(twtdf.Close)
fbdf = pd.DataFrame(fbdf.Close)

# print(twtdf.head())

ratio = twtdf.iloc[0] / fbdf.iloc[0]

# print(ratio)

# print(fbdf.head())

fbdf = fbdf * ratio

# print(fbdf.head())

workingDF = fbdf - twtdf

# print(ser)

# entry = 0.8
# exit = 0.2


# print(df)
# df.columns = ["Price"]

# df["LongTerm"] = df.Price.ewm(span = 65).mean()
# df["ShortTerm"] = df.Price.ewm(span = 22).mean()

# def minimethod(inSeries):
#     """ Takes in a row of the DF, and returns 1 if D30 > D90. 
#     Else, returns -1. """

#     print(inSeries)
#     d30 = inSeries.LongTerm
#     d90 = inSeries.ShortTerm
#     if d30 > d90:
#         return 1
#     else:
#         return -1


# df["Greater"] = df.apply(minimethod, axis = 1)





def newEvalPos(inSeries, inPosition, entry, exit):
    """ As before, takes inSeries, and evaluates using SD, etc. whether to 
    enter or exit given input parameters. Decision to enter / exit is dependent 
    on inPosition, which is an int (1 / 0 / -1) displaying long / no / short. 
    Returns 1, 0, -1 based on current position long / no / short. """

    PR = inSeries.at["Price"]
    LT = inSeries.at["LongTerm"]
    ST = inSeries.at["ShortTerm"]
    SD = inSeries.at["LTSD"]
    
    score = (ST- LT) / SD
    pscore = (PR - LT) / SD

    newPos = inPosition

    if inPosition == 0:
        if score < 0 and pscore < -entry:
            # rmsg = "Buy To Long"
            newPos = 1
        elif score > 0 and pscore > entry:
            # rmsg = "Sell To Short"
            newPos = -1
    
    elif inPosition == 1:
        if score > -exit:
            newPos = 0

    elif inPosition == -1:
        if score < exit:
            newPos = 0
    return newPos

def evaluate(inDF, entry, exit):
    """ Given period of time (minutes, 60 min increment), entry (# of stdevs to enter the market), and exit 
    (# of stdevs to exit the market), find and return the final balance. """

    ldf =inDF.copy(deep = True)

    ser = inDF.Close
    ldf = pd.DataFrame(ser)
    # print(df)
    ldf.columns = ["Price"]

    # print(ldf)

    ldf.columns = ["Price"]

    ldf["LongTerm"] = ldf.Price.ewm(span = longPeriod).mean()
    ldf["ShortTerm"] = ldf.Price.ewm(span = shortPeriod).mean()
    
    ldf["LTSD"] = ldf.LongTerm.rolling(longPeriod).std()


    pList = [] # contains a record of the current position

    pList.append(newEvalPos(ldf.iloc[0], 0, entry, exit))

    for i in range(1, len(ldf)):
        row = ldf.iloc[i]
        newPos = newEvalPos(row, pList[-1], entry, exit)
        pList.append(newPos)

    ldf["Position"] = pList

    k = ldf["Price"].tail(1).index.item()
    ldf.loc[k, "Position"] = 0
    records = ldf.Position.diff()
    ldf["Record"] = records

    ldf["Cash"] = -1 * (ldf.Record * ldf.Price)
    ldf["Cash"] = pd.DataFrame.cumsum(ldf.Cash)

    ldf["Sunk"] = ldf.Price * ldf.Position

    ldf["Balance"] = ldf.Cash + ldf.Sunk

    ldf.dropna(inplace = True)

    return ldf

def getBalance(inDF):
    """ Given the output dataframe from evaluate, return the final balance. 
    Returns a float. """

    filename = "2265T1.csv"
    inDF.to_csv(filename)

    print(len(inDF[inDF.Record != 0]) / 2)

    k = list(inDF.Balance.tail(1))[0]
    
    return k

k = evaluate(workingDF, superEntry, superExit)


print(k[k.Record != 0])



# print(k)
print(getBalance(k))

# plt.plot(k.Price)

# plt.show()

    