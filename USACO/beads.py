"""
ID: colinya1
LANG: PYTHON3
TASK: beads
"""

fin = open("beads.in", "r")
fout = open("beads.out", "a")

n = int(fin.readline().strip())
necklace = fin.readline().strip()

print(n)
print(necklace[0:])

def evaluate(stringIn):
    """stringIn represents a necklace that has already been broken. 
    We read from the beginning to the right, and then from the end to the left. 
    Returns int, which is number of beads which can be legally taken."""

    numBeads = 0
    startColor = "w"
    endColor = "w"

    sameColor = True

    while sameColor:
        for char in stringIn:
            if startColor == "w":
                startColor = char
            
            if char == "w":
                numBeads += 1
            elif startColor == char:
                numBeads += 1
            else:
                sameColor = False
                break
        break
    
    sameColor = True
    
    stringBack = stringIn[numBeads:][::-1]
    while sameColor:
        for char in stringBack:
            if endColor == "w":
                endColor = char
            
            if char == "w":
                numBeads += 1
            elif endColor == char:
                numBeads += 1
            else:
                sameColor = False
                break
        break
    return numBeads

maxNum = 0
for i in range(n):
    newNeck = necklace[i:] + necklace[:i]
    print(newNeck)
    newMax = evaluate(newNeck)
    if newMax > maxNum:
        maxNum = newMax

print(maxNum)
fout.write(str(maxNum) + "\n")