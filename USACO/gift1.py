"""
ID: colinya1
LANG: PYTHON3
TASK: gift1
"""

fin = open("gift1.in", "r")
fout = open("gift1.out", "a")

Lines = fin.readlines()

NP = int(Lines.pop(0)) #num of people
listnames = []

for i in range(NP):
    listnames.append(Lines.pop(0).strip()) #each name

print(listnames)

monies = {} # this will log transations, linking name to total cash

for name in listnames:
    monies[name] = 0

morenames = True

while morenames == True:
    #print("starting loop")
    currentname = Lines.pop(0).strip()
    print("currentname", currentname)
    numbers = Lines.pop(0).strip()
    amt = int(numbers.split()[0])
    numpeople = int(numbers.split()[1])

    print(amt, numpeople)
    
    if numpeople != 0:
        remainder = amt % numpeople

        amt -= remainder
    
        recipients = []

        for i in range(numpeople):
            recipients.append(Lines.pop(0).strip())

        for r in recipients:
            monies[r] = monies[r] + (amt / numpeople)
        monies[currentname] = monies[currentname] - amt

    if len(Lines) == 0:
        #print("ending loop")
        morenames = False



for m in monies:
    # print(str(m))
    # print(str(monies[m]))
    exitstring = str(m) + " " + str(int(monies[m])) + "\n"
    # print(exitstring)
    fout.write(exitstring)