# day13.py

with open('day13real.txt') as ipf:
    lines = ipf.readlines()

pairs = []
folds = []

for l in lines:
    if "," in l:
        [a, b] = l.split(",")
        pairs.append((int(a), int(b)))
    elif "=" in l:
        [c, d] = l.split("=")
        folds.append([c[-1], int(d[:-1])])

# print(pairs)
# print(folds)

def foldup(yline, pairs_in):
    new_pairs = []
    for p in pairs_in:
        [x, y] = p
        if y < yline:
            new_pairs.append(p)
        if y >= yline:
            new_pairs.append((x, 2*yline - y))
    return new_pairs

def foldleft(xline, pairs_in):
    new_pairs = []
    for p in pairs_in:
        [x, y] = p
        # print(xline)
        if x < xline:
            new_pairs.append(p)
        if x >= xline:
            # print(p, 2*xline - x)
            new_pairs.append((2*xline - x, y))
    return new_pairs

def fold(n, pairs_in):
    pairs_copy = pairs_in
    for i in range(n):
        curr_fold = folds[i]
        # print(curr_fold)
        if curr_fold[0] == "x":
            pairs_copy = list(set(foldleft(curr_fold[1], pairs_copy)))
        else:
            pairs_copy = list(set(foldup(curr_fold[1], pairs_copy)))
    
    return pairs_copy

pairs = fold(len(folds), pairs)

print(pairs)
print(len(pairs))

# new_pairs = foldleft(655, pairs)

# print(pairs)
# print(len(new_pairs))

max_x = 38
max_y = 5


for i in range(max_y + 1):
    for j in range(max_x + 1):
        if (j, i) in pairs:
            print("*", end="")
        else:
            print(" ", end= "")
    print()