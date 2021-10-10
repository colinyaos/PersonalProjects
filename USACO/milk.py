"""
ID: colinya1
LANG: PYTHON3
TASK: milk
"""

fin = open("milk.in", "r")
fout = open("milk.out", "w")

inputLine = fin.readline().strip().split()

demand = int(inputLine[0])

numSupply = int(inputLine[1])

suppliers = []

for i in range(numSupply):
    supplyLine = fin.readline().strip().split()
    newList = [int(x) for x in supplyLine]
    suppliers.append(newList)

suppliers = sorted(suppliers, key = lambda x: x[0])

totalCost = 0

while not demand == 0:
    currentSup = suppliers.pop(0)
    if demand >= currentSup[1]:
        demand -= currentSup[1]
        totalCost += currentSup[1] * currentSup[0]
    else:
        totalCost += demand * currentSup[0]
        demand = 0

fout.write(str(totalCost) + "\n")