import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test

def allUnique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)

def part_a(data):
    for i in range(4, len(data)):
        d = data[i-4:i]
        if allUnique(d):
            return i

def part_b(data):
    for i in range(14, len(data)):
        d = data[i-14:i]
        if allUnique(d):
            return i

def main():
    test_data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    data = parseAOC("./day6.txt")

    print(part_a(test_data))
    print(part_a(data))

    print(part_b(data))

if __name__ == "__main__":
    main()