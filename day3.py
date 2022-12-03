import random
import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test, removeEmpty, ALPHABETH_FULL

def part_a(data):
    data = removeEmpty(data)
    score = 0
    for compartments in data:
        comp1 = compartments[:len(compartments)//2]
        comp2 = compartments[len(compartments)//2:]
        for letter in ALPHABETH_FULL:
            if letter in comp1 and letter in comp2:
                score_for_letter = ALPHABETH_FULL.index(letter) + 1
                score += score_for_letter
                break
    return score

def part_b(data):
    data = removeEmpty(data)
    score = 0
    while len(data) > 0:
        [r1, r2, r3] = data[0:3]
        data = data[3:]
        for letter in ALPHABETH_FULL:
            if letter in r1 and letter in r2 and letter in r3:
                score_for_letter = ALPHABETH_FULL.index(letter) + 1
                score += score_for_letter
                break
    return score

def main():
    test_data = parseAOC_test("""\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""")
    data = parseAOC("./day3.txt")

    assert part_a(test_data) == 157
    print(part_a(data))

    assert part_b(test_data) == 70
    print(part_b(data))

if __name__ == "__main__":
    main()