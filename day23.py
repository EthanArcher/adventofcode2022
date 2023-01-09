import copy
from enum import Enum

from aoc import read_input_no_strip


class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    WEST = 2
    EAST = 3


def get_next_direction(direction: Direction):
    return Direction((direction.value + 1) % 4)


def direction_empty(r, c, direction: Direction):
    global elf_locations
    locations = set()
    match direction:
        case Direction.NORTH:
            locations.add((r - 1, c - 1))
            locations.add((r - 1, c))
            locations.add((r - 1, c + 1))
        case Direction.SOUTH:
            locations.add((r + 1, c - 1))
            locations.add((r + 1, c))
            locations.add((r + 1, c + 1))
        case Direction.WEST:
            locations.add((r - 1, c - 1))
            locations.add((r, c - 1))
            locations.add((r + 1, c - 1))
        case Direction.EAST:
            locations.add((r - 1, c + 1))
            locations.add((r, c + 1))
            locations.add((r + 1, c + 1))
    for l in locations:
        if l in elf_locations: return False
    return True


def get_proposed_location(r, c, dir):
    current_direction = dir
    for d in range(4):
        if direction_empty(r, c, current_direction):
            match current_direction:
                case Direction.NORTH:
                    return r - 1, c
                case Direction.SOUTH:
                    return r + 1, c
                case Direction.WEST:
                    return r, c - 1
                case Direction.EAST:
                    return r, c + 1
        else:
            current_direction = get_next_direction(current_direction)
    return r, c


def adjoining_all_empty(r, c):
    global elf_locations
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if (r + i, c + j) in elf_locations and (r + i, c + j) != (r, c):
                return False
    return True


if __name__ == "__main__":
    lines = read_input_no_strip("day23", str)
    elf_locations = {}
    direction = Direction.NORTH
    proposed_locations = set()
    clashed_proposed_locations = set()
    min_r, max_r, min_c, max_c = float('inf'), 0, float('inf'), 0
    elf_moved = True
    round_count = 0

    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] == "#":
                elf_locations.update({(r, c): (r, c)})

    # change which while condition runs for the different parts
    while round_count < 10:
        # while elf_moved:
        elf_moved = False
        round_count += 1

        for elf in elf_locations:
            r, c = elf
            if not adjoining_all_empty(r, c):
                elf_moved = True
                proposed_location = get_proposed_location(r, c, direction)
                elf_locations.update({(r, c): proposed_location})
                if proposed_location in proposed_locations:
                    clashed_proposed_locations.add(proposed_location)
                else:
                    proposed_locations.add(proposed_location)

        updated_elf_locations = {}
        for elf in elf_locations:
            if elf_locations.get(elf) in clashed_proposed_locations:
                updated_elf_locations.update({elf: elf})
            else:
                updated_elf_locations.update({elf_locations.get(elf): elf_locations.get(elf)})
        elf_locations = copy.deepcopy(updated_elf_locations)
        updated_elf_locations.clear()
        clashed_proposed_locations.clear()
        proposed_locations.clear()
        direction = get_next_direction(direction)

    for elf in elf_locations:
        r, c = elf
        min_r = min(min_r, r)
        max_r = max(max_r, r)
        min_c = min(min_c, c)
        max_c = max(max_c, c)

    print(min_r, max_r, min_c, max_c)
    rectangle = (max_r - min_r + 1) * (max_c - min_c + 1)
    print("rectangle =", rectangle)
    spaces = rectangle - len(elf_locations)
    print("spaces:", spaces)

    print("round:", round_count)
