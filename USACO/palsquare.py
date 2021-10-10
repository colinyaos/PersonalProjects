"""
ID: colinya1
LANG: PYTHON3
TASK: palsquare
"""

fin = open("palsquare.in", "r")
fout = open("palsquare.out", "w")

n = int(fin.readline().strip())

def isPalin(number):
    """Given number in (string), return True if it is a palindrome. 
    Otherwise, return False. """
    subject = number

    # print("testing ispalin with", subject)
    # print(type(subject))
    sLen = len(subject)

    centrePoint = int((sLen - (sLen % 2) ) / 2)
    # print(centrePoint)
    firstHalf = subject[:centrePoint]
    secondHalf = subject[:-centrePoint -1:-1]

    # print(firstHalf, secondHalf)

    if firstHalf == secondHalf:
        return True
    else:
        return False

def reBase(number, base):
    """Given a number (b10 int), and a base (int), compute the representation
    of that number in the given base. 
    Returns a string. """

    exponent = base
    power = 1
    optionals = "ABCDEFGHIJ"

    if exponent > number:
        if number >= 10:
            return optionals[number - 10]
        else:
            return str(number)
    else:
        while exponent <= number:
            power += 1
            exponent = exponent * base
    power -= 1 #this power is now the largest exponent less than our given number

    exponent = base ** power

    listExps = ""
    counter = 0 #internal counter for multiple of powers

    while number >= 0:
        if number >= exponent:
            counter += 1
            number -= exponent
        else:
            if counter >= 10:
                listExps += optionals[counter - 10]
                # print("appending", optionals[counter - 10])
            else:
                # print("appending", counter)
                listExps += str(counter)
            
            counter = 0
            power -= 1
            exponent = base ** power
        if power < 0:
            break
        # print("number is", number, "exponent is", exponent, "counter is", counter)



    # while number >= 0:
    #     if number >= exponent:
    #         counter += 1
    #         number -= exponent
    #     else:
    #         if counter >= 10:
    #             print("bigger than 10 branch taken")
    #             listExps += optionals[counter - 10]
    #         else:
    #             listExps += str(counter)
    #         power -= 1

    #         if power == 0:
    #             break
    #         exponent = base ** power
    #         counter = 0
    #     print("number is", number, "exponent is", exponent, "counter is", counter)

    # listExps += str(number)
    # print("rebasetype", type(listExps))
    return listExps

# print(reBase(4530, 11))


for i in range(1, 301):
    k = i ** 2
    # print(reBase(k, n))
    # print(type(reBase(k, n)))
    if isPalin(reBase(k, n)):
        message = reBase(i, n) + " " + reBase(k, n) + "\n"
        fout.write(message)
