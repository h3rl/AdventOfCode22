import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test

data = parseAOC("./day15.txt")
test_data = parseAOC("./day15t.txt")

def mlen(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def part1(data, Y=10, debug=False):

    B = dict()
    M = set()
    # parse
    for line in data:
        line = line.split(":")
        [x,y] = line[0][len("Sensor at x="):].split(", y=")
        x,y = int(x), int(y)
        sensor = (x,y)
        [x,y] = line[1][len(" closest beacon is at x="):].split(", y=")
        x,y = int(x), int(y)
        beacon = (x,y)
        if beacon not in B:
            B[beacon] = []

        #print(sensor, beacon)

        B[beacon].append(sensor)
        M.add(beacon)
        M.add(sensor)

    print("parsed")

    # find all points that are not occupied
    # at y=10

    covering = set()
    min_x = 1e6
    max_x = 0
    min_y = 1e6
    max_y = 0
    for b, sensors in B.items():
        #print(b, sensors)
        for s in sensors:
            l = mlen(b,s)
            x,y = s
            if y + l > Y > y - l:
                #print("coverage", s, l)
                covering.add((s,l))
            
            min_x = min(min_x, b[0]-l)
            max_x = max(max_x, b[0]+l)
            min_y = min(min_y, b[1]-l)
            max_y = max(max_y, b[1]+l)


    R = max_x-min_x+1
    C = max_y-min_y+1
    # print(R,C)
    # print((min_x, min_y),(max_x, max_y))

    print("covering mapped")
    P1 = 0
    if debug:
        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                ok = False
                p = (x,y)
                for (s,l) in covering:
                    if mlen(p,s) <= l:
                        print("#", end="")
                        ok = True
                        break
                if not ok:
                    print(".", end="")
            print("")

    for x in range(int(min_x-1), int(max_x+1)):
        p = (x,Y)
        for (s,l) in covering:
            if mlen(p,s) <= l:
                P1 += 1
                break
    print("sub beacon")

    # beacon pos dont count so we subtract them
    for b in B:
        if b[1] == Y:
            print(b)
            P1 -=1

    print(P1)

def part2(data, lim=(0,20)):

    B = set()
    S = set()
    # parse
    for line in data:
        line = line.split(":")
        [x,y] = line[0][len("Sensor at x="):].split(", y=")
        sx,sy = int(x), int(y)
        [x,y] = line[1][len(" closest beacon is at x="):].split(", y=")
        bx,by = int(x), int(y)
        B.add((bx,by))
        l = mlen((bx,by),(sx,sy))
        S.add((sx,sy,l))

    print("parsed")
    
    for (sx,sy,l) in S:
        for dx in range(l+2):
            dy = l-dx+1
            for dir_x,dir_y in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                x = sx + dx*dir_x
                y = sy + dy*dir_y

                assert mlen((x,y),(sx,sy))==l+1

                if not(lim[0]<=x<=lim[1] and lim[0]<=y<=lim[1]):
                    continue
                

                valid = True
                for (xx,yy,ll) in S:
                    if ll >= mlen((x,y),(xx,yy)):
                        valid = False
                        break

                if not valid:
                    continue

                P2 = x*4000000+y
                print(x,y)
                print(P2)
                return


# part1(data,Y=2000000, debug = False)
part2(test_data,lim=(0,20))
part2(data, lim=(0,4000000))