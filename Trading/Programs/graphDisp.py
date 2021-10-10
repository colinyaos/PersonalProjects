import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "2265T1.csv"

allDF = pd.read_csv(filename)

k, (plot1, plot2, plot3) = plt.subplots(3)

plot1.plot(allDF.Price, "k")

print(allDF.head())

# print(len(allDF))

longplot = allDF[allDF.Position == 1]
shortplot = allDF[allDF.Position == -1]

plot1.plot(longplot.Price, ".g", linestyle = "None")
plot1.plot(shortplot.Price, ".r", linestyle = "None")

COpoints = allDF[allDF.Record != 0]

plot2.plot(allDF.LongTerm, "k")
plot2.plot(allDF.ShortTerm, "b")
plot2.plot(COpoints.LongTerm, "co")

plot3.plot(allDF.Balance, "k")

lenXAxis = len(allDF)
horizontalAxis = []

def formatDates(inString, whatever):
    """ Will be given an input string with the number corresponding to the entry 
    for that data point. Will lookup the relevant value in the DF and return a 
    string in the format "MM/DD". """

    # print("instring is", inString)
    # print("whatever", whatever)

    if int(inString) < 0:
        return inString
    if int(inString) > len(allDF) -1:
        return inString


    # print("instring is", inString)
    # print("whatever", whatever)

    currDate = allDF.iloc[int(inString)].Datetime
    month = currDate[5:7]
    day = currDate[8:10]
    return str(month + "/" + day)

plot1.xaxis.set_major_formatter(plt.FuncFormatter(formatDates))

# print(formatDates(3))

# print("finished\n\n\n")

plt.show()

