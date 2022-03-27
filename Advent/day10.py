# day10.py

with open('day10real.txt') as ipf:
    lines = ipf.readlines()


def parseline(s):
    corresponding = {')':'(', ']':'[', '}':'{', '>':'<'}
    
    buffer = []
    for c in s:
        if c in corresponding.values():
            buffer.append(c)
        elif c in corresponding.keys():
            if buffer[-1] == corresponding[c]:
                buffer.pop()
            else:
                badval = buffer.pop()
                # print("Had " + badval + " but got " + c)
                return c
    return "n"

# pointvals = {')':3, ']':57, '}':1197, '>':25137, 'n':0}

# total = 0

# for l in lines:
#     total += pointvals[parseline(l)]

# print(total)

def validline(s):
    corresponding = {')':'(', ']':'[', '}':'{', '>':'<'}
    
    buffer = []
    for c in s:
        if c in corresponding.values():
            buffer.append(c)
        elif c in corresponding.keys():
            if buffer[-1] == corresponding[c]:
                buffer.pop()
            else:
                return False
    return True

def completeline(s):
    corresponding = {')':'(', ']':'[', '}':'{', '>':'<'}
    inv_corresponding = {v:k for k, v in corresponding.items()}

    buffer = []
    for c in s:
        if c in corresponding.values():
            buffer.append(c)
        elif c in corresponding.keys():
            if buffer[-1] == corresponding[c]:
                buffer.pop()
    
    leftover = []
    
    for c in buffer:
        leftover.insert(0, inv_corresponding[c])

    return "".join(leftover)

def scoreline(s):
    char_scores = {')':1, ']':2, '}':3, '>':4}

    total_score = 0

    for c in s:
        total_score = total_score * 5
        total_score += char_scores[c]
    
    return total_score


valid_lines = []

for l in lines:
    if validline(l):
        valid_lines.append(l)

score_lines = []

for v in valid_lines:
    score_lines.append(completeline(v))

scores = []

for s in score_lines:
    scores.append(scoreline(s))

scores.sort()

print(len(scores), scores[len(scores) // 2])