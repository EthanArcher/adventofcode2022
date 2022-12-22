from aoc import read_input


def new_rock_type_1():
    return [[0, 0, 1, 1, 1, 1, 0]]


def new_rock_type_2():
    return [[0, 0, 0, 2, 0, 0, 0],
            [0, 0, 2, 2, 2, 0, 0],
            [0, 0, 0, 2, 0, 0, 0]]


def new_rock_type_3():
    return [[0, 0, 3, 3, 3, 0, 0],
            [0, 0, 0, 0, 3, 0, 0],
            [0, 0, 0, 0, 3, 0, 0]]


def new_rock_type_4():
    return [[0, 0, 4, 0, 0, 0, 0],
            [0, 0, 4, 0, 0, 0, 0],
            [0, 0, 4, 0, 0, 0, 0],
            [0, 0, 4, 0, 0, 0, 0]]


def new_rock_type_5():
    return [[0, 0, 5, 5, 0, 0, 0],
            [0, 0, 5, 5, 0, 0, 0]]


def print_chamber():
    reverse_for_printing = chamber[::-1]
    for i in range(len(reverse_for_printing)):
        print(str(reverse_for_printing[i]).replace("0", " "))


def push_rock(rock, direction, top):
    global chamber
    if direction == ">":
        can_move_right = True
        for i in range(len(rock)):
            can_move_right = can_move_right and rock[i][6] == 0
            if top + i < len(chamber) and top >= 0:
                for c in range(6):
                    if rock[i][c] > 0 and chamber[top + i][c + 1] > 0:
                        can_move_right = False
        if can_move_right:
            for line in rock:
                for i in range(5, -1, -1):
                    line[i + 1] = line[i]
                line[0] = 0
    else:
        can_move_left = True
        for i in range(len(rock)):
            can_move_left = can_move_left and rock[i][0] == 0
            if top + i < len(chamber) and top >= 0:
                for c in range(1, 7):
                    if rock[i][c] > 0 and chamber[top + i][c - 1] > 0:
                        can_move_left = False
        if can_move_left:
            for line in rock:
                for i in range(6):
                    line[i] = line[i + 1]
                line[6] = 0
    return rock


def get_next_direction():
    global d_index
    if d_index + 1 < len(hot_gas):
        d_index += 1
    else:
        d_index = 0
    return hot_gas[d_index]


def new_rock_falls(rock):
    # The tall, vertical chamber is exactly seven units wide
    # pushed by a jet of hot gas one unit then fall one unit
    global chamber
    # push rock by jet 4 times, this will be its position when it hits the top row of the chamber
    for i in range(4):
        direction = get_next_direction()
        rock = push_rock(rock, direction, len(chamber) + 3 - i)

    top = len(chamber) - 1
    falling = True
    while top >= 0 and falling:
        # check if the rock can fall
        for i in range(len(rock)):
            if top + i < len(chamber) and top >= 0:
                for c in range(7):
                    # if there is a bit of rock check the row below
                    if rock[i][c] > 0 and chamber[top + i][c] > 0:
                        falling = False
                        break
        if falling and top >= 0:
            # no collision so keeps falling
            # apply the jet of air
            top -= 1
            direction = get_next_direction()
            # need to add a way to check if there is rock in the direction
            push_rock(rock, direction, top + 1)

    # add the rock to the chamber
    for r in range(len(rock)):
        if top + r >= len(chamber) - 1:
            chamber.append([0, 0, 0, 0, 0, 0, 0])
        for c in range(7):
            chamber[top + r + 1][c] += rock[r][c]


if __name__ == "__main__":
    # Construction
    line = read_input("day17", str)[0]
    hot_gas = list(line)
    d_index = -1

    chamber = []

    for i in range(1, 2023):
        rock_type = i % 5
        match rock_type:
            case 1:
                new_rock_falls(new_rock_type_1())
            case 2:
                new_rock_falls(new_rock_type_2())
            case 3:
                new_rock_falls(new_rock_type_3())
            case 4:
                new_rock_falls(new_rock_type_4())
            case 0:
                new_rock_falls(new_rock_type_5())

    print_chamber()
    print(len(chamber))

    # Part 1 is 3197
