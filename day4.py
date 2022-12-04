import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test, strToIntList

def part_a(data):
    overlap = 0
    for line in data:
        if line == "":
            continue
        [p1, p2] = line.split(",")
        [p1_s, p1_e] = strToIntList(p1.split("-"))
        [p2_s, p2_e] = strToIntList(p2.split("-"))
        
        if (p1_s >= p2_s and p1_e <= p2_e) or \
            (p2_s >= p1_s and p2_e <= p1_e):
            overlap += 1
    return overlap




def part_b(data):
    overlap = 0
    for line in data:
        if line == "":
            continue
        [p1, p2] = line.split(",")
        [p1_s, p1_e] = strToIntList(p1.split("-"))
        [p2_s, p2_e] = strToIntList(p2.split("-"))

        for a in range(p1_s, p1_e + 1):
            if a >= p2_s and a <= p2_e:
                overlap += 1
                break
    return overlap

def main():
    test_data = parseAOC_test("""\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""")
    data = parseAOC("./day4.txt")
    
    assert part_a(test_data) == 2
    print(part_a(data))

    assert part_b(test_data) == 4
    print(part_b(data))

if __name__ == "__main__":
    main()