from aoc import read_input


def part1(line):
    return find_start_of_sequence(line, 4)


def part2(line):
    return find_start_of_sequence(line, 14)


def find_start_of_sequence(line, length):
    letter_set = set()
    for i in range(length-1, len(line)):
        for j in range(length):
            letter_set.add(line[i - j])
        if len(letter_set) == length:
            return i + 1
        letter_set.clear()
    return 0


data = read_input("day06", str)
for line in data:
    p1 = part1(line)
    p2 = part2(line)
    print(p1)
    print(p2)
    assert (p1 == 1912)
    assert (p2 == 2122)