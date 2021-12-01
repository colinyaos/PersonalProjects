# AdventDayOne.py

# counts number of instances in which a number is greater than the preceding number. 

with open('input1.txt') as ipf:
    lines = ipf.readlines()

ints = []

for l in lines:
    ints.append(int(l[0:-1]))

total = 0

for i in range(len(ints) - 3):
    window1 = ints[i] + ints[i+1] + ints[i+2]
    window2 = ints[i+1] + ints[i+2] + ints[i+3]
    if window1 < window2:
        total += 1

print(total)