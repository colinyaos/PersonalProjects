# adventDaySeven.py

# counts crabs, determines optimal mean. 

with open('input7.txt') as ipf:
    lines = ipf.readlines()

listcrabs = [int(x) for x in lines[0].split(",")]

# --- PART ONE

# mean = (sum(listcrabs) / len(listcrabs))

# totfuel = sum(map((lambda x: abs(x - mean)), listcrabs))

def calcfuel(listIn, point):
    return sum(map((lambda x: abs(x - point)), listIn))

# print(totfuel)

fuelList = [calcfuel(listcrabs, i) for i in range(max(listcrabs))]

print(min(fuelList))

# ---- PART TWO

def newcalcfuel(listIn, point):
    distances = map((lambda x: abs(x - point) ), listIn)
    fuelcosts = map((lambda x: x*(x+1) / 2), distances)
    return sum(fuelcosts)

newFuelList = [newcalcfuel(listcrabs,i) for i in range(max(listcrabs))]

print(min(newFuelList))
