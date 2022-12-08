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

# 0 is invisible, 1 is visible
visible_map = []
score_map = []
height_map = data.copy()
#height_map = test_data.copy()
HEIGHT = len(height_map)
WIDTH = len(height_map[0])
SIZE = len(height_map)
print(HEIGHT, WIDTH)

for line in height_map:
    visible_map.append([0 for _ in range(SIZE)])
    score_map.append([0 for _ in range(SIZE)])

# outer perimiter is visible
for k in range(SIZE):
    visible_map[k][0] = 1
    visible_map[k][-1] = 1
for k in range(SIZE):
    visible_map[0][k] = 1
    visible_map[-1][k] = 1

# left right
for y in range(SIZE):
    last = height_map[y][0]
    for x in range(SIZE):
        current = height_map[y][x]

        # if visible_map[y][x] == 1:# not sure
        #     continue

        if current > last:
            last = current
            visible_map[y][x] = 1

# right left
for y in range(SIZE):
    last = height_map[y][-1]
    for x in range(SIZE-1, -1, -1):
        current = height_map[y][x]

        # if visible_map[y][x] == 1:# not sure
        #     continue

        if current > last:
            last = current
            visible_map[y][x] = 1

# top down
for x in range(SIZE):
    last = height_map[0][x]
    for y in range(SIZE):
        current = height_map[y][x]

        if current > last:
            last = current
            visible_map[y][x] = 1

# bottom up
for x in range(SIZE):
    last = height_map[-1][x]
    for y in range(SIZE-1, -1, -1):
        current = height_map[y][x]

        # if visible_map[y][x] == 1:# not sure
        #     continue

        if current > last:
            last = current
            visible_map[y][x] = 1

a = 0
for l in visible_map:
    a += sum(l)

for x in range(SIZE):
    for y in range(SIZE):
        tree = height_map[y][x]
        print("looking at tree at", x, y, "with height", tree)
        treescore = 1
        # look up
        score = 0
        for k in range(y-1, -1, -1):
            score += 1
            if height_map[k][x] >= tree:
                break
        treescore *= score
        # look down
        score = 0
        for k in range(y+1, SIZE):
            score += 1
            if height_map[k][x] >= tree:
                break
        treescore *= score
        
        # look left
        score = 0
        for k in range(x-1, -1, -1):
            score += 1
            if height_map[y][k] >= tree:
                break
        treescore *= score
        
        # look right
        score = 0
        for k in range(x+1, SIZE):
            score += 1
            if height_map[y][k] >= tree:
                break
        treescore *= score

        score_map[y][x] = treescore

b = 0
for row in score_map:
    b = max(row+[b])

print("Solution a: " + str(a))
print("Solution b: " + str(b))