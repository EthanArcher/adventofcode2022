from aoc import read_input_no_strip


def convert_from_snafu(v: str):
    global snafu
    total = 0
    reversed_value = v[::-1]
    for d in range(len(reversed_value)):
        multiplier = 5 ** d
        total += multiplier * snafu.get(reversed_value[d])
    return total


def largest_divisor(v: int):
    d = 0
    while v // (5 ** d) >= 5:
        d += 1
    return d


def calculate_v_and_remainder(v: int, l: int, values):
    unit = (5 ** l)
    unit_count = v // unit

    if unit_count >= 3:
        values.update({l + 1: values.get(l + 1, 0) + 1})
        return calculate_v_and_remainder(v - (5 ** (l + 1)), l, values)
    else:
        values.update({l: unit_count})
        return v - (unit * unit_count)


def balance(values, l):
    for i in range(l + 1):
        if values.get(i) > 2:
            values.update({i + 1: values.get(i + 1) + values.get(i) - 2})
            values.update({i: -2})


def convert_to_snafu(v: int):
    global snafu_conv
    snafu = ""
    l = largest_divisor(v)
    remainder = v
    values = {}

    for i in range(l, -1, -1):
        remainder = calculate_v_and_remainder(remainder, i, values)

    balance(values, l)

    for i in range(l + 1, -1, -1):
        snafu += snafu_conv.get(values.get(i, 0))
    return snafu


if __name__ == "__main__":
    lines = read_input_no_strip("day25", str)
    snafu = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
    snafu_conv = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}
    total = 0
    for line in lines:
        total += convert_from_snafu(line)

    print("total:", convert_to_snafu(total))
