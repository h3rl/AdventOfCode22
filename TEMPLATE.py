import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test

def part_a(data):
    result = 0
    # your code here..
    return result

def part_b(data):
    result = 0
    # your code here..
    return result

def main():
    test_data = parseAOC_test("""\
TESTDATA
MOREDATA
""")
    data = parseAOC("./1.txt")

    assert part_a(test_data) == 0
    print(part_a(data))

    # assert part_b(test_data) == 0
    # print(part_b(data))

if __name__ == "__main__":
    main()