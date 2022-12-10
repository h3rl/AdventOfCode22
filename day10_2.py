from collections import defaultdict
import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test

data = parseAOC("./day10.txt")
datat = parseAOC("./day10t.txt")
CT = defaultdict(lambda:0)
U = 20
P1 = 0
NT = T = 1
CT[1] = 1

G = [['_' for _ in range(40)] for _ in range(6)]

for line in data:
    words = line.split()
    instr = words[0]
    if instr == "noop":
        NT += 1
    elif instr == "addx":
        v = int(words[1])
        NT += 2
        CT[NT] = v
    
    while NT - T > 0:
        X = 0
        for k,v in CT.items():
            if k <= T:
                X += v
        if U == T:

            ss = T * X
            print(T, X, ss)
            P1 += ss
            U += 40

        t1 = T-1
        r = t1//40
        c = t1%40
        
        s = ' '
        if abs(X-c)<=1:
            s = '#'
        G[r][c] = s

        T += 1

for r in G:
    print(''.join(r))


print(P1)
