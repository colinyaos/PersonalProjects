"""
ID: colinya1
LANG: PYTHON3
TASK: wormhole
"""

import datetime

fin = open("wormhole.in", "r")
fout = open("wormhole.out", "w")


n = int(fin.readline().strip())

wormholes = []

for i in range(n):
    point = fin.readline().split()
    littleList = []
    for i in point:
        littleList.append(int(i))
    wormholes.append(littleList)

# test data starts here

# n = 10

# wormholes = [[0, 0], [1, 0], [1, 1], [0, 1]]

# wormholes = [[987878530, 332490544], [545074228, 332490544],[571194544, 278963943],[32922985, 229703843] ,
#         [571194544, 851333603] ,
#         [90862786, 28227282] ,
#         [219975775, 267376202], 
#         [219975775, 332490544], 
#         [90862786, 62367085], 
#         [872930617, 951881113]]


# we should call these by 1, 2, 3, 4, etc, using 0 for extra whatever values

next_portal = [] # this goes by horizontal, so same y ONLY

for w in wormholes:
    least_distance = 1000000000
    closest_worm = -1
    for k in wormholes:
        if k == w:
            continue
        if k[1] == w[1]:
            if k[0] > w[0]:
                if k[0] - w[0] < least_distance:
                    closest_worm = wormholes.index(k)
                    least_distance = k[0] - w[0]
    next_portal.append(closest_worm) # should be careful because this is still zero-indexed

# make lPortal here, this should indicate with a 1 those that are the leftmost portal

print("nPortal", next_portal, "\n-----------------------\n")

def generator(nList):
    """ Given an list of integers with length n, returns a list of dictionaries of length n, with keys as 
    the given integers, and each key being paired with its corresponding portal.
    This should contain all possible pairings. """
    # time to use a bit of recursion
    # print("Generator called, ", nList)

    if len(nList) == 2:
        # print("n=2 return")
        return [{nList[0]:nList[1], nList[1]:nList[0]}]
    else:
        superReturnList = []
        # print(len(nList))
        for i in range(1, len(nList) ):
            copyList = nList.copy()
            # print(copyList, i)
            val1 = copyList[i]
            val2 = copyList[0]
            del copyList[i]
            del copyList[0]
            for dict in generator(copyList):
                dict[val1] = val2
                dict[val2] = val1
                superReturnList.append(dict)
                # print("appended", dict)
        return superReturnList

# print(generator(list(range(4))))

# note that next_portal is now full of the indices of the next closest, except where there are none
# in that case, next_portal gives -1. 

# is_end = [] #1 for end, 0 for not end

# for i in range(len(wormholes)):
#     ycoord = wormholes[i][1]
#     isBigger = False
#     for k in range(i, len(wormholes)):
#         if wormholes[k] > ycoord:
#             continue
#         else:
#             isBigger = True
#     if isBigger:
#         is_end[i] = 1
#     else:
#         is_end[i] = 0

def countloops(wHoles, nPortal, pairings):
    # wHoles is a list of wormhole coords, nPortal is an nPortal list
    # pairings is an dict of pairings from generator
    # returns T if starting point is loop, F otherwise in a list
    global debug

    loops = False

    if debug: print("countloop start")
    for i in range(len(wHoles)):
        currentpos = i
        if debug: print("currentpos is", i)
        if debug: print("pairings is", pairings)
        isDone = False

    # let's try only recording portal locations when we enter the portal

        entries = [i]
        while not isDone:
            nextLoc = pairings[currentpos]
            if debug: print("tping from", currentpos, "to", nextLoc)
            currentpos = nextLoc
            # if currentpos in locations:
            #     print(currentpos, "is in", locations)
            #     isDone = True
            #     isLoop = True
            # else:
            #     locations.append(currentpos)
            
            if debug: print("nPortal of ", currentpos, "is", nPortal[currentpos])
            nextLoc = nPortal[currentpos]
            
            if nextLoc == -1:
                isDone = True
                break
            
            currentpos = nextLoc
            if currentpos in entries:
                # print(currentpos, "is in", entries)
                isDone = True
                loops = True

            entries.append(currentpos)
            # print("entries is", entries)

        if debug: print("end of loop\n")

        if loops == True:
            break
    if debug: print("returning...", loops, "\n\n")
    return loops



    # loops = []

    # for i in range(len(wHoles)):
    #     currentpos = i
    #     isDone = False
    #     isLoop = False
    #     visitedPos = [i]
    #     while isDone == False:          
    #         if nPortal[currentpos] == -1:
    #             isDone = True
    #             # now, we know for sure that next is another portal
    #         else:
    #             currentpos = pairings[i]
    #             if currentpos in visitedPos:
    #                 isLoop = True
    #                 isDone = True
    #                 print("looperoo")
    #             visitedPos.append(currentpos)
    #             print("visited pos", visitedPos)
    #     loops.append(isLoop)

    # print(loops)

    # output = 0

    # for i in loops:
    #     if i:
    #         output += 1

    # return output

def countloops2(a, b, c):
    return True

def countAllLoops(wHoles, nPortal):
    firstTime = datetime.datetime.now()
    allPairings = generator(list(range(len(wHoles))))
    totalLoops = 0
    # print(allPairings)
    for pairing in allPairings:
        startTime = datetime.datetime.now()
        if countloops(wHoles, nPortal, pairing):
            # print(pairing, "is a valid pairing")
            totalLoops += 1
        else:
            # print(pairing, "is not a valid pairing")
            pass
        endTime = datetime.datetime.now()
        # print("time for loop =", endTime - startTime)
    lastTime = datetime.datetime.now()
    print("total time is", lastTime - firstTime)
    return totalLoops


debug = False

k = countAllLoops(wormholes, next_portal)

print(k)

fout.write(str(k) + "\n")

# we will now refer to the wormholes as #0, #1, #2, etc. 

# def generator(vertices):
#     """ generates all possible pairings for vertices of an n-gon. 
#     returns a list of lists, where each sublist has len 2, pos0 < pos1. 
#     pos0 is connected to pos1. 
#     Note that the order of generation must be the same each time. 
#     vertices is taken to be a list of ints denoting vertices of an n-gon, 
#     and our desired output format is a list of (n/2)-length lists of 2-length tuples, 
#     where each 2-length tuple denotes a pairing of two points. """
#     # We want a recursive call, so that we can use generator of n to find
#     # a good pairing for generator n+2. 

#     if len(vertices) == 2:
#         return [[(vertices[0], vertices[1])]]

#     output = [] #output is a list containing lists of tuples

#     for i in range(len(vertices) - 1):
#         # The way this works is we generate our first pairing based on what 0 does. 
#         # Then, we use the recursive call to pull the n-2 case, and use that to 
#         # fill in the rest of the necessary pairings for our tempPairing. 
#         # TempPairing is then added to output. 

#         zeroPair = (vertices[0], vertices[1 + i])

#         # print(zeroPair)

#         newVertices = vertices.copy()

#         newVertices.remove(vertices[1 + i])
#         newVertices.remove(vertices[0])

#         subgen = generator(newVertices)

#         # print(subgen)

#         for subArrangement in subgen:
#             subArrangement.insert(0, zeroPair)
#             output.append(subArrangement)
#     return output

# def getrelationships(coordlist, ordering):
#     """ given coordinates, ordering, return a dictionary. 
#     Keys in the dictionary are point A in a pair, and values are point B in a pair. 
#     Then, reverse the order and put all the relations in again. """

#     outdict = {}

#     for entry in ordering:
#         outdict[coordlist[entry[0]]] = coordlist[entry[1]]
#         outdict[coordlist[entry[1]]] = coordlist[entry[0]]    

#     return outdict

# def traverse(coordlist, ordering, startpoint):
#     """ given coordinates, ordering, and a starting point, runs this starting point until its conclusion. 
#     Returns boolean t if it exits successfully, and boolean false if it runs into a loop. 
#     coordlist is a list of tuples [(a, b), (c, d)] and ordering is a list of tuples [(1, 2), (3, 4)]. 
#     """
#     currLocation = startpoint
#     relations = getrelationships(coordlist, ordering)

#     pointsVisited = []

# def testwalk(coordlist, ordering):
#     """given a list of coordinates of portals (list of tuples e.g. [(0,0), (3, 4), (5, 6)]), and 
#     ordering, which is another list of tuples (e.g. [(2, 3), (5, 6), (1, 4)]), we pair the portals 
#     up using the tuples, and then run cows through each portal to see if we get stuck in loops. 
#     returns boolean T/F if y/n can get stuck in loop. 
#     """
#     # we will do a lot of the grunt work via cows with laser eyes. 



# # print(generator(list(range(6))))


# testgen = generator(list(range(6)))

# print(len(testgen))

# print(testgen[2])

# testcoords = [(1, 1), (4, 5), (9, 8), (7, 5), (16, 1), (8, 5)]

# print(getrelationships(testcoords, testgen[2]))

# print(generator(testrange))
