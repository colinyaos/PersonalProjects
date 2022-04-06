# adventDayFive.py

# Take in a list of line segments, and 
# identify points where two or more overlap. 

with open('input5.txt') as ipf:
    lines = ipf.readlines()

plist = [l.split(" -> ") for l in lines]

coordlist = [( p[0].split(",") , p[1].split(",") ) for p in plist]
# coordlist should now be a list of points. 
# every entry in coordlist should be a pair containing two lists, 
# each with two strings inside. 


ptlist = [ ( tuple(map(int,c[0])) , tuple(map(int,c[1]))   ) for c in coordlist]

# ptlist should be a list of line segments. 
# each "line segment" should be a pair of points. 
# each "point" should be a pair containing two ints. 

# example element: ((850, 828), (850, 98))

print(ptlist[5])

# ----- PART ONE


# coveredpts = []
# duppts = set([])

# def tryput(pair):
#     # tries to put some pair in coveredpts. 
#     # if it's already there, adds it to duppts. 
#     if pair in coveredpts:
#         duppts.add(pair)
#     else:
#         coveredpts.append(pair)

# for pt in ptlist:
#     ((x1, y1), (x2,y2)) = pt

#     if x1 == x2:
#         miny = min([y1, y2])
#         maxy = max([y1, y2])

#         for y in range(miny, maxy + 1):
#             p = (x1, y)
#             tryput(p)

#     if y1 == y2:
#         minx = min([x1, x2])
#         maxx = max([x1, x2]) 
        
#         for x in range(minx, maxx + 1):
#             p = (x, y1)
#             tryput(p)

# print(len(duppts))


# duppts = {[]}

# for i in range(len(ptlist)):
#     ((x1, y1), (x2, y2)) = i

#     if not x1 == x2 and not y1 == y2:
#         continue

#     seg1pts = {[]}
#     if x1 == x2:
#         miny = min([y1, y2])
#         maxy = max([y1, y2])

#         for y in range(miny, maxy + 1):
#             p = (x1, y)
#             seg1pts.add(p)

#     if y2 == y2:
#         minx = min([x1, x2])
#         maxx = max([x1, x2]) 
        
#         for x in range(minx, maxx + 1):
#             p = (x, y1)
#             seg1pts.add(p)

#     # seg1pts should now be a set loaded with all points in the seg. 

#     for j in range(i+1, len(ptlist)):
#         ((x3, y3), (x4, y4)) = j

#         if not x3 == x4 and not y3 == y4:
#             continue

#         seg2pts = {[]}
#         if x3 == x4:
#             miny = min([y3, y4])
#             maxy = max([y3, y4])

#             for y in range(miny, maxy + 1):
#                 p = (x3, y)
#                 seg2pts.add(p)

#         if y3 == y4:
#             minx = min([x3, x4])
#             maxx = max([x3, x4]) 
            
#             for x in range(minx, maxx + 1):
#                 p = (x, y3)
#                 seg2pts.add(p)
#         # seg2pts is now a set loaded with all points in seg2. 
#         print("b")



##     ------------  PART TWO

coveredpts = []
duppts = set([])


def tryput(pair):
    # tries to put some pair in coveredpts. 
    # if it's already there, adds it to duppts. 
    if pair in coveredpts:
        duppts.add(pair)
    else:
        coveredpts.append(pair)

for pt in ptlist:
    ((x1, y1), (x2,y2)) = pt

    if x1 == x2:
        miny = min([y1, y2])
        maxy = max([y1, y2])

        for y in range(miny, maxy + 1):
            p = (x1, y)
            tryput(p)

    if y1 == y2:
        minx = min([x1, x2])
        maxx = max([x1, x2]) 
        
        for x in range(minx, maxx + 1):
            p = (x, y1)
            tryput(p)
    
    if x1 + y1 == x2 + y2:
        minx = min([x1, x2])
        maxx = max([x1, x2]) 

        for x in range(minx, maxx+1):
            p = (x, (x1+y1) - x)
            tryput(p)

    if - x1 + y1 == - x2 + y2:
        minx = min([x1, x2])
        maxx = max([x1, x2]) 

        for x in range(minx, maxx+1):
            p = (x, (-x1+y1) + x)
            tryput(p)

print(len(duppts))