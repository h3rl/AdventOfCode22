import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test
from collections import deque,defaultdict

data = parseAOC("./day18.txt")

X,Y,Z = [],[],[]
PT =  set()

sides = 0

for line in data:
    x,y,z = line.split(",")
    x,y,z = int(x),int(y),int(z)
    PT.add((x,y,z))

    # add 6 sides per point
    sides += 6

    # if adjecent points are in the list, remove 2 sides

adj = 0

for x,y,z in PT:
    for dx,dy,dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        if (x+dx,y+dy,z+dz) in PT:
            adj += 1

print(sides-adj)