# day12.py

with open('day12real.txt') as ipf:
    lines = ipf.readlines()

points = {}

for l in lines:
    # print(points)
    [str1, str2] = l[:-1].split(sep = "-")
    # print(str1, str2)

    if not str1 in points.keys():
        points[str1] = [str2]
    elif str1 in points.keys():
        list1 = points[str1]
        list1.insert(0, str2)
        points[str1] = list1

    if not str2 in points.keys():
        points[str2] = [str1]
    elif str2 in points.keys():
        list2 = points[str2]
        list2.insert(0, str1)
        points[str2] = list2

# print(points)

def isUppercase(str):
    for c in str:
        if c.islower():
            return False

    return True

# def step(path):
#     # for some path:
#     # we try to add another step, 
#     # then return the list of possible results. 

#     last = path[-1]
#     nexts = points[last]

#     out_list = []

#     for n in nexts:
#         p = path.copy()

#         if isUppercase(n):
#             p.append(n)
#             out_list.append(p)
#         else:
#             if n == "start":
#                 continue
#             if p.count(n) > 1:
#                 pass
#             else:
#                 p.append(n)
#                 out_list.append(p)


#     return out_list

# # print(step(["start"]))

# prospective = [["start"]]
# paths = []

# while not prospective == []:
#     curr_path = prospective.pop()
#     new_paths = step(curr_path)
#     for p in new_paths:
#         if p[-1] == "end":
#             paths.append(p)
#         else:
#             prospective.append(p)

# for i in range(20):
#     print(paths[i])
# print(len(paths))

def step2(path, hasdup):
    nodupList = []
    dupList = []
    
    last = path[-1]
    nexts = points[last]
    
    for n in nexts:
        p = path.copy()
        if n == "start":
            continue
        if isUppercase(n) or p.count(n) == 0:
            p.append(n)
            if hasdup:
                dupList.append(p)
            else:    
                nodupList.append(p)
        elif p.count(n) == 1 and hasdup == False:
            p.append(n)
            dupList.append(p)
    
    return [nodupList, dupList]


prospective = [["start"]]
prospw2 = []
paths = []

while not prospective == [] or not prospw2 == []:
    # print(prospective)
    if not prospw2 == []:
        # print("prospw2", prospw2)
        curr_path = prospw2.pop()
        [nodups, dups] = step2(curr_path, True)
        for p in nodups:
            if p[-1] == "end":
                paths.append(p)
            else:
                prospective.append(p)
        for p in dups:
            if p[-1] == "end":
                paths.append(p)
            else:
                prospw2.append(p)
    
    if not prospective == []:
        curr_path = prospective.pop()
        [nodups, dups] = step2(curr_path, False)
        # print(nodups)
        for p in nodups:
            # print("nodup", p)
            if p[-1] == "end":
                paths.append(p)
            else:
                prospective.append(p)
        for p in dups:
            if p[-1] == "end":
                paths.append(p)
            else:
                prospw2.append(p)

# for i in range(33):
#     print(paths[i])
print(len(paths))


# print(step2(['start', 'b', 'd', 'b'], False))