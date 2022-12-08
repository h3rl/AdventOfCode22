import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test

def print_map(map):
    for line in map:
        print(line)

data = parseAOC("./day8.txt")
test_data = parseAOC_test("""\
30373
25512
65332
33549
35390
""")

G = [list(map(int,list(line))) for line in data]

DIR = [(-1,0),(0,1),(1,0),(0,-1)]
R = len(G)
C = len(G[0])

p1 = 0
for r in range(R):
    for c in range(C):
        for (dr,dc) in DIR:
            nr = r+dr
            nc = c+dc
            ok = True
            while True:
                if not (0 <= nr < R and 0 <= nc < C):
                    break
                if G[nr][nc] >= G[r][c]:
                    ok = False
                nr += dr
                nc += dc
            if ok:
                p1 += 1
                break

print(p1)

p2 = 0
for r in range(R):
    for c in range(C):
        score = 1
        for (dr,dc) in DIR:
            dist = 0
            nr = r
            nc = c
            while True:
                nr += dr
                nc += dc
                if not (0 <= nr < R and 0 <= nc < C):
                    break
                dist += 1
                if G[nr][nc] >= G[r][c]:
                    break
            score *= dist
        p2 = max(p2,score)
print(p2)
