# adventDayTwo.py

# reads repeated up/down/forward instructions, then
# figures out position and depth as a result. 

with open('input2.txt') as ipf:
    lines = ipf.readlines()

# PART ONE

hor = 0
dep = 0

for l in lines:
    words = l.split()
    quantity = int(words[1])
    if  words[0] == "forward":
        hor += quantity
    elif words[0] == "down":
        dep += quantity
    elif words[0] == "up":
        dep -= quantity
    
print(hor, dep)


# PART 2

hor = 0
dep = 0
aim = 0

for l in lines:
    words = l.split()
    quantity = int(words[1])
    if  words[0] == "forward":
        hor += quantity
        dep += aim * quantity
    elif words[0] == "down":
        aim += quantity
    elif words[0] == "up":
        aim -= quantity

print(hor, dep, hor*dep)