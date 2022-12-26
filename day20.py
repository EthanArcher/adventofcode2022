from aoc import read_input


def find_by_index(values, index):
    # check if the current value at that index is correct if not try the next one
    i = 0
    while values[i][1] != index:
        i += 1
    return i


def find_first_by_value(values, value):
    for i in range(len(values)):
        if values[i][0] == 0:
            return i


def mix(values):
    for i in range(size):
        index = find_by_index(values, i)
        v, sp = values[index]

        new_index = (index + v) % (size - 1)
        values.insert(new_index, values.pop(index))
    return values


def read_with_decryption_key(decryption_key_value):
    global lines
    values = list()
    for i in range(size):
        values.append((lines[i] * decryption_key_value, i))
    return values


def part_1():
    mixed = read_with_decryption_key(1)
    for _ in range(1):
        mixed = mix(mixed)
    i_0 = find_first_by_value(mixed, 0)
    sum_i = sum([mixed[(i_0 + i) % len(mixed)][0] for i in range(1000, 3001, 1000)])
    print(sum_i)


def part_2():
    mixed = read_with_decryption_key(811589153)
    for _ in range(10):
        mixed = mix(mixed)
    i_0 = find_first_by_value(mixed, 0)
    sum_i = sum([mixed[(i_0 + i) % len(mixed)][0] for i in range(1000, 3001, 1000)])
    print(sum_i)


if __name__ == "__main__":
    lines = read_input("day20", int)
    size = len(lines)

    # dict of starting position to final position
    # values, starting_position

    part_1()
    part_2()
