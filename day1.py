import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test

def part_a(data):
    elfs = []
    s = 0
    for line in data:
        if line == "":
            elfs.append(s)
            s = 0
        else:
            s += int(line)
    return max(elfs)

def part_b(data):
    elfs = []
    s = 0
    for line in data:
        if line == "":
            elfs.append(s)
            s = 0
        else:
            s += int(line)
    
    elfs.sort(reverse=True)
    return sum(elfs[0:3])



def main():
    test_data = ("""\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""").split("\n")
    data = parseAOC("./day1.txt")

    assert part_a(test_data) == 24000
    print(part_a(data))

    assert part_b(test_data) == 45000
    print(part_b(data))

if __name__ == "__main__":
    main()