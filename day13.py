import json

from aoc import read_input


def is_in_the_right_order(left_side, right_side):
    finished = False
    result = True
    if left_side == right_side:
        return finished, False
    if len(left_side) == 0:
        return True, True
    for p in range(len(left_side)):
        if p == len(right_side):
            return True, False
        left = left_side[p]
        right = right_side[p]
        # print(f'Compare {left_side[p]} vs {right_side[p]}')
        if isinstance(left, list) or isinstance(right, list):
            finished, result = is_in_the_right_order(left if isinstance(left, list) else [left], right if isinstance(right, list) else [right])
        else:
            if left < right:
                return True, True
            elif left == right:
                continue
            else:
                return True, False
        if finished:
            return finished, result
    if len(left_side) < len(right_side):
        return True, True
    return finished, result


def count_of_smaller_packets(comparison_packet):
    count = 1
    for packet in packets:
        if is_in_the_right_order(packet, comparison_packet)[1]:
            count += 1
    return count


if __name__ == "__main__":
    lines = read_input("day13", str)

    # Part 1
    index = 1
    results = {}
    indices_sum = 0
    result = True
    for i in range((len(lines) + 1) // 3):
        result = is_in_the_right_order(json.loads(lines[i * 3]), json.loads(lines[i * 3 + 1]))[1]
        results.update({index: result})
        if result:
            indices_sum += index
        index += 1

    print(indices_sum)

    # Part 2
    packets = []
    for line in lines:
        if not (line.isspace() or line == ""):
            packets.append(json.loads(line))
    packets.append([[2]])
    packets.append([[6]])

    d1 = count_of_smaller_packets([[2]])
    d2 = count_of_smaller_packets([[6]])
    print(d1 * d2)