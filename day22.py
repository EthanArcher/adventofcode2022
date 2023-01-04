import re

from aoc import read_input_no_strip

edge = 49


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


def get_face(face):
    global face_1, face_2, face_3, face_4, face_5, face_6
    match face:
        case 1:
            return face_1
        case 2:
            return face_2
        case 3:
            return face_3
        case 4:
            return face_4
        case 5:
            return face_5
        case 6:
            return face_6


def move_cube(start_row, start_col, direction, distance, start_face):
    current_row, current_col, current_face, current_direction = start_row, start_col, start_face, direction
    for s in range(distance):
        next_row, next_col, next_face, next_direction = next_pos_cube(current_face, current_row, current_col,
                                                                      current_direction)
        if get_face(next_face)[next_row][next_col] != "#":
            current_row, current_col, current_face, current_direction = next_row, next_col, next_face, next_direction
        else:
            break
    return current_row, current_col, current_face, current_direction


def next_pos_cube(current_face, current_row, current_col, direction):
    new_row, new_col, new_face, new_direction = current_row, current_col, current_face, direction
    match direction:
        case "U":
            if current_row == 0:
                new_face, new_direction, new_row, new_col = next_face_and_direction(current_face, direction,
                                                                                    current_row, current_col)
            else:
                new_row = current_row - 1
        case "D":
            if current_row == edge:
                new_face, new_direction, new_row, new_col = next_face_and_direction(current_face, direction,
                                                                                    current_row, current_col)
            else:
                new_row = current_row + 1
        case "L":
            if current_col == 0:
                new_face, new_direction, new_row, new_col = next_face_and_direction(current_face, direction,
                                                                                    current_row, current_col)
            else:
                new_col = current_col - 1
        case "R":
            if current_col == edge:
                new_face, new_direction, new_row, new_col = next_face_and_direction(current_face, direction,
                                                                                    current_row, current_col)
            else:
                new_col = current_col + 1

    return new_row, new_col, new_face, new_direction


def next_face_and_direction(current_face, current_direction, current_row, current_col):
    match current_direction:
        case "U":
            match current_face:
                case 1:
                    return 6, "R", current_col, 0
                case 2:
                    return 6, "U", edge, current_col
                case 3:
                    return 1, "U", edge, current_col
                case 4:
                    return 3, "R", current_col, 0
                case 5:
                    return 3, "U", edge, current_col
                case 6:
                    return 4, "U", edge, current_col

        case "D":
            match current_face:
                case 1:
                    return 3, "D", 0, current_col
                case 2:
                    return 3, "L", current_col, edge
                case 3:
                    return 5, "D", 0, current_col
                case 4:
                    return 6, "D", 0, current_col
                case 5:
                    return 6, "L", current_col, edge
                case 6:
                    return 2, "D", 0, current_col

        case "L":
            match current_face:
                case 1:
                    return 4, "R", edge - current_row, 0
                case 2:
                    return 1, "L", current_row, edge
                case 3:
                    return 4, "D", 0, current_row
                case 4:
                    return 1, "R", edge - current_row, 0
                case 5:
                    return 4, "L", current_row, edge
                case 6:
                    return 1, "D", 0, current_row

        case "R":
            match current_face:
                case 1:
                    return 2, "R", current_row, 0
                case 2:
                    return 5, "L", edge - current_row, edge
                case 3:
                    return 2, "U", edge, current_row
                case 4:
                    return 5, "R", current_row, 0
                case 5:
                    return 2, "L", edge - current_row, edge
                case 6:
                    return 5, "U", edge, current_row


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

    face_1, face_2, face_3, face_4, face_5, face_6 = list(), list(), list(), list(), list(), list()

    for r in range(0, 50):
        face_1.append(grid[r][50:100])
        face_2.append(grid[r][100:150])

    for r in range(50, 100):
        face_3.append(grid[r][50:100])

    for r in range(100, 150):
        face_4.append(grid[r][0:50])
        face_5.append(grid[r][50:100])

    for r in range(150, 200):
        face_6.append(grid[r][0:50])

    directions = list(filter(None, re.split('(\d+)', direction)))

    # find starting position
    current_row = 0
    for c in range(width):
        if grid[0][c] != " ":
            current_col = c
            break

    # Part 1

    current_direction = "R"

    for d in directions:
        if str(d).isnumeric():
            current_row, current_col = move(current_row, current_col, current_direction, int(d))
        else:
            current_direction = rotate(current_direction, d)

    password = 1000 * (current_row + 1) + 4 * (current_col + 1) + ["R", "D", "L", "U"].index(current_direction)
    print(password)

    # Part 2

    current_row, current_col, current_direction, current_face = 0, 0, "R", 1

    for d in directions:
        if str(d).isnumeric():
            current_row, current_col, current_face, current_direction = move_cube(current_row, current_col,
                                                                                  current_direction, int(d),
                                                                                  current_face)
        else:
            current_direction = rotate(current_direction, d)

    print(current_row, current_col, current_face, current_direction)

    r = current_row + 51
    c = current_col + 51

    password = 1000 * r + 4 * c + current_face

    print(password)
