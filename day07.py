from aoc import read_input


def build_directories(current_level_contents, remaining_commands, current_directory):
    command = remaining_commands.pop(0).split(" ")
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == "..":
                return current_level_contents
            current_directory = command[2]
            current_level_contents.update({current_directory: build_directories({}, remaining_commands, current_directory)})
        if command[1] == "ls":
            while remaining_commands and not remaining_commands[0].startswith("$"):
                command = remaining_commands.pop(0).split(" ")
                if command[0].isnumeric():
                    file_size, filename = command
                    current_level_contents.update({filename: file_size})
                elif command[0] == "dir":
                    current_level_contents.update({command[1]: {}})
    if remaining_commands:
        build_directories(current_level_contents, remaining_commands, current_directory)
    return current_level_contents


def find_total_size_of_dir(directory, key):
    current_sum = 0
    for d, c in directory.items():
        if isinstance(c, dict):
            current_sum += find_total_size_of_dir(c, d)
        else:
            current_sum += int(c)
    sizes.append(current_sum)
    return current_sum


def part1():
    find_total_size_of_dir(directories.get("/"), "/")
    filtered = list(filter(lambda size: size < 100000, sizes))
    return sum(filtered)
    
    
def part2():
    total_disk_space = 70000000
    required = 30000000
    sizes.sort(reverse=True)
    used_space = sizes[0]
    space_to_clear = used_space + required - total_disk_space
    closest = total_disk_space
    for size in sizes:
        if size < space_to_clear:
            return closest
        closest = size
    return closest


commands = read_input("day07", str)
sizes = []
directories = build_directories({}, commands, "")

p1 = part1()
print(p1)

p2 = part2()
print(p2)

assert (p1 == 1423358)
assert (p2 == 545729)