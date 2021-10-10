"""
ID: colinya1
LANG: PYTHON3
TASK: ride
"""

fin = open("ride.in", "r")
fout = open("ride.out", "w")

x = fin.readline()
y = fin.readline()

letterString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(len(x), len(y))

x = x[:-1]
y = y[:-1]

print(len(x), len(y))


mult1 = 1
mult2 = 1

# x = "COMETQ"
# y = "HVNGAT"


print(x, y)

for l in list(x):
    mult1 *= letterString.index(l) + 1
    print(mult1)

for l in list(y):
    print(l)
    mult2 *= letterString.index(l) + 1

# print(mult1, mult2)
print(mult1)
print(mult2)


if (mult1 % 47) == (mult2 % 47):
    fout.write("GO\n")
else:
    fout.write("STAY\n")

fout.close()