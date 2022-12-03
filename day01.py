from aoc import read_input


def part1():
    data = read_input("day01", str)
    data.append("")
    this_elf = 0
    top1 = 0
    top2 = 0
    top3 = 0

    for v in data:
        if v != "":
            this_elf += int(v)
        else:
            if this_elf > top1:
                top3 = top2
                top2 = top1
                top1 = this_elf
            elif this_elf > top2:
                top3 = top2
                top2 = this_elf
            elif this_elf > top3:
                top3 = this_elf
            this_elf = 0

    print(top1)
    print(top2)
    print(top3)
    print(top1 + top2 + top3)


part1()
