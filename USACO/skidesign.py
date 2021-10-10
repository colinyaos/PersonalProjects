"""
ID: colinya1
LANG: PYTHON3
TASK: skidesign
"""

fin = open("skidesign.in", "r")
fout = open("skidesign.out", "w")

n = int(fin.readline().strip())

heights = []

for i in range(n):
    heights.append(int(fin.readline().strip()))


# heights = [1, 1, 17, 17, 27]

print("heights is", heights)

### Below here is the crappy dumb first attempt at an algorithm
### The idea is to search over every interval of 17, and trim everything to match
### Then, it's a simple matter of computing weights

costs = []

for i in range(84):
    lowest = i
    highest = i + 17
    tempCost = 0

    for h in heights:
        if h > highest:
            tempCost += (h - highest) ** 2
        elif h < lowest:
            tempCost += (h - lowest) ** 2
    
    costs.append(tempCost)

minCost = min(costs)

print("mincost is", minCost)

print("at:", costs.index(minCost))

fout.write(str(minCost) + "\n")
