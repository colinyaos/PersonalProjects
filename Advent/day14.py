# day14.py



with open('day14real.txt') as ipf:
    lines = ipf.readlines()

base = lines[0][:-1]
rules = {}

for i in range(2, len(lines)):
    [pair, insert] = lines[i].split(" -> ")
    rules[pair] = insert[:-1]

print(base)
print(rules)
letters = set(rules.values())

def step(polymer):
    pairs = []
    for i in range(len(polymer) - 1):
        pairs.append(polymer[i:i+2])

    additionals = []
    for p in pairs:
        if p in rules.keys():
            additionals.append(rules[p])
        else:
            additionals.append("")
    additionals.append("")
    # print(additionals)


    result = ""
    for char in polymer:
        result += char
        result += additionals.pop(0)
    
    return result

# curr_base = base

# for i in range(40):
#     curr_base = step(curr_base)
#     print(i, len(curr_base))

# def countbases(str):
#     letters = set(str)
#     for l in letters:
#         print(l, str.count(l))

# countbases(curr_base)

pair_to_pair = {}

for pair in rules.keys():
    midchar = rules[pair]
    fst = pair[0]
    snd = pair[1]

    fst_pair = fst + midchar
    snd_pair = midchar + snd

    pair_to_pair[pair] = [fst_pair, snd_pair]

num_pair_dict = {}

for pair in rules.keys():
    num_pair_dict[pair] = 0

def pair_step(pair, new_num_pair, num):
    [fst, snd] = pair_to_pair[pair]
    new_num_pair[fst] += num
    new_num_pair[snd] += num

    return new_num_pair

input_pairs = []

for i in range(len(base) - 1):
    input_pairs.append(base[i:i+2])

for p in input_pairs:
    num_pair_dict[p] += 1

def update_num_dict():
    blank_pair_dict = {}
    for pair in rules.keys():
        blank_pair_dict[pair] = 0
    
    for key in num_pair_dict.keys():
        val = num_pair_dict[key]
        blank_pair_dict = pair_step(key, blank_pair_dict, val)

    return blank_pair_dict

def count_pair_dict(npdict):
    letter_dict = {}
    for l in letters:
        letter_dict[l] = 0
    
    for key in npdict.keys():
        val = npdict[key]
        letter_dict[key[0]] += val
        letter_dict[key[1]] += val
    
    letter_dict[base[0]] += 1
    letter_dict[base[-1]] += 1

    for l in letter_dict.keys():
        letter_dict[l] = letter_dict[l] / 2

    return letter_dict

for i in range(40):
    num_pair_dict = update_num_dict()

print(count_pair_dict(num_pair_dict))


maxval = max(count_pair_dict(num_pair_dict).values())
minval = min(count_pair_dict(num_pair_dict).values())

print(maxval, minval, maxval - minval)

