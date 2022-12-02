import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test

def part_a(data):
    SHAPES = {"A":"rock","B":"paper","C":"scissors",
            "X":"rock","Y":"paper","Z":"scissors"}

    totscore = 0
    for match in data:
        if not match:
            continue
        [elf_play, our_play] = match.split(" ")
        elf_play = SHAPES[elf_play]
        our_play = SHAPES[our_play]

        score = 0

        # draw
        if elf_play == our_play:
            score += 3
        # win
        elif elf_play == "rock" and our_play == "paper" \
        or elf_play == "paper" and our_play == "scissors" \
        or elf_play == "scissors" and our_play == "rock":
            score += 6

        # lost
        else:
            score += 0

        # shapescore
        if our_play == "rock":
            score += 1
        elif our_play == "paper":
            score += 2
        elif our_play == "scissors":
            score += 3
        totscore += score
    return totscore


def part_b(data):
    SHAPES = {"A":"rock","B":"paper","C":"scissors"}
    RESULT = {"X":"loose","Y":"draw","Z":"win"}
    SCORES = {"rock":1, "paper":2, "scissors":3}
    totscore = 0
    for match in data:
        if not match:
            continue
        [elf_play, outcome] = match.split(" ")
        elf_play = SHAPES[elf_play]
        outcome = RESULT[outcome]
        score = 0

        # draw
        if outcome == "draw":
            score += 3
            score += SCORES[elf_play] # we play same as elf
        # win
        elif outcome == "win":
            score += 6

            if elf_play == "rock": # we play paper
                score += SCORES["paper"]
            elif elf_play == "paper": # we play scissors
                score += SCORES["scissors"]
            elif elf_play == "scissors": # we play rock
                score += SCORES["rock"]

        # loose
        else:
            score += 0
            if elf_play == "rock": # we play scissors
                score += SCORES["scissors"]
            elif elf_play == "paper": # we play rock
                score += SCORES["rock"]
            elif elf_play == "scissors": # we play paper
                score += SCORES["paper"]
        totscore += score
    return totscore

def main():
    test_data = parseAOC_test("""\
A Y
B X
C Z
""")
    data = parseAOC("./day2.txt")

    assert part_a(test_data) == 15
    print(part_a(data))

    assert part_b(test_data) == 12
    print(part_b(data))

if __name__ == "__main__":
    main()