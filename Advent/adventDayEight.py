# adventDayEight.py

# counts digits on an outdated display. 

with open('input8.txt') as ipf:
    lines = ipf.readlines()

# ---- PART ONE

lastDigits = [l.split("| ")[1][:-1] for l in lines]

# print(lastDigits[1:5])

ldWordList = [d.split() for d in lastDigits]

# print(ldWordList[1:5])

oneCount = 0
fourCount = 0
sevenCount = 0
eightCount = 0

for ld in ldWordList:
    for word in ld:
        if len(word) == 2:
            oneCount += 1
        elif len(word) == 4:
            fourCount += 1
        elif len(word) == 3:
            sevenCount += 1
        elif len(word) == 7:
            eightCount += 1

# print(oneCount, fourCount, sevenCount, eightCount, sum([oneCount, fourCount, sevenCount, eightCount]))



# ---- PART TWO

# Some work with pencil and paper reveals the following...

# The c-f pair can be identified immediately by looking for which number is 1. 
# c occurs in 8 of the numbers, while f occurs in 9, so c and f can be distinguished. 
# Similarly, e occurs in 4 of the numbers, which is unique, so e can be found. 
# b occurs in 6 of the numbers, also unique, so b can be found. 
# a is also found in 8 of the numbers, so because c is found, a is found as well. 
# 
# Differentiating d and g is more difficult. Perhaps the best solution is to differentiate 0 and 9, then work accordingly. 

def identifyLetters(line):
    # given some line, figure out what's what. 
    # returns list of chars which correspond to the real chars, 
    # in abcdefg order. 

    [fst, snd] = line.split("|")
    words = fst.split()
    bars = range(1, 8)

    letterDict = {}

    for c in "abcdefg":
        letterDict[c] = fst.count(c)

    # print(letterDict)

    onerep = list(filter((lambda w: len(w) == 2), words))[0]
    
    if letterDict[onerep[0]] == 8:
        # then it's c. 
        bars[2] = onerep[0]
        bars[5] = onerep[1]
    else:
        bars[2] = onerep[1]
        bars[5] = onerep[0]

    # c and f are now assigned. 

    bars[4] = letterDict.keys()[letterDict.values().index(4)] # assigning e
    bars[1] = letterDict.keys()[letterDict.values().index(6)] # assigning b

    sevenrep = list(filter((lambda w: len(w) == 3), words))[0]
    bars[0] = list(filter((lambda x: x not in onerep), sevenrep))[0] # assigning a

    fourrep = list(filter((lambda w: len(w) == 4), words))[0]
    bars[3] = list(filter((lambda x: x not in (onerep + bars[1])), fourrep))[0] # assigning d

    bars[6] = list(filter((lambda x: x not in bars), letterDict.keys()))[0] # assigning g

    return(bars)

numbers = []

def matchseq(foo):
    # Given some input string, match it with the value in valdict. Returns the proper digit. 
    valdict = {"abcdefg": 8,
        "abdfg": 5,
        "acdeg": 2,
        "acdfg": 3,
        "acf": 7,
        "abcdfg": 9,
        "abdefg": 6,
        "bcdf": 4,
        "abcefg": 0,
        "cf": 1}

    return(valdict["".join(sorted(foo))])

def subword(ldict, oldword):
    # given dict of char to char and the old word, output the new word.
    newword = ""
    for c in oldword:
        newword += ldict[c]
    return newword


# for i in range(5):
#     print(identifyLetters(lines[i]))


totsum = 0

for i in range(len(lines)):
    # print(i)
    l2ldict = dict(zip(identifyLetters(lines[i]), list("abcdefg")))
    # print(l2ldict)

    newwords = [subword(l2ldict, w) for w in ldWordList[i]]

    # print(["".join(sorted(w)) for w in newwords])
    newdigs = [matchseq(w) for w in newwords]

    newsum = 1000 * newdigs[0] + 100 * newdigs[1] + 10 * newdigs[2] + newdigs[3]
    totsum += newsum
    # print(newsum)

print(totsum)
