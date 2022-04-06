# adventDayNine.py

# advanced fluid / gas modeling with python. 
# jk, we're just doing some brute-force bashing. 

with open('input9.txt') as ipf:
    lines = ipf.readlines()

# FOR TESTING PURPOSES
# lines = [
# "2199943210",
# "3987894921",
# "9856789892",
# "8767896789",
# "9899965678"]


lines = [l[:-1] for l in lines] # REPLACE WHEN IN PROD

hdist = len(lines[0])
vdist = len(lines)

digMap = [ list(l) for l in lines]

isLowMap = [([True] * hdist) for v in range(vdist)]

# print(isLowMap)

# ------ PART ONE ------

for i in range(vdist):
    # check right side
    for j in range(hdist - 1):
        ovalue = digMap[i][j]
        nvalue = digMap[i][j+1]
        if ovalue >= nvalue:
            isLowMap[i][j] = False

    # check left side
    for j in range(1, hdist):
        ovalue = digMap[i][j]
        nvalue = digMap[i][j-1]
        if ovalue >= nvalue:
            isLowMap[i][j] = False

for j in range(hdist):
    # check top side
    for i in range(1, vdist):
        ovalue = digMap[i][j]
        nvalue = digMap[i-1][j]
        if ovalue >= nvalue:
            isLowMap[i][j] = False

    # check bot side
    for i in range(vdist - 1):
        ovalue = digMap[i][j]
        nvalue = digMap[i+1][j]
        if ovalue >= nvalue:
            isLowMap[i][j] = False

values = []
botPoints = []

for i in range(vdist):
    for j in range(hdist):
        if isLowMap[i][j]:
            # print("(" + str(i) + ", " + str(j) + ")", digMap[i][j])
            values.append(int(digMap[i][j]))
            botPoints.append((i, j))

# print(sum(values) + len(values))


# ------ PART TWO ------

def mpget(pair):
    # given a pair, gets it from the map. 
    (x, y) = pair
    return digMap[x][y]

def getAdjCoords(pair):
    # given a coord pair, gets the coords of all adjacents. 
    # returns a list of all such ordered pairs. 
    coordList = []

    (x, y) = pair

    if x == 0:
        coordList.append((1, y))
    elif x == vdist - 1:
        coordList.append((x-1, y))
    else:
        coordList.append((x-1, y))
        coordList.append((x+1, y))

    if y == 0:
        coordList.append((x, 1))
    elif y == hdist - 1:
        coordList.append((x, y-1))
    else:
        coordList.append((x, y-1))
        coordList.append((x, y+1))
    
    return coordList

def inBasin(point, basinpoints):
    # given point and set of points in basin, evaluate if a point is in the basin. 
    padjs = getAdjCoords(point)
    if mpget(point) == '9':
        return False
    
    for p in padjs:
        if not p in basinpoints:
            if mpget(point) >= mpget(p):
                return False
    
    return True

def evalBasin(point):
    # given some point, gets the rest of the points of the basin. 
    # returns points in basin. 
    
    basinPts = {point}
    basinCandidates = set(getAdjCoords(point))

    while not len(basinCandidates) == 0:
        # print("bac:", basinCandidates)

        newCandidates = set([])
        
        for p in basinCandidates:
            # print("checking", p, "resulted in", inBasin(p, basinPts))
            if inBasin(p, basinPts):
                basinPts.add(p)
                newCandidates = newCandidates.union(set(getAdjCoords(p)).difference(basinPts))
                # print("nc is", newCandidates)

        basinCandidates = newCandidates

    # print("Basin points for", point, "are", basinPts)
    return((basinPts))

basinSizes = list(map((lambda x: len(evalBasin(x))), botPoints))

print("bsizes", basinSizes)

bsizes = sorted(basinSizes)

print(bsizes[-1] * bsizes[-2] * bsizes[-3])

# print(hdist, vdist)
# print(getAdjCoords((0,9)))

# valList = []
# for p in botPoints:
#     basinpts = evalBasin(p)
#     valList.append([mpget(b) for b in basinpts])

# for v in valList:
#     print(v)