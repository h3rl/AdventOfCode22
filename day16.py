import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test
from collections import deque,defaultdict

data = parseAOC("./day16.txt")
test_data = parseAOC("./day16t.txt")


E = defaultdict(lambda:[])#valve -> connections
R = {}#rates

for line in test_data:
    words = line.split()
    valve = words[1]
    rate = int(words[4][5:-1])
    connections = [word.replace(",","") for word in words[9:]]
    #print(valve, rate, connections)
    for t in connections:
        E[valve].append(t)
    R[valve] = rate
    
DP = {}

def dfs(pos,v,t):
    if t == 0:
        return 0
    k = (pos,tuple(sorted(v)),t)
    if k in DP:
        return DP[k]
    ans = 0
    if t > 0 and pos not in v and R[pos] > 0:
        nans = set(v)
        nans.add(pos)
        ans = max(ans, sum(R[o] for o in v)+dfs(pos,nans,t-1))
    if t > 0:
        for n in E[pos]:
            ans = max(ans, sum(R[o] for o in v)+dfs(n,v,t-1))
    DP[k] = ans
    if len(DP) % 1000 == 0:
        print(len(DP))
    return ans

print(dfs("AA",set(),30))