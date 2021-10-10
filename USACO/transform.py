"""
ID: colinya1
LANG: PYTHON3
TASK: transform
"""

fin = open("transform.in", "r")
fout = open("transform.out", "w")

n = int(fin.readline().strip())

original = []
transformed = []

for i in range(n):
    original.append(fin.readline().strip())

for i in range(n):
    transformed.append(fin.readline().strip())

# note that for both, we have a list of lines, so we specify the line, then column for each entry. 

def rotateOne(inputSquare):
    """takes a list of lists - input square, then rotates it once
    clockwise. Returns the resulting rotated array."""
    outputSquare = []
    
    for i in range(n):
        subRow = ""
        for j in range(n):
            subRow += inputSquare[n - j - 1][i]
        outputSquare.append(subRow)
    return outputSquare

def flipH(inputSquare):
    """takes a list of lists - input suare, then flips it once
    horizontally, across a y-axis. Returns the resulting flipped array. """
    outputSquare = []

    for i in range(n):
        subRow = ""
        for j in range(n):
            subRow += inputSquare[i][n - j - 1]
        outputSquare.append(subRow)
    return outputSquare

outputValue = 0

if rotateOne(original) == transformed:
    outputValue = 1
elif rotateOne(rotateOne(original)) == transformed:
    outputValue = 2
elif rotateOne(rotateOne(rotateOne(original))) == transformed:
    outputValue = 3
else:
    flipper = flipH(original)
    if flipper == transformed:
        outputValue = 4
    else:
        print(rotateOne(flipper))
        print(transformed)
        print(rotateOne(flipper) == transformed)
        if rotateOne(flipper) == transformed:
            outputValue = 5
        elif rotateOne(rotateOne(flipper)) == transformed:
            outputValue = 5
        elif rotateOne(rotateOne(rotateOne(flipper))) == transformed:
            outputValue = 5

if outputValue == 0:
    if original == transformed:
        outputValue = 6
    else:
        outputValue = 7

fout.write(str(outputValue) + "\n")
