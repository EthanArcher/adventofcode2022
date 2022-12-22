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


def print_chamber(chamber):
    reverse_for_printing = chamber[::-1]
    for i in range(len(reverse_for_printing)):
        print(str(reverse_for_printing[i]).replace("0", " "))


def push_rock(rock, direction, top, chamber):
    can_move = True
    if direction == ">":
        for i in range(len(rock)):
            can_move = can_move and rock[i][6] == 0
            if top + i < len(chamber) and top >= 0:
                for c in range(6):
                    if rock[i][c] > 0 and chamber[top + i][c + 1] > 0:
                        can_move = False
        if can_move:
            for line in rock:
                for i in range(5, -1, -1):
                    line[i + 1] = line[i]
                line[0] = 0
    else:
        for i in range(len(rock)):
            can_move = can_move and rock[i][0] == 0
            if top + i < len(chamber) and top >= 0:
                for c in range(1, 7):
                    if rock[i][c] > 0 and chamber[top + i][c - 1] > 0:
                        can_move = False
        if can_move:
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


def new_rock_falls(rock, chamber):
    # The tall, vertical chamber is exactly seven units wide
    # pushed by a jet of hot gas one unit then fall one unit
    # push rock by jet 4 times, this will be its position when it hits the top row of the chamber
    for i in range(4):
        direction = get_next_direction()
        rock = push_rock(rock, direction, len(chamber) + 3 - i, chamber)

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
            push_rock(rock, direction, top + 1, chamber)

    # add the rock to the chamber
    for r in range(len(rock)):
        if top + r >= len(chamber) - 1:
            chamber.append([0, 0, 0, 0, 0, 0, 0])
        for c in range(7):
            chamber[top + r + 1][c] += rock[r][c]


def find_height_after_rocks_fall(number_of_rocks_to_fall):
    global height_difference_sequence_tracker
    global d_index
    d_index = -1
    last_rock_1_height = 0

    chamber = []
    rock_number = -4
    for i in (range(1, number_of_rocks_to_fall + 1)):
        rock_type = i % 5
        match rock_type:
            case 1:
                rock_number += 5
                new_rock_falls(new_rock_type_1(), chamber)
                height_difference = len(chamber) - last_rock_1_height
                last_rock_1_height = len(chamber)
                height_difference_sequence_tracker += "," + str(height_difference)
            case 2:
                new_rock_falls(new_rock_type_2(), chamber)
            case 3:
                new_rock_falls(new_rock_type_3(), chamber)
            case 4:
                new_rock_falls(new_rock_type_4(), chamber)
            case 0:
                new_rock_falls(new_rock_type_5(), chamber)
    return len(chamber)


if __name__ == "__main__":
    # Construction
    line = read_input("day17", str)[0]
    hot_gas = list(line)
    d_index = -1
    height_difference_sequence_tracker = ""

    p1_height = find_height_after_rocks_fall(2022)
    print(p1_height)
    assert p1_height == 3197
    # Part 1 is 3197

    # Part 2
    # find the sequence
    # take the last half of the sequence and check if it was repeated

    # need to build the table map with the full sequence list
    find_height_after_rocks_fall(5000)
    hdst = height_difference_sequence_tracker.split(",")
    hdst = list(filter(None, hdst))
    sub_sequence = ",".join(hdst[len(hdst) // 2:])

    if sub_sequence[0] == ",": sub_sequence = sub_sequence[1:]
    searching_for_sequence = True
    while searching_for_sequence:
        occurrences = height_difference_sequence_tracker.count(sub_sequence)
        if occurrences > 1:
            searching_for_sequence = False
        else:
            sub_sequence = sub_sequence[sub_sequence.find(",") + 1:]

    height_gains = sub_sequence.split(",")
    rocks_in_sequence = len(height_gains) * 5

    first_occurrence_after = height_difference_sequence_tracker.find(sub_sequence)
    bit_before = height_difference_sequence_tracker[:first_occurrence_after - 1]
    rocks_before_start_sequence = len(bit_before[1:].split(",")) * 5

    total_number_of_rocks = 1000000000000
    repeats = (total_number_of_rocks - rocks_before_start_sequence) // rocks_in_sequence
    remaining_rocks = (total_number_of_rocks - rocks_before_start_sequence) % rocks_in_sequence

    h1 = find_height_after_rocks_fall(rocks_before_start_sequence + rocks_in_sequence)
    h2 = find_height_after_rocks_fall(rocks_before_start_sequence + rocks_in_sequence * 2)

    height_of_sequence = h2 - h1

    rocks_without_sequence = rocks_before_start_sequence + rocks_in_sequence + remaining_rocks
    total_height = find_height_after_rocks_fall(rocks_without_sequence) + ((repeats - 1) * height_of_sequence)

    print(total_height)
    assert total_height == 1568513119571
