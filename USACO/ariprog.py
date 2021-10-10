"""
ID: colinya1
LANG: PYTHON3
TASK: ariprog
"""

import math
from bisect import bisect_left
import datetime

# fin = open("ariprog.in", "r")
# fout = open("ariprog.out", "w")

# N = int(fin.readline().strip())
# M = int(fin.readline().strip())

startTime = datetime.datetime.now()


N = 11 # length of progs
M = 200 # upper bound of bisquares


listPQ = []

for i in range(M + 1):
    for j in range(i + 1):
        listPQ.append(i ** 2 + j ** 2)
listPQ = list(set(listPQ))
listPQ.sort()
llPQ = len(listPQ)

# print(listPQ)




# Hash table approach? starts here

multiplier = -1

if N < 4:
    multiplier = 1
elif N < 6:
    multiplier = 4
elif N < 12:
    multiplier = 12
else:
    multiplier = 84

hashed = listPQ

if not multiplier == 1:
    hashed = [(math.floor(x / multiplier), x % multiplier) for x in listPQ]
    hashDict = dict(zip(listPQ, hashed))

# our final datatype is named BigDict
# BigDict has keys from 0 -> n-1, where n is multiplier
# Values are lists of all the quotients when divided by n for each modulo

bigDict = {}

for k in range(multiplier):
    bigDict[k] = []

for h in hashed:
    quotient = h[0]
    remainder = h[1]
    bigDict[remainder].append(quotient)

# for l in bigDict:
    # print(l, bigDict[l])

hashTime = datetime.datetime.now()

print("hash", hashTime - startTime)




# Now, we need a method that will scan a list and identify ariProgs. 

# Methodology: Given starting point, generate a list of all possible diffs
# Then, scan through one by one, writing out good progs as they appear

def search(index1, diff, n, listIn):
    """ Takes listIn and looks for an ariprog of length n in listIn. 
    If such an AP exists, return [index1, diff]. Else, return []. 
    Assumptions: index1 + n * diff < last entry in listIn. 
    listIn is sorted, with no dupes. """

    numTerms = 1
    currentTerm = listIn[index1]
    currentIndex = index1

    while numTerms < n:
        target = currentTerm + diff
        
        while currentTerm < target:
            currentTerm = listIn[currentIndex]
            if currentTerm > target:
                return []
            if currentTerm == target:
                numTerms += 1
                break

            currentIndex += 1

            if currentIndex > len(listIn) - 1:
                return []
        
        # print("numTerms is", numTerms)

    return [index1, diff]

def lowerSearch(index1, n, listIn):
    """ Given index1 and length of prog n, and listIn, use search to 
    find all possible progs that satisfy the given conditions. """

    possibleDiffs = math.ceil((listIn[-1] - listIn[index1]) / (n-1))

    # print("pdiff", index1, n, possibleDiffs)
    possibleProgs = []

    for i in range(1, possibleDiffs + 1):
        given = search(index1, i, n, listIn)
        if not given == []:
            possibleProgs.append(given)

    return possibleProgs

def allSearch(n, listIn):
    """ Main method to call. Uses lowersearch over every candidate to find all 
    possible ariProgs. Takes in length n and list listIn."""

    possibleI1s = list(range(len(listIn) - n + 1))
    allProgs = []

    for i in possibleI1s:
        print("tested", i)
        results = lowerSearch(i, n, listIn)
        for r in results:
            allProgs.append(r)

    return allProgs





######################
# Some Tests Here
######################

# T = [1, 2, 5, 6, 7, 8, 15, 22, 29, 35]
#    0, 1, 2, 3, 4, 5, 6,  7,  8,  9


# print("\nlistPQ:", listPQ, "\n")

# print("search", search(7, 7, 3, T))

# print("\n", lowerSearch(2, 3, T))

# print("\n", allSearch(3, T))


print("\n", len(allSearch(N, listPQ)))

endTime = datetime.datetime.now()

print(endTime - startTime)

# print("search", search(2, 24, 5, listPQ))

# print("search", search(2, 8, 5, listPQ))

# print("\n", lowerSearch(2, 5, listPQ))




#SEEKER NOW DEPRECATED
# begin seeker here

# allProgs = [] # This contains all progressions, each of which is stored as a list
# firstNum = 0 # This is the index of the first number in the progression that we test
# secondNum = 1 # This is the index of the second number in the progression we wish to test

# def inMost(index1, index2):
#     """ Given indices of values 1 and 2, test to see if there is a value 3 in the list. 
#     If so, return its index. Else, return -1. """
#     firstVal = listPQ[index1]
#     secondVal = listPQ[index2]
#     diff = secondVal - firstVal
#     target = secondVal + diff

#     # print("firstval", firstVal, "secondVal", secondVal, "target", target)

#     if target > listPQ[-1]:
#         return -1

#     insertPoint = bisect_left(listPQ, target)

#     if listPQ[insertPoint] == target:
#         return insertPoint
#     else:
#         return -1
    
# def nextLoop(index1, index2, length):
#     """ Given indices of values 1 and 2, test to see if there is an arithmetic progression
#     of length "length" in the list. If so, return the indices of the progression. Else, return empty list. """
#     progression = [index1, index2]

#     diff = listPQ[index2] - listPQ[index1]
#     if listPQ[index2] + (length - 2) * diff > listPQ[-1]:
#         return []

#     while len(progression) < length:
#         isGood = inMost(progression[-2], progression[-1])
#         if not isGood == -1:
#             progression.append(isGood)
#         else:
#             # print("failure to find progression for", index1, index2, length)
#             return []
    
#     if len(progression) == length:
#         return progression
    
# def outerLoop(index1, length):
#     """Given 1 and length, evaluate all candidates for 2. Using nextloop, iterate through to find valid. 
#     If yes, store the indices of the progressions, and continue looping. Else, continue looping. 
#     Return list of indices of all valid progressions, if empty, return empty list. """
    
#     # length 1-3 has diff mult 1
#     # length 4-5 has diff mult 4
#     # length 6-11 has diff mult 12
#     # length 12-25 has diff mult 84

#     multiplier = -1
#     if length < 4:
#         multiplier = 1
#     elif length < 6:
#         multiplier = 4
#     elif length < 12:
#         multiplier = 12
#     else:
#         multiplier = 84
    
#     # print(multiplier)

#     progRange = listPQ[-1] - listPQ[index1]
#     possibilities = list(range(1, math.ceil(progRange / multiplier) + 1))
#     possibleNums = [listPQ[index1] + p * multiplier for p in possibilities]

#     loopCandidates = []

#     for p in possibleNums:
#         if p > listPQ[-1]:
#             continue
#         possibleIndex = bisect_left(listPQ, p)
#         if listPQ[possibleIndex] == p:
#             loopCandidates.append(possibleIndex)

#     goodLoops = []

#     for l in loopCandidates:
#         nl = nextLoop(index1, l, length)
#         if nl == []:
#             continue
#         else:
#             goodLoops.append(nl)
    
#     return goodLoops

# def baseLoop(length):
#     """ for given length, iterates from 0 to n-2 for first value. Uses outerloop to 
#     test for each first entry, and returns in usual format results. """
#     firstCandidates = list(range(len(listPQ) - 2))
#     outList = []

#     for l in firstCandidates:
#         tempList = outerLoop(l, length)
#         for t in tempList:
#             outList.append(t)
    
#     return outList

# def finalize(length):
#     allLoops = baseLoop(length)
#     tempList = []
#     for a in allLoops:
#         firstVal = listPQ[a[0]]
#         secondVal = listPQ[a[1]]
#         diff = secondVal - firstVal
#         tempList.append([firstVal, diff])
    
#     sList = sorted(tempList, key = lambda element: (element[1], element[0]))
    
#     returnList = ([str(x[0]) + " " + str(x[1]) for x in sList])

#     return returnList


# Tests here

# startTime = datetime.datetime.now()

# print("\n-------------------------\nTests begin here\n")

# print("listpq:", listPQ[0:20])
# print("range:  ", list(range(20)))

# print("\ninmost")
# print(inMost(5, 8))

# print("\nnextLoop")
# print(nextLoop(6, 8, 3))

# print("\nouterLoop")
# print(outerLoop(1, 3))

# print("\nBaseLoop")
# print(baseLoop(11))
# print(len(baseLoop(11)))


# print("\nFinalize")
# print(finalize(N))

# print("\n")

# def littleThing(a, b):
#     totalLoop = outerLoop(a, b)
#     outList = []
#     for t in totalLoop:
#         tempList = []
#         for k in t:
#             tempList.append(listPQ[k])
        
#         outList.append(tempList)
#     return outList

# for k in outerLoop(10, 5):
#     print([listPQ[x] for x in k])

# print("\n LT")
# print(littleThing(4, 18))

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# finalList = finalize(N)

# if len(finalList) == 0:
#     fout.write("NONE\n")
# else:

#     for k in finalize(N):
#         fout.write(str(k) + "\n")


# endTime = datetime.datetime.now()

# print(endTime - startTime)














########################################

# allProgs = []

# isDone = False
# firstCounter = 0
# nextCounter = 1

# print("\n\n")
# print(listPQ[0:30])
# print("\n\n")


# while not isDone:
#     tempProg = []
#     diff = listPQ[nextCounter] - listPQ[firstCounter]
#     tempProg.append(listPQ[firstCounter])
#     tempProg.append(listPQ[nextCounter])

#     while len(tempProg) <= N:
#         newTarget = listPQ[nextCounter] + diff
#         print("newTarget", newTarget)
        

#         counter = nextCounter + 1
#         while listPQ[counter] <= newTarget:
#             counter += 1
#             # if counter > math.ceil(len(listPQ)  / 2):
#             #     isDone = True

#             #     print("this counter procced")
#             #     break
#         counter -= 1
#         if listPQ[counter] == newTarget:
#             tempProg.append(listPQ[counter])
#             nextCounter += 1
#         else:
#             # print("this counter failed", tempProg, counter, len(listPQ))
#             nextCounter += 1
#             break
    
#     if len(tempProg) == N:
#         allProgs.append(tempProg)
    
#     if firstCounter == llPQ - M:
#         break

#     firstCounter += 1
#     nextCounter = firstCounter + 1
#     print("continuing to loop", firstCounter)

# print("all", len(allProgs))

# print("ap", allProgs)

# outList = []




# for a in allProgs:
#     firstA = a[0]
#     secondA = a[1]
#     diff = secondA - firstA

#     outList.append(str(firstA) + " " + str(secondA))

# print(outList)




# for o in outList:
#     fout.write(o + "\n")

#The Following is Wayy Too Slow
# for i in range(llPQ):
#     for j in range(i + 1, llPQ):
#         diff = listPQ[j] - listPQ[i]
#         fullRange = []
#         isGood = True

#         for k in range(M):
#             fullRange.append(listPQ[i] + k * diff)
#         for e in fullRange:
#             if not e in listPQ:
#                 isGood = False
#         if isGood:
#             print(fullRange)
        



# print(len(listPQ))

# print(listPQ[-1])

# maxDiffs = {} # contains max differences for each length of sequence

# for i in range(3, 26):
#     maxDiffs[i] = (math.ceil((listPQ[-1] - listPQ[0]) / i))

# print("maxdiff", maxDiffs)

# def checkProg(n, diff):
#     """ n is length of progression, diff is the current distance to be iterated on
#     returns a list containing the first elements that are valid solutions for given diff."""
    # totalGap = n * diff

    # print("totalGap =", totalGap)
    # biggestStart = listPQ[-1] - totalGap

    # print("biggestStart", biggestStart)
    # numIters = 0
    # while listPQ[numIters] < biggestStart:
    #     numIters += 1

    # print(numIters)
    # returnList = []
    # for i in range(numIters): #this tests iterations for each starting point
    #     goodSoFar = True
    #     baseNum = listPQ[i]
    #     # print(baseNum)
        
    #     for k in range(n): #this tests for the presence of each entry in the 
    #         if baseNum + diff * k in listPQ:
    #             goodSoFar = True
    #         else:
    #             goodSoFar = False
        
    #     if goodSoFar:
    #         returnList.append(listPQ[i])

# k = checkProg(5, 20)

# print(k)
