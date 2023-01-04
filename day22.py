import re

from aoc import read_input_no_strip


def move(start_row, start_col, direction, distance):
    current_row, current_col = start_row, start_col
    for s in range(distance):
        next_row, next_col = next_pos(current_row, current_col, direction)
        if grid[next_row][next_col] != "#":
            current_row, current_col = next_row, next_col
        else:
            break
    return current_row, current_col


def rotate(current_direction, rotation):
    clock = ["R", "D", "L", "U"]
    n = clock.index(current_direction)
    if rotation == "R":
        return clock[(n + 1) % len(clock)]
    else:
        return clock[n - 1]


def next_pos(current_row, current_col, direction):
    global grid
    new_row, new_col = current_row, current_col
    match direction:
        case "U":
            if current_row == 0:
                new_row = len(grid) - 1
            else:
                new_row = current_row - 1
        case "D":
            new_row = (current_row + 1) % len(grid)
        case "L":
            if current_col == 0:
                new_col = width - 1
            else:
                new_col = current_col - 1
        case "R":
            new_col = (current_col + 1) % width

    if grid[new_row][new_col] == " ":
        return next_pos(new_row, new_col, direction)
    else:
        return new_row, new_col


if __name__ == "__main__":
    lines = read_input_no_strip("day22", str)
    direction_of_travel = "R"
    direction = lines[len(lines) - 1]
    width = 0
    grid = list()
    for i in range(len(lines) - 2):
        row = list(lines[i])
        grid.append(row)
        width = max(width, len(lines[i]))

    for r in grid:
        if len(r) < width:
            for c in range(len(r), width):
                r.append(" ")

    # for r in grid:
    #     print(r)

    directions = list(filter(None, re.split('(\d+)', direction)))

    # find starting position
    current_row = 0
    for c in range(width):
        if grid[0][c] != " ":
            current_col = c
            break

    current_direction = "R"

    for d in directions:
        if str(d).isnumeric():
            current_row, current_col = move(current_row, current_col, current_direction, int(d))
        else:
            current_direction = rotate(current_direction, d)

    password = 1000 * (current_row + 1) + 4 * (current_col + 1) + ["R", "D", "L", "U"].index(current_direction)
    print(password)
