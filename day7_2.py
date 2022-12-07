import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test
from collections import defaultdict

def solve(data):
    directory = defaultdict(lambda:0)
    cursor = []
    for line in data:
        # parse line
        words = line.split(" ")
        if words[1] == "ls" or words[0] == "dir":
            continue
        elif words[1] == "cd":
            if words[2] == "..":
                cursor.pop()
            else:
                cursor.append(words[2])
        else:
            #info about cwd
            cursor_copy = cursor.copy()
            while len(cursor_copy) > 0:
                directory["/".join(cursor_copy)] += int(words[0])
                cursor_copy.pop()
    
    a = 0

    freed = 70000000 - directory["/"]
    target = 30000000 - freed

    b = 1e9 # smallest

    for key, val in directory.items():
        if val < b and val > target:
            b = val
        if val < 100000:
            a += val

    print("Solution a: " + str(a))
    print("Solution b: " + str(b))

if __name__ == "__main__":
    data = parseAOC("./day7.txt")
    solve(data)