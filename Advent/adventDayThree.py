# adventDayThree.py

# Takes in binary representations of numbers,
# Then performs the specified transformations 
# to get "gamma" and "epsilon" rates. 

with open('input3.txt') as ipf:
    lines = ipf.readlines()

for i in range(len(lines)):
    lines[i] = [int(c) for c in lines[i][:-1]]

tot = len(lines)
width = len(lines[0])

# PART ONE

gamma = ""
epsilon = ""

for w in range(width):
    count1 = 0
    for t in range(tot):
        if lines[t][w] == 1:
            count1 += 1
    if count1 * 2 >= tot:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

# print(gamma, epsilon)

gb, eb = int(gamma, 2), int(epsilon, 2)

# print(gb, eb, gb * eb)

# PART TWO

oxyrat = lines
co2rat = lines

for w in range(width):
    print("loxy", len(oxyrat))
    if len(oxyrat) == 1:
        break
    
    num1 = 0
    for o in oxyrat:
        if o[w] == 1:
            num1 += 1
    if num1 * 2 >= len(oxyrat):
        mostpop = 1
    else:
        mostpop = 0

    oxyrat = [x for x in filter(lambda l: l[w] == mostpop, oxyrat)]

for w in range(width):
    print("lco2", len(co2rat))
    if len(co2rat) == 1:
        break

    num1 = 0
    for c in co2rat:
        if c[w] == 1:
            num1 += 1
    if num1 * 2 >= len(co2rat):
        leastpop = 0
    else:
        leastpop = 1
    
    co2rat = [x for x in filter(lambda l: l[w] == leastpop, co2rat)]



print(oxyrat, co2rat)

ostr = "".join([str(x) for x in oxyrat[0]])
cstr = "".join([str(x) for x in co2rat[0]])

ob = int(ostr, 2)
cb = int(cstr, 2)

print(ob, cb, ob*cb)