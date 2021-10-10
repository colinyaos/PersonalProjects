"""
ID: colinya1
LANG: PYTHON3
TASK: barn1
"""

fin = open("barn1.in", "r")
fout = open("barn1.out", "w")

inputLine = fin.readline().strip().split()

m = int(inputLine[0])
s = int(inputLine[1])
c = int(inputLine[2])

occupiedNumbers = []
for i in range(c):
    newChar = fin.readline().strip()
    print(newChar)
    occupiedNumbers.append(int(newChar))

occupiedNumbers.sort()

# m = 4
# occupiedNumbers = [3, 4, 6, 8, 14, 15, 16, 17, 21, 25, 26, 27, 30, 31, 40, 41, 42, 43]

gapList = []
truthValue = False
currValue = -1

for n in range(len(occupiedNumbers) - 1):
    thisValue = occupiedNumbers[n]
    thatValue = occupiedNumbers[n+1]
    if not thatValue - thisValue == 1:
        gapList.append([thisValue, thatValue])

print(gapList)

lengthList = []

for g in gapList:
    lengthList.append(g[1] - g[0] - 1)

print(lengthList)

chunks = len(lengthList) + 1

extraBoards = chunks - m

sLengthList = sorted(lengthList)

eBoardLength = 0

for s in range(extraBoards):
    eBoardLength += sLengthList[s]

print(eBoardLength)

print(eBoardLength)

fout.write(str(eBoardLength + c) + "\n")