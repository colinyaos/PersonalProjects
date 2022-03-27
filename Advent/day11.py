# day11.py

with open('day11real.txt') as ipf:
    lines = ipf.readlines()

octos = []

for l in lines:
    row = []
    for i in range(len(l) - 1):
        row.append(int(l[i]))
    octos.append(row)

height = len(octos)
width = len(octos[0])

def display_array(a):
    for row in a:
        for i in row:
            if not i == 0:
                print(i, end = "")
            else:
                print(" ", end = "")
        print()

def charge():
    for i in range(height):
        for j in range(width):
            octos[i][j] += 1

def flash_one(x, y):
    hastop = not (y == 0)
    hasbot = not (y == height - 1)
    haslef = not (x == 0)
    hasrig = not (x == width - 1)

    if hastop:
        octos[y-1][x] += 1
        if hasrig:
            octos[y-1][x+1] += 1
        if haslef:
            octos[y-1][x-1] += 1
    if hasbot:
        octos[y+1][x] += 1
        if hasrig:
            octos[y+1][x+1] += 1
        if haslef:
            octos[y+1][x-1] += 1
    if haslef:
        octos[y][x-1] += 1
    if hasrig:
        octos[y][x+1] += 1
    
def find_flashed():
    has_flashed = []

    for i in range(height):
        for j in range(width):
            if octos[i][j] > 9:
                has_flashed.append([j, i])
    
    return has_flashed


def flash(l):
    has_flashed = find_flashed()

    new_flashes = len(has_flashed)
    # print(has_flashed)
    if len(has_flashed) == 0:
        return 0

    for h in has_flashed:
        [x, y] = h
        flash_one(x, y)

    has_flashed = has_flashed + l
    for h in has_flashed:
        [x, y] = h
        octos[y][x] = 0
    
    return new_flashes + flash(has_flashed)


def step():
    charge()
    flashes = flash([])
    # display_array(octos)
    return flashes

total = 0

for i in range(500):
    new_flashes = step()
    if new_flashes == 100:
        print(i)
    total += new_flashes

# display_array(octos)

print(total)