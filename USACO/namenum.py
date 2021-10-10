"""
ID: colinya1
LANG: PYTHON3
TASK: namenum
"""

fin = open("namenum.in", "r")
fout = open("namenum.out", "w")

with open("dict.txt", "r") as nameDict:
    givenNames = nameDict.readlines()

givenNames = [x.strip() for x in givenNames]

n = fin.readline().strip()

numList = [] #list of nums that makes up our input

for i in range(len(n)):
    numList.append(int(n[i]))

keypadList = [[], [], ["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["J", "K", "L"], ["M", "N", "O"], ["P", "R", "S"], ["T", "U", "V"], ["W", "X", "Y"]]

goodNamesSoFar = []

for name in givenNames:
    if len(name) == len(numList):
        goodNamesSoFar.append(name)

for i in range(len(numList)):
    # print(i)
    # print(numList[i])
    goodLetters = keypadList[numList[i]]
    namesToKeep = []

    bananavar = 0
    for name in goodNamesSoFar:
        bananavar += 1
        # print(name)
        # print(bananavar, name[2], name)
        if name[i] in goodLetters:
            namesToKeep.append(name)
        # print("You're pretty good")
    goodNamesSoFar = namesToKeep

if len(goodNamesSoFar) == 0:
    fout.write("NONE\n")
else:
    for name in goodNamesSoFar:
        fout.write(name + "\n")

