from aoc import read_input, alphabet


def to_area(values):
    r1, r2 = values.split("-")
    return set(range(int(r1), int(r2)+1))


def part1():
    total = 0
    for area1, area2 in input_as_ranges:
        if area1.issubset(area2) or area1.issuperset(area2):
            total = total + 1

    return total


def part2():
    total = 0
    for area1, area2 in input_as_ranges:
        if len(area1.intersection(area2)) > 0:
            total = total + 1

    return total


data = read_input("day04", str)
input_as_ranges = []
for line in data:
    s1, s2 = line.split(",")
    a1 = to_area(s1)
    a2 = to_area(s2)
    input_as_ranges.append((a1, a2))

print(part1())
print(part2())
assert (part1() == 582)
assert (part2() == 893)
