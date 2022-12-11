import copy

from aoc import read_input


def create_function(function_string) -> callable:
    split_function_string = function_string.split(" ")
    operator = split_function_string[4]
    if operator == "+":
        return lambda x: x + (int(split_function_string[5]) if split_function_string[5].isnumeric() else x)
    elif operator == "*":
        return lambda x: x * (int(split_function_string[5]) if split_function_string[5].isnumeric() else x)


def create_test_function(d, t, f) -> callable:
    def decide_where_to_throw(z, monkey_key):
        if z % d == 0:
            monkey_tracker[t].append(z)
        else:
            monkey_tracker[f].append(z)
    return decide_where_to_throw


def divide_by_3(x):
    return x // 3


def modulo_max(x):
    return x % monkey_constant


input_lines = read_input("day11", str)

monkey = 0
monkey_tracker = {}
monkey_operations = {}
monkey_tests = {}
monkey_counter = []
monkey_constant = 1

while input_lines:
    line = input_lines[0]
    line_split = line.split(":")
    if not line or line.isspace():
        monkey += 1
    elif "Starting items:" in line:
        starting_items = [int(x) for x in line_split[1].split(",")]
        monkey_tracker.update({monkey: starting_items})
        monkey_counter.append(0)
    elif "Operation:" in line:
        function = line_split[1]
        monkey_operations.update({monkey: create_function(function)})
    elif "Test:" in line:
        divisor = int(line_split[1].split("divisible by ")[1])
        monkey_constant = monkey_constant * divisor
        throw_to_if_true = int(input_lines[1][-1])
        throw_to_if_false = int(input_lines[2][-1])
        monkey_tests.update({monkey: create_test_function(divisor, throw_to_if_true, throw_to_if_false)})
        input_lines = input_lines[2:]

    input_lines = input_lines[1:]

monkey_tracker_reset = copy.deepcopy(monkey_tracker)


def rounds_of_monkey(monkey_tracker, rounds, worry_manager):
    for i in range(1, rounds + 1):
        for monkey in monkey_tracker:
            for item in monkey_tracker[monkey]:
                monkey_counter[monkey] += 1
                worry_level_after_inspection = worry_manager(monkey_operations[monkey](item))
                monkey_tests[monkey](worry_level_after_inspection, monkey)
            monkey_tracker[monkey].clear()
    monkey_counter.sort(reverse=True)
    print(monkey_counter)
    print(monkey_counter[0] * monkey_counter[1])
    return monkey_counter[0] * monkey_counter[1]


# part1
p1 = rounds_of_monkey(monkey_tracker, 20, divide_by_3)
assert(p1 == 61503)

# reset the monkeys
monkey_tracker = copy.deepcopy(monkey_tracker_reset)
for i in range(len(monkey_counter)):
    monkey_counter[i] = 0

# part2
p2 = rounds_of_monkey(monkey_tracker, 10000, modulo_max)
assert(p2 == 14081365540)
