from aoc import read_input


instructions = read_input("day10", str)
register_x = 1
computing = False
cycle_number = 1
cycles_to_check = [20, 60, 100, 140, 180, 220]
signal_strengths = []
crt = []

while instructions:
    step = instructions[0]
    crt.append("#" if abs((cycle_number-1) % 40 - register_x) <= 1 else ".")
    if cycle_number in cycles_to_check:
        signal_strengths.append(cycle_number * register_x)
    if computing:
        computing = False
        # action the instruction at the end of the cycle
        register_x += int(step.split(" ")[1])
        instructions = instructions[1:]
    else:
        if step.startswith("addx"):
            computing = True
        else:
            instructions = instructions[1:]

    cycle_number += 1

# part 1
print(sum(signal_strengths))

# part 2
for i in range(0, len(crt), 40):
    print("".join(crt[i:i+40]))

