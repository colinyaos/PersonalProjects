# OpChallenge.py

# We are given the coordinates of "food" in terms of pairs of floats (x, y). 
# Starting from the origin, we take walks in unit steps in cardinal directions, 
# ending when out "walk" traces over a "food" coordinate. 
# "Food" is positioned such that any walk which goes uniformly outwards will 
# eventually trace over some "Food". In other words, the boundary is closed. 
# The challenge is to determine the average walk length. 

import random
import datetime

startTime = datetime.datetime.now()

# Coordinates of food, as a list of pairs of floats. 
# Default test case is the 4x4 square centered around the origin. 

# foodCoords = [(2, 0), (2, 1), (2, 2), (2, -1), (2, -2), (-2, 0), (-2, -1), (-2, -2), (-2, 1), (-2, 2), (1, 2), (-1, 2), (0, 2), (-1, -2), (0, -2), (1, -2)]

# Holds the formula for the ellipse / closed region. 
# Can be split out if necessary. 
def formula(x, y):
    return ((x-2.5)/30)**2 + ((y - 2.5)/40)**2 - 1


def formula2(x,y):
    if (abs(x) < 2 and abs(y) < 2):
        return -1
    else:
        return 1


# Relying on formula, tests to see if a pair is in the region. 
# Returns True if yes, otherwise False. 
def inRegion(pair):
    (x, y) = pair
    if formula(x, y) < 0:
        return True
    else:
        return False

# given pair1 and pair2, uses inRegion to "walk"
# pairOne and pairTwo until we find the absolute borderline
# (minimum difference between pairOne and pairTwo)
# which is outside the region. 
# PairOne is assumed to be the point in the region, 
# pairTwo is assumed to be the point outside the region. 
# Returns the pair corresponding to the closest borderline. . 
def walkOut(pairOne, pairTwo):
    (x1, y1) = pairOne
    (x2, y2) = pairTwo

    midPoint = ((x1+x2) / 2.0, (y1+y2) / 2.0)
    # print(midPoint)

    if abs(x1 - x2) + abs(y1 - y2) <= 0.0000001: #precision modifier, up later
        return pairTwo

    if inRegion(midPoint):
        return walkOut(midPoint, pairTwo)
    else:
        return walkOut(pairOne, midPoint)

# print(inRegion((-20,18.5)))

# print(walkOut((-20, 28), (-20, 29)))
# print(walkOut((0,20), (40,20)))

xs = range(-27,33)
ys = range(-37,43)

# Center of ellipse is at (2.5, 2.5)
# Minor radius (x) is 30, major radius (y) is 40. 

# Given some x, finds the two y-values that lie on the border of the ellipse. 
# Returns them as the pair (less, greater), with precision to 3 decimal places. 
def ellipseSolverX(x):
    pointIn     = (x, 2.5)
    pointUp     = (x, 2.5 + 40)
    pointDown   = (x, 2.5 - 40)

    upperBound = walkOut(pointIn, pointUp)
    lowerBound = walkOut(pointIn, pointDown)

    return (lowerBound[1], upperBound[1])

def ellipseSolverY(y):
    pointIn     = (2.5, y)
    pointLeft   = (2.5 - 30, y)
    pointRight  = (2.5 + 30, y)

    leftBound = walkOut(pointIn, pointLeft)
    rightBound = walkOut(pointIn, pointRight)

    return (leftBound[0], rightBound[0])

# print("esy 20", ellipseSolverY(20))

# print(walkOut((2.5, 20), (32.5, 20)))


xDict = {}
yDict = {}

for x in xs:
    xDict[x] = ellipseSolverX(x)

for y in ys:
    yDict[y] = ellipseSolverY(y)


# newInRegion uses the lookup instead of manual calculation. 
# It only works with lattice points, which is what we want. 
def newInRegion(point):
    (x, y) = point

    try:
        (lowx, highx) = yDict[y]

        if lowx <= x <= highx:
            (lowy, highy) = xDict[x]
            if lowy <= y <= highy:
                return True
        else:
            return False
    except Exception:
        return False

# print(xDict[25])
# print(yDict[28])
# print(newInRegion((25,29)))

# walkStep takes a list of steps (coords of previous walks), and 
# appends another step onto it, using Random. 
# Returns the modified list of steps. 
def walkStep(steps):
    currSteps = steps
    (lastx, lasty) = steps[-1]
    directions = [(lastx+1, lasty), (lastx-1, lasty), (lastx, lasty+1), (lastx, lasty-1)]
    randInt = random.randint(0, 3)
    
    newPath = currSteps + [directions[randInt]]
    # print(newPath)
    return newPath

# given a single step, gets the next step. 
# should be much easier on memory and computation. 
# returns a single step. 
def walkSingleStep(lastStep):
    (lastx, lasty) = lastStep
    directions = [(lastx+1, lasty), (lastx-1, lasty), (lastx, lasty+1), (lastx, lasty-1)]
    randInt = random.randint(0, 3)
    return directions[randInt]

# Given a list of steps, checks if the last two steps allowed 
# our bug to cross over some food. 
# Returns Boolean T/F. 
def checkFood(steps):
    lastStep = steps[-1]

    if not inRegion(lastStep):
        return True
    else:
        return False

# walkPath does a full path simulation. It walks a path
# until it finds a food particle, then returns as an int
# the number of steps necessary to get to that state. 
# EDIT: Now returns the raw distance, in cm travelled, by the ant. 
def walkPath():
    startPoint = (0,0)
    currentPath = [startPoint]

    isDone = False
    while not isDone:
        currentPath.append(walkSingleStep(currentPath[-1]))
        # print(currentPath)
        isDone = not inRegion(currentPath[-1])
    (lastix, lastiy) = walkOut(currentPath[-1], currentPath[-2])
    (last2x, last2y) = currentPath[-2]
    lastStepVal = abs(lastix - last2x) + abs(lastiy - last2y)
    return 10 * ((len(currentPath) - 1) + lastStepVal)



def newWalkPath():
    startPoint = (0,0)
    currentPath = [startPoint]

    while newInRegion(currentPath[-1]):
        currentPath.append(walkSingleStep(currentPath[-1]))
        # print(currentPath)

    (last1x, last1y) = currentPath[-1]
    (last2x, last2y) = currentPath[-2]

    if last1x == last2x:
        (lowy, highy) = xDict[last1x]
        lastStepVal = min(last1y - lowy, last1y - highy)
    else:
        (lowx, highx) = yDict[last1y]
        lastStepVal = min(last1x - lowx, last1x - highx)
    # print(currentPath)
    return 10 * ((len(currentPath) - 1) + lastStepVal)



# TESTS AND EXECUTION BELOW

# print(newWalkPath())

if True:

    # testPath = [(0,0), (1,0)]

    # print(walkStep(testPath))

    # walkPath()

    # trials = []

    # for i in range(4000):
    #     trials.append(walkPath())
    #     if i % 500 == 0:
    #         print(i)

    # print(float(sum(trials)) / len(trials))

    # endTime = datetime.datetime.now()

    # print("Elapsed time:", endTime - startTime)

    # 11644.965 -- 1 M
    # 11651.097 -- 1 M
    # 11642.764 -- 4 M
    # 11640.811 -- 40 M


    sumValues = 0
    numTrials = 0

    for i in range(1000):
        sumValues += newWalkPath()
        numTrials += 1
        if i % 100000 == 0:
            print(i)

    print(float(sumValues / numTrials))

    newEndTime = datetime.datetime.now()

    print("New elapsed time:", newEndTime - startTime)

    # 11329.818 -- 400 K -- 7:10
    # 11330.370 -- 40 M  -- 13:44:30
    # 11316.102 -- 400 K -- 7:10
    # 11327.590 -- 40 M  -- 12:00:55
