import sys

from aoc import read_input


def count_neighbour_faces_not_connected(x, y, z, this_face):
    faces = 6
    if x > 0 and cubes[x - 1][y][z] == this_face: faces -= 1
    if x < max_dimension and cubes[x + 1][y][z] == this_face: faces -= 1
    if y > 0 and cubes[x][y - 1][z] == this_face: faces -= 1
    if y < max_dimension and cubes[x][y + 1][z] == this_face: faces -= 1
    if z > 0 and cubes[x][y][z - 1] == this_face: faces -= 1
    if z < max_dimension and cubes[x][y][z + 1] == this_face: faces -= 1
    return faces


def flood_fill(x, y, z):
    if x < 0 or x > max_dimension or 0 < y > max_dimension or z < 0 or z > max_dimension:
        return
    if cubes[x][y][z] != 0:
        return

    cubes[x][y][z] = 2
    flood_fill(x + 1, y, z)
    flood_fill(x - 1, y, z)
    flood_fill(x, y + 1, z)
    flood_fill(x, y - 1, z)
    flood_fill(x, y, z + 1)
    flood_fill(x, y, z - 1)


if __name__ == "__main__":
    # Construction
    lines = read_input("day18", str)
    max_dimension = 0
    sys.setrecursionlimit(10000)
    print(sys.getrecursionlimit())
    for line in lines:
        x, y, z = line.split(",")
        max_dimension = max(max_dimension, int(x), int(y), int(z))

    cubes = [[[0 for x in range(max_dimension + 1)] for y in range(max_dimension + 1)] for z in
             range(max_dimension + 1)]
    for line in lines:
        x, y, z = line.split(",")
        cubes[int(x)][int(y)][int(z)] = 1

    # Part 1 - find all the faces
    total_faces = 0
    for x in range(max_dimension + 1):
        for y in range(max_dimension + 1):
            for z in range(max_dimension + 1):
                if cubes[x][y][z] == 1:
                    total_faces += count_neighbour_faces_not_connected(x, y, z, 1)
    print(total_faces)
    assert total_faces == 4348
    # p1 = 4348

    # Part 2 - remove all the air bubbles
    flood_fill(0, 0, 0)
    air_bubbles = 0
    for x in range(max_dimension + 1):
        for y in range(max_dimension + 1):
            for z in range(max_dimension + 1):
                if cubes[x][y][z] == 0:
                    air_bubbles += count_neighbour_faces_not_connected(x, y, z, 0)
    print(total_faces - air_bubbles)
    assert total_faces - air_bubbles == 2546
    # p2 = 2546
