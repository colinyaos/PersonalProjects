# adventDaySix.py

# Using cutting-edge technology, we estimate the rate at which a lanternfish population grows,
# thanks to some unfounded assumptions and basic calculations. 



with open('input6.txt') as ipf:
    lines = ipf.readlines()

listfish = [int(x) for x in lines[0].split(",")]

def iterate(inlist):
    updatedlist = [x-1 for x in inlist]

    numfishspawned = updatedlist.count(-1)

    adjustedlist = [6 if x < 0 else x for x in updatedlist] + [8] * numfishspawned

    return adjustedlist

finalList = listfish

for i in range(80):
    finalList = iterate(finalList)

# print(len(finalList))

# --- PART TWO

finalList = listfish

fishDict = {n:finalList.count(n) for n in set(finalList)}

# print(fishDict)

# def iter(dict):
#     # takes a dict and steps it forward. 
#     stepDict = {(d-1):dict[d] for d in dict.keys()}
#     # print("step", stepDict)
#     try:
#         newfish = stepDict.pop(-1)
#         stepDict[6] = stepDict[6] + newfish
#         stepDict[8] = newfish
#     except Exception as e:
#         # print(e)
#         pass
#     return stepDict


# fishDict[6] = 0
# fishDict[7] = 0 
# fishDict[8] = 0

# print(fishDict)

# for i in range(16):
#     fishDict = iter(fishDict)
#     # print(fishDict)


# print(sum(fishDict.values()))

newList = [0] + fishDict.values() + [0, 0, 0]

def step(inList):
    fst = inList[0]
    snd = inList[1:]
    outList = snd + [fst]
    outList[6] += fst
    return outList

# print(newList)

for i in range(256):
    # print(newList)
    newList = step(newList)

print(sum(newList))