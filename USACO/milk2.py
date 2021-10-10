"""
ID: colinya1
LANG: PYTHON3
TASK: milk2
"""

fin = open("milk2.in", "r")
fout = open("milk2.out", "w")

n = int(fin.readline().strip())
lines = []

for i in range(n):
    lines.append(fin.readline().strip())

lineslist = []
for i in range(n):
    lineslist.append(lines[i].split())

for ll in lineslist:
    ll[0] = int(ll[0])
    ll[1] = int(ll[1])

startTimes = []
endTimes = []

for littleList in lineslist:
    startTimes.append(littleList[0])
    endTimes.append(littleList[1])


veryStartTime = min(startTimes)
veryEndTime = max(endTimes)

for littleList in lineslist:
    littleList[0] -= veryStartTime
    littleList[1] -= veryStartTime
#The above is used to scale the times, so the earliest is now 0. 

sortedLines = sorted(lineslist, key = lambda x: x[0])

for entry in sortedLines:
    print(entry)


mergers = 0

pointer = 0

print("let's do a thing")

if not n < 2:
    for i in range(n-1):
        # print("looking for", pointer, (pointer + 1))
        if sortedLines[pointer][1] >= sortedLines[pointer + 1][0]:
            sortedLines[pointer][1] = max(sortedLines[pointer][1], sortedLines.pop(pointer + 1)[1]) 
            #sets upper to max of both, then removes the second
            mergers += 1
        else:
            pointer += 1

intervals = sortedLines
    


# for ll in lineslist:
#     print(ll)
#     tempStart = ll[0]
#     tempEnd = ll[1]
#     if len(intervals) == 0:
#         intervals.append(ll)
#     else:
#         changeMade = False
#         for i in intervals:
#             intervalStart = i[0]
#             intervalEnd = i[1]
#             if tempStart < intervalStart and tempEnd >= intervalStart:# start is before, so we can add
#                 changeMade = True
#                 i[0] = tempStart
#                 if tempEnd > intervalEnd:
#                     i[1] = tempEnd
#             elif tempStart <= intervalEnd and tempEnd >= intervalEnd: # start may be before, but end is certainly after
#                 # print("This was called, right?")
#                 i[1] = tempEnd
#                 changeMade = True
#             elif tempStart >= intervalStart and tempEnd <= intervalEnd: #entirely contained
#                 break
#         if changeMade == True:
#             mergers += 1
#         if changeMade == False:
#             intervals.append(ll)
#     print("intervals is", intervals)

print(mergers)

print(intervals)

listLens = [ll[1] - ll[0] for ll in lineslist]

longestLen = max(listLens)


unSortList = sorted(intervals, key = lambda x: x[0])
longestUnLen = 0

print(unSortList)

for i in range(len(unSortList) - 1):
    diff = unSortList[i+1][0] - unSortList[i][1]
    if diff > longestUnLen:
        longestUnLen = diff

def wasted(): 
    
    # superList = [False] * (veryEndTime - veryStartTime)

    # for littleList in lineslist:
    #     for i in range(littleList[1] - littleList[0]):
    #         superList[littleList[0] + i] = True

    # longestLen = 0
    # longestUnLen = 0

    # tempLen = 0
    # tempUnLen = 0

    # for i in superList:
    #     if i == True:
    #         tempLen += 1
    #         if tempLen > longestLen:
    #             longestLen = tempLen
    #         tempUnLen = 0
    #     else:
    #         tempLen = 0
    #         tempUnLen += 1
    #         if tempUnLen > longestUnLen:
    #             longestUnLen = tempUnLen

    # print(longestLen, longestUnLen)
    return None


fout.write(str(longestLen) + " " + str(longestUnLen) + "\n")




# dictList = []

# for i in range(n):
#     dictList.append({lineslist[i][0]:lineslist[i][1]})

