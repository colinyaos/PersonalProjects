import random

class pull:
    """A class for pull objects. 
    Defined by input string, has attributes isLimited, rarity, and CE / S
    input string has format "3* Servant General"
    """

    def __init__(self, inputString):
        self.description = inputString
        self.words = inputString.split()
        self.rarity = int(self.words[0][0])
        self.type = self.words[1]
        self.availability = self.words[2]
    
    def get_rarity(self):
        return self.rarity
    
    def is_Servant(self):
        if self.type == "Servant":
            return True
        else: 
            return False
    
    def is_limited(self):
        if self.availability == "Limited":
            return True
        else: 
            return False

    def __str__(self):
        return str(self.description)

def translation(inputNum):
    """inputNum is an int between 1 and 100 (inc). 
    We treat 1 as luckier than 100. 
    Rates are as follows:
    5* : 1%, 4% (catch-all)
    4* : 3%, 12% (for now, no split by limit)
    3* : 40%, 40%. 
    We evaluate going in this order."""

    outString = ""

    if inputNum <= 5:
        outString += "5* "
    elif inputNum <= 20:
        outString += "4* "
    else:
        outString += "3* "
    
    if inputNum in range(2, 6) or inputNum in range(9, 21) or inputNum in range(61, 101):
        outString += "CE "
    else:
        outString += "Servant "
    
    outString += "General"

    return outString

def pullone():
    """returns a single pull, using translation(). 
    generates the random number from 1-100 with python random. """

    seed = random.randint(1, 100)
    return pull(translation(seed))


def pullten():
    outlist = []
    for i in range(10):
        outlist.append(pullone())
    
    return outlist

def pullteneval(pullList):
    """takes in a list of 10 pulls. 
    If there is at least 1 4* or above card, 
    and at least 1 3* or above S, return True. 
    Else, return false. """
    isfour = False #rarity total
    isthree = False #non-CE

    for pull in pullList:
        if pull.get_rarity() >= 4:
            isfour = True
        if pull.is_Servant():
            isthree = True
    
    return isfour and isthree

def filterpulls(superpullList):
    """return list of 10-pulls that satisfy the guaranteed requirements. 
    using pullteneval"""
    outputList = []
    for tenp in superpullList:
        if pullteneval(tenp):
            outputList.append(tenp)
    return outputList

def aggregate(superpullList):
    """ Takes in cleaned pullList from filterpulls, and aggregates to 
    find out the totals for everything.
    prints total breakdown for 3* CE, 3* S, 4* CE, 4* S, 5* CE and 5* S. 
    Returns in absolute numbers and in % form. 
    """
    numCounts = [0, 0, 0, 0, 0, 0]
    # print(len(superpullList))
    for pullList in superpullList:
        # print(len(pullList))
        for p in pullList:
            # print(p)
            num = 0 #use this instead of whatever else
            num += 2 * (p.get_rarity() - 3)
            if p.is_Servant():
                num += 1
            numCounts[num] += 1
    # print("3* CE:", numCounts[0])
    # print("3* S:", numCounts[1])
    # print("4* CE:", numCounts[2])
    # print("4* S:", numCounts[3])
    # print("5* CE:", numCounts[4])
    # print("5* S:", numCounts[5])

    pullsum = sum(numCounts)

    percentCounts = [round(x / pullsum * 100, 6) for x in numCounts]
    print("3* CE:", percentCounts[0])
    print("3* S:", percentCounts[1])
    print("4* CE:", percentCounts[2])
    print("4* S:", percentCounts[3])
    print("5* CE:", percentCounts[4])
    print("5* S:", percentCounts[5])

finalPullList = []

for i in range(1000000):
    finalPullList.append(pullten())

# print(len(finalPullList[0]))

finalPullList = filterpulls(finalPullList)

# print(len(finalPullList))
aggregate(finalPullList)


# otherPullList = []

# for i in range(10000):
#     otherPullList.append(pullten())

# # print(len(finalPullList[0]))
# # print(len(finalPullList))


# aggregate(otherPullList)
