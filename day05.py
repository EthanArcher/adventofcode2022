import copy
from aoc import read_input_no_strip


def part1():
    for line in instructions:
        ins = line.split(" ")
        amount, start, end = int(ins[1]), int(ins[3])-1, int(ins[5])-1
        for a in range(amount):
            c = ship[start].pop()
            ship[end].append(c)

    result = ""
    for stack in ship:
        result = result + stack[len(stack)-1]
    print(result)
    return result


def part2():
    for line in instructions:
        ins = line.split(" ")
        amount, start, end = int(ins[1]), int(ins[3])-1, int(ins[5])-1
        crates = []
        for a in range(amount):
            c = ship[start].pop()
            crates.insert(0, c)

        ship[end] = ship[end] + crates

    result = ""
    for stack in ship:
        result = result + stack[len(stack) - 1]
    print(result)
    return result


data = read_input_no_strip("day05", str)

crates_input = []
instructions = []
gap = False
for line in data:
    if line == "":
        gap = True
    elif gap:
        instructions.append(line)
    else:
        crates_input.append(line)
last_line = crates_input.pop(len(crates_input) - 1)
positions = range(1, len(last_line), 4)
ship = [[] for y in range(len(positions))]

for line in crates_input:
    for pos in positions:
        crate = line[pos]
        if crate != "" and crate != " ":
            ship[(pos // 4)].insert(0, crate)

ship_reset = copy.deepcopy(ship)
assert (part1() == "RFFFWBPNS")
ship = copy.deepcopy(ship_reset)
assert (part2() == "CQQBBJFCS")