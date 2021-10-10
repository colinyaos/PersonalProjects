"""
ID: colinya1
LANG: PYTHON3
TASK: combo
"""

fin = open("combo.in", "r")
fout = open("combo.out", "w")

n = int(fin.readline().strip())

john = [int(x) for x in fin.readline().split()]

master = [int(x) for x in fin.readline().split()]

# john = [1, 2, 3]

# master = [5, 6, 7]

# def loosedigits(x):
#     """ given integer x, return list of integers that can be exchanged with x."""

#     temp = x - 1

#     output = []

#     for i in [-2, -1, 0, 1, 2]:
#         output.append((temp + i)%100 + 1)
    
#     return output

def dist(p1, p2, n):
    """ finds distance between p1 and p2 in base n"""
    d1 = abs(p2 - p1)
    return min(d1, n - d1)

dist1 = dist(master[0], john[0], n)
dist2 = dist(master[1], john[1], n)
dist3 = dist(master[2], john[2], n)

ranges = {4:1, 3:2, 2:3, 1:4, 0:5}

possibles = 1

if dist1 in ranges.keys():
    possibles = possibles * (5 - dist1)
else:
    possibles = 0

if dist2 in ranges.keys():
    possibles = possibles * (5 - dist2)
else:
    possibles = 0

if dist3 in ranges.keys():
    possibles = possibles * (5 - dist3)
else:
    possibles = 0

print(possibles)

output = 250 - possibles

if n <= 5:
    output = n * n * n

fout.write(str(output) + "\n")

# johnpossibles = []

# for i in loosedigits(john[0]):
#     for j in loosedigits(john[1]):
#         for k in loosedigits(john[2]):
#             johnpossibles.append([i, j, k])

# masterpossibles = []

# for i in loosedigits(master[0]):
#     for j in loosedigits(master[1]):
#         for k in loosedigits(master[2]):
#             masterpossibles.append([i, j, k])

# both = set(johnpossibles) & set(masterpossibles)

# print(len(both))