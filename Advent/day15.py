# day15.py

with open('day15real.txt') as ipf:
    lines = ipf.readlines()

risk_map = []

for l in lines:
    row = []
    for c in l:
        if not c == "\n":
            row.append(int(c))
    risk_map.append(row)

# For the second map
new_map = []

for i in range(5):
    for l in lines:
        row = []
        for j in range(5):
            for c in l:
                if not c == "\n":
                    row.append((int(c) + i + j - 1) % 9 + 1)
        new_map.append(row)

# print(new_map[-1])
risk_map = new_map

height = len(risk_map)
width = len(risk_map[0])

# print(risk_map[0])

def display_array(a):
    for row in a:
        for i in row:
            print(i, end = " ")
        print()

# display_array(risk_map)

cumul_map = []
for i in range(height):
    row = []
    for j in range(width):
        row.append(-1)
    cumul_map.append(row)

# display_array(cumul_map)



# we reintroduce the good ol' point-ID scheme to make life easier for ourselves. 
# pID = y * width + height

def getID(x, y, width):
    return y * width + x

def getcoords(ID, width):
    return [ID % width, ID // width]

def get_bordering_points(ID):
    [x, y] = getcoords(ID, width)
    neighbors = []

    if not x == 0:
        neighbors.append(getID(x-1, y, width))
    if not x == width - 1:
        neighbors.append(getID(x+1, y, width))
    if not y == 0:
        neighbors.append(getID(x, y-1, width))
    if not y == height - 1:
        neighbors.append(getID(x, y+1, width))

    return neighbors

points_known = [0]
risk_array = []
for l in risk_map:
    risk_array += l
cost_array = [-1 for i in range(height * width)]
cost_array[0] = 0

bordering_pts = set(get_bordering_points(0))

for b in bordering_pts:
    cost_array[b] = risk_array[b]

while (len(points_known) < height * width):
    min_cost = 99999999999
    current_closest = -1
    for b in bordering_pts:
        if cost_array[b] < min_cost:
            min_cost = cost_array[b]
            current_closest = b
    
    cost_array[current_closest] = min_cost
    points_known.append(current_closest)
    bordering_pts.remove(current_closest)

    new_borders = get_bordering_points(current_closest)

    for n in new_borders:
        if cost_array[n] == -1:
            bordering_pts.add(n)
            cost_array[n] = min_cost + risk_array[n]
        else:
            new_cost = min_cost + risk_array[n]
            cost_array[n] = min(cost_array[n], new_cost)

    print(len(points_known))

print("result:", cost_array[-1])