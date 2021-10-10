"""
ID: colinya1
LANG: PYTHON3
TASK: crypt1
"""

fin = open("crypt1.in", "r")
fout = open("crypt1.out", "w")

n = fin.readline().strip()

digits = [int(x) for x in fin.readline().split()]

# digits = [2, 3, 4, 6, 8]

print(digits)
print(len(digits))


# we'll call the numbers bigin, smallin, inter1, inter2, and output, in that order
# bigin can be a plain int, smallin is a list of 2 ints

def intsplitter(x):
    """ Takes in some int x, and returns a list of ints that make up the digits of x"""
    xstr = str(x)
    output = []
    
    for i in xstr:
        output.append(int(i))
    return output



bigins = []

for i in digits:
    for j in digits:
        for k in digits:
            bigins.append(100*i + 10*j + k)

# print(len(bigins))

smallins = []

for i in digits:
    for j in digits:
        smallins.append([i,j])

validNums = []

for b in bigins:
    for s in smallins:
        inter1 = s[1] * b

        # print(inter1)

        if len(str(inter1)) > 3:
            continue
        if not set(intsplitter(inter1)).issubset(digits):
            continue
        
        # print(s)

        inter2 = s[0] * b
        if len(str(inter2)) > 3:
            continue
        if not set(intsplitter(inter2)).issubset(digits):
            continue
        
        smallin = 10*s[0] + s[1]

        if not set(intsplitter(smallin * b)).issubset(digits):
            continue

        validNums.append([b, s])

# print(validNums)

fout.write(str(len(validNums)) + "\n")

# if __name__ == "__main__":
#     print(intsplitter(122344))
#     banana = intsplitter(23443235234)
#     print(set(banana).issubset(digits))


