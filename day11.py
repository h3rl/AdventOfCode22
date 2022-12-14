from collections import defaultdict
import math
import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test

#data = parseAOC("./day11.txt")

def Oper(m,oval):
    if m == 0:
        return oval*19
    elif m == 1:
        return oval+1
    elif m == 2:
        return oval +6
    elif m == 3:
        return oval+5
    elif m == 4:
        return oval**2
    elif m == 5:
        return oval+7
    elif m == 6:
        return oval*7
    elif m == 7:
        return oval+2

class Monkey:
    def __init__(self) -> None:
        self.id = -1
        self.inspects = 0
        self.items = []
        self.operation = ""
        self.test = 0
        self.trueloc = -1
        self.falseloc = -1

        self.worrylevel=0
        self._oper = None

    #change on inspect
    def setOper(self):
        self._oper = lambda old: eval(self.operation)

    def Operation(self,oval):
        # o = lambda old: eval(self.operation)
        return self._oper(oval)
    
    # decide next throw
    def Test(self,wl):
        if wl % self.test == 0:
            return self.trueloc
        return self.falseloc

M = []

with open("./day11.txt","r") as file:
    line = "lul"
    while line != "":
        line = file.readline()
        if line.startswith("Monkey"):
            monkey = Monkey()
            monkey.id = int( line[line.index("Monkey ")+len("Monkey ")])

            line = file.readline()
            line = line[line.index(":")+1:]
            monkey.items = [int(a) for a in line.replace(" ","").split(",")]
            
            line = file.readline()
            line = line[line.index("=")+1:]
            monkey.operation = line
            monkey.setOper()
            line = file.readline()
            monkey.test = int(line[line.index("by")+2:])
            
            line = file.readline()
            monkey.trueloc = int(line[line.index("monkey")+len("monkey")+1:])
            line = file.readline()
            monkey.falseloc = int(line[line.index("monkey")+len("monkey")+1:])

            M.append(monkey)
ROUNDS = 10000

P1 = 0

common = 1
for m in M:
    common *= m.test

for r in range(ROUNDS):
    for monkey in M:
        while len(monkey.items) > 0:
            wl = monkey.items.pop(0)
            wl = wl % common
            wl = Oper(monkey.id,wl)
            #wl = monkey.Operation(wl)
            #wl = math.floor(wl/3)
            nloc = monkey.Test(wl)
            M[nloc].items.append(wl)
            monkey.inspects += 1
    
    print(f"Round {r+1}")
    for monkey in M:
        # iar = ""
        # if len(monkey.items) > 0:
        #     iar = ','.join(str(x) for x in monkey.items)
        print(f"Monkey {monkey.id}: {monkey.inspects}")
    print("")


I = []
for m in M:
    I.append(m.inspects)

P1 += max(I)
I.remove(P1)
P1 *= max(I)
print(P1)