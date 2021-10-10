import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataf = "./StocksData/es1min.csv"; multiplier = 50
# tsdataf = "./StocksData/ts1min.csv"; multiplier = 11000
# zndataf = "./StocksData/zn1min.csv"; multiplier = 1000
esm1df = "./StocksData/esm1.csv"; multiplier = 50


dataf = esm1df

df = pd.read_csv(dataf, names = ["DateTime", "Price", "Bid", "Ask"], header = 0)

# print(df.head())




def evalPos(inSeries, entry, exit):
    """ Returns Buy, Sell, Exit, and Hold for the given position data. 
    if price - ema > sd, return "Sell"
    if ema - price > sd, return "Buy"
    if abs(price - ema) < 0.1, return "Exit"
    Else, return "Hold"
    """

    price = inSeries.at["Price"]
    ema = inSeries.at["EMA"]
    sd = inSeries.at["SD"]

    if price - ema > entry * sd:
        return "Sell"
    if ema - price > entry * sd:
        return "Buy"


    if price - ema < exit * sd:
        return "Exit"


    else:
        return "Hold"

def newEvalPos(inSeries, entry, exit, inPosition):
    """ As before, takes inSeries, and evaluates using SD, etc. whether to 
    enter or exit given input parameters. Decision to enter / exit is dependent 
    on inPosition, which is an int (1 / 0 / -1) displaying long / no / short. 
    Returns 1, 0, -1 based on current position long / no / short. """

    # print(inSeries)

    diff = inSeries.at["Diff"]
    
    # rmsg = ""
    newPos = inPosition

    if inPosition == 0:
        if diff < -entry:
            # rmsg = "Buy To Long"
            newPos = 1
        elif diff > entry:
            # rmsg = "Sell To Short"
            newPos = -1
        # else:
        #     # rmsg = "Stand"
        #     newPos = 0
    
    elif inPosition == 1:
        if diff > -exit:
            # rmsg = "Exit Long"
            newPos = 0

    elif inPosition == -1:
        if diff < exit:
            # rmsg = "Exit Short"
            newPos = 0
        # else:
        #     rmsg = "Hold"
    # else:
    #     rmsg = "Hold"
    
    return newPos

# testIndices = ["DateTime", "Price", "EMA", "SD"]

# testSeries = pd.Series([1, 9, 8, 2], index = testIndices)

# testDF = pd.DataFrame(index = testIndices)

# testDF = testDF.append(testSeries, ignore_index=True)

# print(testDF)


# print(testDF.iloc[4])
# print(newEvalPos(testSeries, 1, 0.1, -1))


def dummy(inseries):
    print(inseries)
    print("\n")

def inOut(decision, givenPosition):
    """ Given a decision and a given position, evaluate if 
    the trader should enter or exit positions at various times. 
    Returns ints 1, 0, or -1 corresponding to current position."""

    dec = decision
    currPos = givenPosition
    # if currentPosition[0] == 1:
    #     print("money")

    if dec == "Hold":
        # print("currentpos is", currentPosition, "at time", currTime)
        return currPos
    if currPos == 0:
        # print("Is anybody home?")
        if dec == "Sell":
            # print("This isn't getting triggered")
            currPos = -1
        if dec == "Buy":
            # print("buying in at zero")
            currPos = 1
    else: #This implies that currentPos is 1 or -1
        if dec == "Exit":
            currPos = 0
        if dec == "Sell" and currPos == 1:
            currPos = -1
        if dec == "Buy" and currPos == -1:
            currPos = 1
    # print("currentpos is", currentPosition, "at time", currTime)
    return currPos


def evaluate(period, entry, exit):
    """ Given period of time (minutes, 60 min increment), entry (# of stdevs to enter the market), and exit 
    (# of stdevs to exit the market), find and return the final balance. """

    ldf = df.copy(deep = True)
    ldf.set_index("DateTime")

    # print(ldf)

    ldf["EMA"] = ldf.Price.ewm(span = period).mean()
    ldf["SD"] = ldf["Price"].rolling(period).std()
    ldf["Diff"] = (ldf.Price - ldf.EMA) / ldf.SD
    

    # ldf["Decision"] = ldf.apply(evalPos, args = (entry, exit), axis = 1)

    # Replace above with for loop, retain evalPos for actually setting the arg

    # dList = [] # should contain all decisions made
    pList = [] # contains a record of the current position

    pList.append(newEvalPos(ldf.iloc[0], entry, exit, 0))

    # if dList[0] == "Buy":
    #     pList.append(1)
    # elif dList[0] == "Sell":
    #     pList.append(-1)
    # else:
    #     pList.append(0)

    for i in range(1, len(ldf)):
        row = ldf.iloc[i]
        # print("row", i, "is", row)
        newPos = newEvalPos(row, entry, exit, pList[-1])
        pList.append(newPos)

    # ldf["Decision"] = dList
    ldf["Position"] = pList

    k = ldf["DateTime"].tail(1).index.item()
    ldf.loc[k, "Position"] = 0

    # ldf["Position"] = ldf.apply(inOut, axis = 1)

    records = ldf.Position.diff()

    # b = list(df.Position)
    # # records[9] = b[0]

    # print(records)

    ldf["Record"] = records

    ldf["Cash"] = -1 * (ldf.Record * ((ldf.Bid + ldf.Ask)/2 + ldf.Record * (ldf.Ask - ldf.Bid) /2))
    ldf["Cash"] = pd.DataFrame.cumsum(ldf.Cash)

    ldf["Sunk"] = ldf.Price * ldf.Position

    ldf["Balance"] = ldf.Cash + ldf.Sunk

    ldf.dropna(inplace = True)
    return ldf


# kdf = evaluate(46 * 60, 1, 0.1)

# print(kdf)

# print(kdf[kdf.Record != 0])

def getBalance(inDF, period, entry, exit):
    """ Given the output dataframe from evaluate, return the final balance. 
    Returns a float. """

    filename = str(period) + "_" + str(entry) + "_" + str(exit) + ".csv"
    inDF.to_csv(filename)

    print(len(inDF[inDF.Record != 0]) / 2)


    k = list(inDF.Balance.tail(1))[0]
    
    return k

# print(getBalance(46*60, 1, 0.1))


periods = [12 * 60, 24 * 60, 48 * 60]
entries = [1, 1.5, 2, 2.5]
exits = [-0.2, 0, 0.2, 0.5, 1.0]

periods = [2880]
entries = [1.5]
exits = [-0.5]


for p in periods:
    for e in entries:
        for x in exits:
            if e - x < 0.5:
                continue
            inDF = evaluate(p, e, x)
            b = getBalance(inDF, p, e, x)
            print("%4d  %5.1f  %5.1f  %8.1f"%(p, e, x, b * multiplier))
            

            k, (plot1, plot2) = plt.subplots(2)
            plot1.plot(inDF.DateTime, inDF.Balance)
            plot2.plot(inDF.DateTime, inDF.Price)
            plt.savefig("bothgraphs.png")
            print("finished saving")
            plt.show()
            
            
            
            # plt.plot(inDF.Balance)
            # plt.savefig("inDFBalance.png")
            # plt.show()
            
            # plt.clf()
            # plt.plot(inDF.Price)
            # plt.show()






            print("\n")

# print(getBalance(2880, 2, 0.5))



# # This is the period of time, in minutes

# # df["SMA"] = df.Price + period


# tframeEWM = testFrame.ewm(span = period)

# print(tframeEWM.mean())

# print(tframeEWM)

# rollT = testFrame.rolling(tframeEWM)

# print(tframeEWM.head())

# testFrame["EMA"] = tframeEWM.mean()

# print(testFrame.head())


# df["EMA"] = df.ewm(span = period).mean()

# # print(df.head(7))

# df["SD"] = df["Price"].rolling(period).std()

# df.set_index("DateTime")

# # All calcs that have to do with past data values should be executed above this line

# # df.dropna(inplace = True)


# df["diff"] = (df.Price - df.EMA) / df.SD


# currentPosition = 0
# # in/out has 1 = long, 0 = none, -1 = short

# inPrice = 0
# # inPrice is the price at which trader enters the position

# totalPnL = 0






# df["Decision"] = df.apply(evalPos, axis = 1)

# print(df.tail())


# k = df["DateTime"].tail(1).index.item()

# # print(k)

# # print("\n Words \n")


# df.loc[k, "Decision"] = "Exit"

# # print(df.tail())

# # print("verification over")

# df["Position"] = df.apply(inOut, axis = 1)

# records = df.Position.diff()

# b = list(df.Position)
# # records[9] = b[0]

# print(records)

# df["Record"] = records


# df["Cash"] = - df.Price * df.Record
# df["Cash"] = pd.DataFrame.cumsum(df.Cash)

# df["Sunk"] = df.Price * df.Position

# df["Balance"] = df.Cash + df.Sunk


# df.dropna(inplace = True)

# print(df.head(17))

# print(df.tail())

# print("----------------------------------------------\n")

# print("All Trades")

# print(df[df.Record != 0])