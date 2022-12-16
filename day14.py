import copy

from aoc import read_input


def falling_sand(sand_unit):
    global nothing_in_the_abyss
    c, r = sand_unit
    if r == floor :
        nothing_in_the_abyss = False
        return

    # check if anything below
    if not (c, r+1) in cave:
        falling_sand((c, r+1))
    elif not (c-1, r+1) in cave:
        falling_sand((c-1, r+1))
    elif not (c+1, r+1) in cave:
        falling_sand((c+1, r+1))
    else:
        # print("sand stopped at ", sand_unit)
        if sand_unit == (500, 0):
            return True
        else:
            cave.add(sand_unit)

if __name__ == "__main__":

    # Construction
    lines = read_input("day14", str)
    cave = set()
    sand_entry_point = (500, 0)
    floor = 0
    nothing_in_the_abyss = True
    
    # Columns, Rows
    for line in lines:
        coordinates = line.split(" -> ")

        for p in range(len(coordinates) - 1):
            from_coordinates = coordinates[p].split(",")
            to_coordinates = coordinates[p+1].split(",")
            from_col, from_row = int(from_coordinates[0]), int(from_coordinates[1])
            to_col, to_row = int(to_coordinates[0]), int(to_coordinates[1])
            floor = max(floor, from_row, to_row)
            # if the columns are equal just do the rows
            if to_col == from_col:
                h_row = max(from_row, to_row)
                l_row = min(from_row, to_row)
                for i in range((h_row - l_row) + 1):
                    cave.add((to_col, l_row + i))
            elif to_row == from_row:
                h_col = max(from_col, to_col)
                l_col = min(from_col, to_col)
                for i in range((h_col - l_col) + 1):
                    cave.add((l_col + i, from_row))

    # add in the infinity floor
    for i in range(1000):
        cave.add((i, floor + 2))
        
    cave_1 = copy.deepcopy(cave)
        

    # Part 1
    sand_counter = 0
    while nothing_in_the_abyss:
        falling_sand(sand_entry_point)
        sand_counter += 1
    print(sand_counter - 1)
    
    # Part 2
    sand_counter = 0
    full = False
    floor += 10
    cave = cave_1
    while not full:
        full = falling_sand(sand_entry_point)
        sand_counter += 1
    print(sand_counter)
