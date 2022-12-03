from aoc import read_input


def part1():
    data = read_input("day01", str)
    this_elf = 0
    calorie_list = []

    for v in data:
        if v != "":
            this_elf += int(v)
        else:
            calorie_list.append(this_elf);
            this_elf = 0

    calorie_list.sort(reverse=True)
    print(calorie_list)

    print(calorie_list[0])
    print(calorie_list[1])
    print(calorie_list[2])
    print(calorie_list[0] + calorie_list[1] + calorie_list[2])


part1()
