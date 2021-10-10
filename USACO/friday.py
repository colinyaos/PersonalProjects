"""
ID: colinya1
LANG: PYTHON3
TASK: friday
"""

fin = open("friday.in", "r")
fout = open("friday.out", "a")


n = int(fin.readline())

daysSinceStart = 0
monthDays = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
leapMonthDays = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def isleap(n):
    """if the year (absolute number) is leap, returns True. 
    Else, returns False. """
    realYear = n
    if realYear % 400 == 0:
        return True
    if realYear % 100 == 0:
        return False
    if realYear % 4 == 0:
        return True
    else:
        return False

def thirteen(startday):
    """Returns int day for given startday (int 0 = sun, 1 = mon, 2 = Tue, etc. )
    Startday is the day of the 1st of the month. 
    day follows same format as startday
    """
    daythirteen = startday + 12
    return (daythirteen % 7)

def evalyear(yearnum, startday):
    """Given the year (absolute number) and startday (as before), return a list in the 
    following order: [Sun, Mon, Tue, Wed, Thur, Fri, Sat]. 
    Each day is an int representing the number of 13s that fall on that date. """
    outList = [0, 0, 0, 0, 0, 0, 0]
    currStartDay = startday
    for i in range(1, 13):
        # print(i)
        outList[thirteen(currStartDay)] += 1
        if isleap(yearnum):
            currStartDay = (currStartDay + leapMonthDays[i]) % 7
        else:
            currStartDay = (currStartDay + monthDays[i]) % 7
    return outList

currentYear = 1900
currentStartDay = 1

dayList = [0, 0, 0, 0, 0, 0, 0]
for i in range(n):
    thisYear = evalyear(currentYear, currentStartDay)
    for k in range(7):
        dayList[k] += thisYear[k]

    if isleap(currentYear):
        currentStartDay = (currentStartDay + 366) % 7
    else:
        currentStartDay = (currentStartDay + 365) % 7
    currentYear += 1

# print(dayList)
newString = str(dayList[6])

for i in range(6):
    newString += " "
    newString += str(dayList[i])

newString += "\n"
fout.write(newString)