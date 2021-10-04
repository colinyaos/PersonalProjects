# marooncap.py
# The statement of the problem can be found here: 
# https://mc.uchicago.edu/MC-Challenge_2021.pdf

# Apologies for lack of documentation, was written in a hurry for one-off use. 

import numpy as np

a = [0.53, 0.21]
b = [0.04, 0.27]
c = [0.04, 0.95]
d = [0.59, 0.21]
e = [0.22, 0.34]
f = [0.43, 0.41]
g = [0.32, 0.28]
h = [0.13, 0.66]
i = [0.06, 0.26]
j = [0.42, 0.10]
k = [0.20, 0.33]
l = [0.07, 0.44]

# elemlist = [a, b, c, d, e, f, g, h, i, j, k, l]
# elemlist = [a, b, d, e, f, g, h, i, k, l]
elemlist = [a, b, c, d, e, f, g, h, i, k, l]

firstValue = j
firstValue.append(round(1-sum(firstValue), 3))

newsmallList = []

newelemlist = []

for elem in elemlist:
    elem.append(round(1-sum(elem), 3))
    newsmallList.append(np.array(elem))
    newelemlist.append(np.array([[1, 0, 0], [0, 1, 0], elem]))

def matmult(a,b):
    zip_b = zip(*b)
    # uncomment next line if python 3 : 
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
             for col_b in zip_b] for row_a in a]

def generate_list(num, in_list):
	list_permutations = []

	for i in range(len(in_list) + 1):
		list_copy = in_list.copy()
		list_copy.insert(i, num)
		list_permutations.append(list_copy)

	return list_permutations

def gen_all_lists(num_limit):
	list_of_lists = [[1]]

	for i in range(2, num_limit + 1):
		temp_list_of_lists = []

		for small_list in list_of_lists:
			for sub_list in generate_list(i, small_list):
				temp_list_of_lists.append(sub_list)
		list_of_lists = []
		for l in temp_list_of_lists:
			list_of_lists.append(l)

	return list_of_lists

# superList = gen_all_lists(11)

# print(matmult(newsmallList[3], newelemlist[4]))


# print("firstValue\n\n", firstValue)

# print("this is newelemlist")
# print(newelemlist[0])
# print("\n\n")

# probs = []

# for sublist in superList:
#     # print(sublist)
#     replist = []
#     for elem in sublist:
#         replist.append(elem - 1)
    
#     totalMat = firstValue
#     for r in replist:
#         # print(r)
#         currentMatrix = newelemlist[r]
#         # print(totalMat, currentMatrix)
#         # print("curr_mat", currentMatrix)
#         # print("total_mat", totalMat)
#         # print("\n")
#         totalMat = np.matmul(totalMat, currentMatrix)
#     #     print("t=", totalMat)
#     # print(totalMat)
#     probs.append(totalMat[0])


# print(max(probs))
# slist = superList[probs.index(max(probs))]
# print(slist)

slist = [4, 1, 7, 6, 5, 10, 9, 8, 11, 2, 3]
slist = [x-1 for x in slist]

print(slist)

charlist = ["a", "b" , "c", "d", "e", "f", "g", "h", "i", "k", "l"]
print([charlist[x] for x in slist])
# print(superList[2])

bettercharlist = ["a", "b" , "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]

def testList(inList):
    """ Take in string of chars. Split into list of chars. 
    Then, test list chars based on values, and return final value. 
    Use recursion. 
    return [W L N] as list of floats. """

    if inList == "":
        return 0
    else:
        firstChar = inList[0]



# test1 = np.array([3, 5, 6])
# test2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(np.matmul(test1, test2))

# matmult(test1, test2)



# print(matmult(newelemlist[2], newelemlist[3]))
