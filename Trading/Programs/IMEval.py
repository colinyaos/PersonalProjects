import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

fin = "IM_SPY7d1m07_21.csv"

df = pd.read_csv(fin)

# print(df.head())

# df["KumoLow"] = np.where(df.SKA > df.SKB, df.SKA, df.SKB)

# df["KumoLow"] = np.where(df.SKA > df.SKB, df.SKA, df.SKB)


# df["Kumo"] = df.SKA > df.SKB


# df["InKumo"] = abs(df.SKA - df.Close) + abs(df.Close - df.SKB) == abs(df.SKA - df.SKB)

# bananas = df.InKumo.diff()

# print(bananas)

# df["inKumo"] = 

# print(df.iloc[35, 50])

# TKS / KJS Cross

# print(df[df.InKumo == True])

# print(df[df.Kumo == True])

# print(df.tail())

# KJS Cross

# Kumo Breakout

# SKS Cross

# CKS Cross



def evalKumo(firstList, secondList):
    """ Given 2 consecutive Series in the form 
    Datetime    Open    High    Low     Close   TKS     KJS     SKA     SKB     CKS, 
    evaluate the position. 
    Return a new series that includes all previous information, plus the following:
    TKS/KJS signal strength
    KJS/price signal strength
    Kumo Breakout signal strength
    SKA/SKB signal strength
    CKS/Price signal strength
    Total signal strength

    Bull signals are 1 for weak, 2 for neutral, 3 for strong
    Bear signals are -1 for weak, -2 for neutral, -3 for strong
    No signal is represented by a 0
    """
    list1 = firstList
    list2 = secondList

    TKS1, TKS2, KJS1, KJS2 = list1.TKS, list2.TKS, list1.KJS, list2.KJS
    DT1 = list1.Datetime
    DT2 = list2.Datetime

    print("TKS1", TKS1, "TKS2", TKS2, "KJS1", KJS1, "KJS2", KJS2)
    print("DT1", DT1, "DT2", DT2)


    if (TKS1 > KJS1 and KJS2 > TKS2) or (TKS1 < KJS1 and KJS2 < TKS2):
        # we can immediately conclude there is a cross from the above. 
        upper1 = max(TKS1, KJS1)
        lower1 = min(TKS1, KJS1)
        upper2 = max(TKS2, KJS2)
        lower2 = min(TKS2, KJS2)
        [DT, YIS] = pointcross(DT1, DT2, upper1, lower2, lower1, upper2)
        print(DT, YIS)


def pointcross(dt1, dt2, y1, y2, y3, y4):
    """ Given dt1 and dt2, both Datetime objects, and y-coords
    y1, y2, y3, y4, find the point of intersection. Return in list [Datetime, y-coord]. 
    y1 and y3 have dt1 as x-coord, y2 and y4 have dt2. 
    y1 and y2 are connected, and y3 and y4 are connected. 
    Thus,
    y1  x  y4
    y3  x  y2    . 
    We assume that the two lines do cross over, and that from top to bottom, we have y1 -> y3, y4 -> y2. """



    delta1 = abs(y1 - y3)
    delta2 = abs(y2 - y4)

    ratio = delta1 / (delta1 + delta2)

    print("ratio is", ratio)


    finalDT = dt1 + ratio * (dt2 - dt1)

    high1 = max(y1, y3)
    low2 = min(y2, y4)

    finalY = high1 - ratio * (high1 - low2)

    return [finalDT, finalY]



# timeA = dt.datetime(2021, 7, 31, 13, 30)
# timeB = timeA + dt.timedelta(hours= 2)

# [y1, y2, y3, y4] = [30, 0, 0, 20]

# print(pointcross(timeA, timeB, y1, y2, y3, y4))


print(df.iloc[3], "\n---")

print(evalKumo(df.iloc[3], df.iloc[4]))



