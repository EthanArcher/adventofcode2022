import copy
from enum import Enum

from aoc import read_input_no_strip


class Direction(Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"


def move_wind(r, c, dir):
    match dir:
        case Direction.UP.value:
            if r == 1: r = height - 1
            return r - 1, c, dir
        case Direction.DOWN.value:
            if r == height - 2: r = 0
            return r + 1, c, dir
        case Direction.LEFT.value:
            if c == 1: c = width - 1
            return r, c - 1, dir
        case Direction.RIGHT.value:
            if c == width - 2: c = 0
            return r, c + 1, dir


def get_next_possible_positions(starting_position, time):
    global blizzard_by_time
    next_blizzard = blizzard_by_time.get((time + 1) % len(blizzard_by_time))
    next_blizzard_locations = set()
    for r, c, d in next_blizzard:
        next_blizzard_locations.add((r, c))
    next_positions = set()
    r, c = starting_position
    if not (r, c) in next_blizzard_locations:
        next_positions.add((r, c))
    if r - 1 > 0 and not (r - 1, c) in next_blizzard_locations:
        next_positions.add((r - 1, c))
    if r + 1 < height - 1 and not (r + 1, c) in next_blizzard_locations:
        next_positions.add((r + 1, c))
    if c - 1 > 0 and r < height - 1 and not (r, c - 1) in next_blizzard_locations:
        next_positions.add((r, c - 1))
    if c + 1 < width - 1 and r > 0 and not (r, c + 1) in next_blizzard_locations:
        next_positions.add((r, c + 1))
    return next_positions


def transverse(time, starting_location, end_location):
    positions = set()
    next_positions = set()
    positions.add(starting_location)
    still_travelling = True
    while still_travelling:
        for pos in positions:
            next_positions = next_positions | get_next_possible_positions(pos, time)
        time += 1
        positions = copy.deepcopy(next_positions)
        next_positions.clear()
        if end_location in positions:
            still_travelling = False
    time += 1
    print("time after leg:", time)
    return time


if __name__ == "__main__":
    lines = read_input_no_strip("day24", str)
    directions = [item.value for item in Direction]
    blizzard = set()
    blizzard_by_time = {}
    height = len(lines)
    width = len(lines[0])
    for row in range(height):
        for col in range(width):
            if lines[row][col] in directions:
                blizzard.add((row, col, lines[row][col]))
    blizzard_by_time.update({0: blizzard})

    for i in range(1, (height - 2) * (width - 2)):
        next_blizzard = set()
        for wind in blizzard:
            r, c, d = wind
            next_blizzard.add(move_wind(r, c, d))
        blizzard_by_time.update({i: next_blizzard})
        blizzard = next_blizzard

    starting_position = (0, 1)
    end_position = (height - 2, width - 2)
    positions = set()
    next_positions = set()
    positions.add(starting_position)
    time = 0

    time = transverse(time, starting_position, end_position)
    time = transverse(time, end_position, (1, 1))
    time = transverse(time, starting_position, end_position)
