from aoc import read_input, alphabet


def part1():
    total = 0
    for line in data:
        c1, c2 = set(line[:len(line)//2]), set(line[len(line)//2:])
        duplicates = (c1.intersection(c2))
        for d in duplicates:
            total = total + alphabet.get(d)

    return total


def part2():
    total = 0
    for i in range(len(data)//3):
        elf1 = set(data[i*3])
        elf2 = set(data[i*3+1])
        elf3 = set(data[i*3+2])
        for d in elf1.intersection(elf2).intersection(elf3):
            total = total + alphabet.get(d)

    return total


data = read_input("day03", str)
print(part1())
print(part2())
assert (part1() == 7863)
assert (part2() == 2488)
