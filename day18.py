import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test
from collections import deque,defaultdict

data = parseAOC("./day18.txt")

PT =  set()
sides = 0

for line in data:
    x,y,z = line.split(",")
    x,y,z = int(x),int(y),int(z)
    PT.add((x,y,z))

    # add 6 sides per point
    sides += 6

for x,y,z in PT:
    for dx,dy,dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        if (x+dx,y+dy,z+dz) in PT:
            sides -= 1

print(sides)

maxx = max([x for x,y,z in PT])
maxy = max([y for x,y,z in PT])
maxz = max([z for x,y,z in PT])
MAX = max(maxx,maxy,maxz)+1

OUT = set()
def isOnEdge(x,y,z):
    if x < 0 or y < 0 or z < 0:
        return True
    
    if x >= MAX or y >= MAX or z >= MAX:
        return True

    if (x,y,z) in PT:
        return False

    if (x,y,z) in OUT:
        return True
    VISITED = set()
    Q = deque([(x,y,z)])
    while Q:
        x,y,z = Q.popleft()
        if (x,y,z) in PT:
            continue
        if (x,y,z) in VISITED:
            continue
        VISITED.add((x,y,z))
        if len(VISITED) > 6000:
            for pt in VISITED:
                OUT.add(pt)
            return True
        
        for dx,dy,dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            Q.append((x+dx,y+dy,z+dz))
    return False

sides = 0
for (x,y,z) in PT:
    for dx,dy,dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        if isOnEdge(x+dx,y+dy,z+dz):
            sides += 1

print(sides)
