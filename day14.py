import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test

data = parseAOC("./day14.txt")
test_data = parseAOC("./day14t.txt")

def sign(x):
    if x<0:
        return -1
    elif x>0:
        return 1
    else:
        return 0

R = set()
for line in data:
    points = line.split("->")
    last = None
    for point in points:
        x,y = point.split(",")
        x,y = int(x), int(y)
        if last != None:
            dx = x-last[0]
            dy = y-last[1]
            l = max(abs(dx), abs(dy))
            for i in range(l+1):
                nx = last[0]+i*sign(dx)
                ny = last[1]+i*sign(dy)
                R.add((nx,ny))
        last = (x,y)
src = (500,0)
floor = 0
for r in R:
    floor = max(floor, r[1])

for k in range(-10000,10000):
    R.add((k,floor))

for n in range(100000):
    r = (500,0)
    while True:
        # if r[1] > floor: # svar 1
        #     print(n)
        if (r[0], r[1]+1) not in R:# down
            r = (r[0], r[1]+1)
        elif (r[0]-1,r[1]+1) not in R:# left and down
            r = (r[0]-1, r[1]+1)
        elif (r[0]+1,r[1]+1) not in R:# right and down
            r = (r[0]+1, r[1]+1)
        else:
            break

    if r == (500,0):
        print("ans2",n+1)
        break
        

        
    R.add(r)# settled

        