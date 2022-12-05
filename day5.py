import sys
import pathlib
sys.path.append(pathlib.Path().resolve().__str__())
from util import parseAOC, parseAOC_test, strToIntList

def part_a(crates, instructions):
    grid = dict()
    for i, row in enumerate(crates):
        if not i+1 in grid:
            grid[i+1] = row
    for inst in instructions:
        inst = inst.split(" ")
        moves =int(inst[1])
        from_crate = int(inst[3])
        to_crate = int(inst[5])
        for i in range(moves):
            grid[to_crate].append(grid[from_crate].pop())

    answer = ""
    for k, v in grid.items():
        answer += v[-1]
    
    return answer

def part_b(crates, instructions):
    grid = dict()
    for i, row in enumerate(crates):
        if not i+1 in grid:
            grid[i+1] = row
    for inst in instructions:
        inst = inst.split(" ")
        moves =int(inst[1])
        from_crate = int(inst[3])
        to_crate = int(inst[5])

        tomove = []
        for i in range(moves):
            tomove.append(grid[from_crate].pop())
        tomove.reverse()
        for i in tomove:
            grid[to_crate].append(i)

    answer = ""
    for k, v in grid.items():
        if len(v) > 0:
            answer += v[-1]
    return answer

def parseCrate(data):
    
    grid = dict()
    for l in data:
        pass

def main():
    """
        [D]    
    [N] [C]    
    [Z] [M] [P]
    1   2   3 
    """
    test_data = [["Z","N"],["M","C","D"],["P"]]
    test_data_inst = parseAOC_test("""\
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""")

    data = parseAOC("./day5.txt")
    data_inst = data[data.index("")+1:]
    """
    [Q] [J]                         [H]
    [G] [S] [Q]     [Z]             [P]
    [P] [F] [M]     [F]     [F]     [S]
    [R] [R] [P] [F] [V]     [D]     [L]
    [L] [W] [W] [D] [W] [S] [V]     [G]
    [C] [H] [H] [T] [D] [L] [M] [B] [B]
    [T] [Q] [B] [S] [L] [C] [B] [J] [N]
    [F] [N] [F] [V] [Q] [Z] [Z] [T] [Q]
    1   2   3   4   5   6   7   8   9 
    """
    data = [["F","T","C","L","R","P","G","Q"],["N","Q","H","W","R","F","S","J"],["F","B","H","W","P","M","Q"],["V","S","T","D","F"],["Q","L","D","W","V","F","Z"],
    ["Z","C","L","S"],["Z","B","M","V","D","F"],["T","J","B"],["Q","N","B","G","L","S","P","H"]]
    
    # print(part_a(test_data, test_data_inst))
    # # assert part_a(test_data, test_data_inst) == "CMZ"
    # print(part_a(data, data_inst))

    print(part_b(test_data,test_data_inst))
    # assert part_b(test_data) == ""
    print(part_b(data,data_inst))

if __name__ == "__main__":
    main()