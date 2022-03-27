# Advent Day 9

with open('day9real.txt') as ipf:
    lines = ipf.readlines()

depths = []

for l in lines:
    row = []
    for i in range(len(l) - 1):
        row.append(int(l[i]))
    depths.append(row)

height = len(depths)
width = len(depths[0])

# introducing numbering scheme: ID# for (x, y) = y * width + x
# x, y starts at 0,0 for top left, maxes at bot right. 

def getID(x, y):
    return y * width + x

def fromID(i):
    return [i % width, i // width]

root_dict = {}

def populate_roots():
    for i in range(height):
        for j in range(width):
            curr_val = depths[i][j]
            # is_root = true
            if not (i == 0):
                up_val = depths[i-1][j]
                if up_val < curr_val:
                    # is_root = false
                    continue
            if not (i == height - 1):
                down_val = depths[i+1][j]
                if down_val < curr_val:
                    continue
            if not (j == 0):
                left_val = depths[i][j-1]
                if left_val < curr_val:
                    continue
            if not (j == width - 1):
                right_val = depths[i][j+1]
                if right_val < curr_val:
                    continue
            root_dict[getID(j, i)] = []

def checkself(x, y, root):
    self_value = depths[y][x]
    root_list = root_dict[root]
    is_valid = True
    if self_value == 9:
        is_valid = False
    else:
        self_ID = getID(x, y)
        if self_ID in root_list:
            is_valid = False
        else:
            root_list.append(self_ID)
    root_dict[root] = root_list
    return is_valid

def propagate(x, y, root):
    checkself(x, y, root)

    if not (x == 0):
        valid = checkself(x - 1, y, root)
        if valid:
            propagate(x - 1, y, root)
    if not (x == width - 1):
        valid = checkself(x + 1, y, root)
        if valid:
            propagate(x + 1, y, root)
    if not (y == 0):
        valid = checkself(x, y - 1, root)
        if valid:
            propagate(x, y - 1, root)
    if not (y == height - 1):
        valid = checkself(x, y + 1, root)
        if valid:
            propagate(x, y + 1, root)

populate_roots()

print(root_dict)

for r in root_dict.keys():
    [x, y] = fromID(r)
    propagate(x, y, r)

# print(root_dict)

lengths = []

for v in root_dict.values():
    lengths.append(len(v))

lengths.sort()

print(lengths)

# roots = [[-1] * width for i in range(height)]

# for d in depths:
#     print(d)

# for r in roots:
#     print(r)

# def findhead(x, y):
#     value = depths[y][x]
#     if value == 9:
#         roots[y][x] = -2
#         return -2
#     elif value == 0:
#         roots[y][x] = y * width + x
#     else:
#         hastop   = not (y == 0)
#         hasbot   = not (y == height - 1)
#         hasright = not (x == width - 1)
#         hasleft  = not (x == 0)

        # list contains top, bot, left, right if extant, -1 otherwise


