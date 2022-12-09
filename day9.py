import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test
from collections import defaultdict, namedtuple, deque

data = parseAOC("./day9.txt")
datas = parseAOC_test("""\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""")

def sign(x): # signum function (returns 1, 0 or -1)
    if x == 0:
        return 0
    return x//abs(x)

def adjust(H,T):
    # get deltas
    dx = H[0]-T[0]
    dy = H[1]-T[1]

    if max(abs(dx), abs(dy)) > 1:
        # any delta > 1 => adjust
        return (T[0]+sign(dx), T[1]+sign(dy))
    return T

DX = {"R": 1, "L": -1, "U": 0, "D": 0}
DY = {"R": 0, "L": 0, "U": 1, "D": -1}
S = [(0,0) for _ in range(10)]# snake
P1 = set()
P2 = set()

for line in data:
    d = line[0]# direction
    for _ in range(int(line[1:])):
        # adjust head
        S[0] = (S[0][0] + DX[d], S[0][1] + DY[d])

        for i in range(1,10):
            # adjust rest of snake
            S[i] = adjust(S[i-1], S[i])
        # add tails to answer sets
        P1.add(S[1])
        P2.add(S[-1])

print("Solution a: " + str(len(P1)))
print("Solution b: " + str(len(P2)))