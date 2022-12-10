from aoc import read_input


def move_head_in_dir(direction, distance):
    # Move in direction distance times
    for i in range(distance):
        match direction:
            case "U":
                knots[0] = knots[0][0], knots[0][1] + 1
            case "D":
                knots[0] = knots[0][0], knots[0][1] - 1
            case "L":
                knots[0] = knots[0][0] - 1, knots[0][1]
            case "R":
                knots[0] = knots[0][0] + 1, knots[0][1]
        for j in range(9):
            knots[j+1] = check_tail_position(knots[j], knots[j+1])
            knots_travelled[j+1].add(str(knots[j+1]))


def check_tail_position(h,t):
    head_pos_x, head_pos_y = h
    tail_pos_x, tail_pos_y = t
    dx = head_pos_x - tail_pos_x
    dy = head_pos_y - tail_pos_y
    if abs(dx) == 2 and abs(dy) == 2:
        tail_pos_x = tail_pos_x + int(dx / 2)
        tail_pos_y = tail_pos_y + int(dy / 2)
    # if is not diagonally beside or is in the same place
    elif dx != dy and (abs(dx) == 2 or abs(dy) == 2):
        if dy == 2 or dy == -2:
            tail_pos_x = tail_pos_x + dx
            tail_pos_y = tail_pos_y + int(dy/2)
        elif dx == 2 or dx == -2:
            tail_pos_x = tail_pos_x + int(dx/2)
            tail_pos_y = tail_pos_y + dy
    return tail_pos_x,tail_pos_y


instructions = read_input("day09", str)
tail_history = set()
knots = [(0, 0)] * 10
knots_travelled = [set(), set(), set(), set(), set(), set(), set(), set(), set(), set()]
for instruction in instructions:
    direction, distance = instruction.split(" ")
    move_head_in_dir(direction, int(distance))

p1 = len(knots_travelled[1])
print(p1)
assert (p1 == 6367)
p2 = len(knots_travelled[9])
print(p2)
assert (p2 == 2536)