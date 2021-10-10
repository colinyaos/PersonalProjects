"""
ID: colinya1
LANG: PYTHON3
TASK: dualpal
"""

fin = open("dualpal.in", "r")
fout = open("dualpal.out", "w")

inputLine = fin.readline().strip().split()

n = int(inputLine[0])

s = int(inputLine[1])

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
    return listExps


def testForPalin(number):
    """Given some integer number, check to see if it is a palindrome in bases 2-10. 
    Returns True if at least 2 are palindromes. Else, returns False. """
    numSuccess = 0
    for i in range(2, 11):
        if isPalin(reBase(number, i)):
            numSuccess += 1
    if numSuccess >= 2:
        return True
    else:
        return False

while n > 0:
    s += 1
    if testForPalin(s):
        fout.write(str(s) + "\n")
        n -= 1

