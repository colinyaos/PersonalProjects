# adventDayFour.py

# Take in a list of bingo numbers, and a bunch of bingo boards. 
# Identify the winning board, and find the sum of unused numbers
# on that board. 

with open('input4.txt') as ipf:
    lines = ipf.readlines()

bingonums = [int(x) for x in lines[0].split(",")]

# print(bingonums) # bingonums now contains all the numbers in order as ints. 

boards = []
for i in range(2, len(lines), 6):
    boards.append(lines[i:i+5])
# print(boards[-1])

def formatBoard(inList):
    outList = []
    for row in inList:
        outList.append([int(x) for x in row[:-1].split()])
    return outList

boards = [b for b in map(formatBoard, boards)]

# print(boards[1]) # boards is now a list of boards. 
# each "board" is a list of rows, where each row is a list of ints. 

def evalBoard(nums, board):
    # given a list of nums and the board, 
    # evaluate if the board is winning or not. 
    # returns bool T/F. 

    rows = board
    columns = []

    for i in range(5):
        column = []
        for r in rows:
            column.append(r[i])
        columns.append(column)
    # print(rows)
    # print(columns)

    rowsIn = [list(map((lambda x: x in nums), r)) for r in rows]
    colsIn = [list(map((lambda x: x in nums), c)) for c in columns]

    # print(rowsIn)
    # print(colsIn)

    completeRows = list(map(all, rowsIn))
    completeCols = list(map(all, colsIn))

    if any(completeRows) or any(completeCols):
        return True
    else:
        return False

# print(evalBoard(range(65), boards[2]))

# ---- PART ONE

inits = [bingonums[:n] for n in range(len(bingonums)+1)]

successes = [[evalBoard(i, b) for b in boards] for i in inits]

anysucc = list(map(any, successes))

# print(anysucc)

# print(anysucc.index(True))

# print(inits[26])

goodboards = [evalBoard(inits[26], b) for b in boards]

# print(goodboards)

# print(goodboards.index(True))

# print(goodboards[63])

# print(boards[63])

filledBoard = [list(map((lambda x: "X" if (x in inits[26]) else x), r)) for r in boards[63]]

# print(filledBoard)

sumBoard = [list(map((lambda x: 0 if (x in inits[26]) else x), r)) for r in boards[63]]

totalsum = sum(sum(x) for x in sumBoard)

# print(totalsum * inits[26][-1])

# ----- PART TWO

allsucc = list(map(all, successes))

# print(allsucc.index(True)) # this was 86

anygoodboard = [evalBoard(inits[85], b) for b in boards]

# print(anygoodboard.index(False)) # this was 13

filledBoard2 = [list(map((lambda x: "X" if (x in inits[85]) else x), r)) for r in boards[13]]

# print(filledBoard2)

sumBoard2 = [list(map((lambda x: 0 if (x in inits[86]) else x), r)) for r in boards[13]]

print(sumBoard2, inits[86][-1])

totalsum2 = sum(sum(x) for x in sumBoard2)

print(totalsum2 * inits[86][-1])

