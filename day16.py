from itertools import combinations

from aoc import read_input


def move_to_another_valve(remaining_time, current_position, potential_routes, valves_to_open, current_route, rate,
                          flow):
    for valve in valves_to_open:
        distance = int(a[current_position][valve_to_number_dict.get(valve)])
        # if the time to move to a valve and open it is less than the time remaining
        if distance + 1 < remaining_time:
            remaining_valves_to_open = valves_to_open - {valve}
            # flow while travelling to valve and opening it
            new_flow = flow + rate * (distance + 1)
            new_rate = rate + valve_to_rate_dict.get(valve)
            if remaining_valves_to_open:
                move_to_another_valve(remaining_time - distance - 1, valve_to_number_dict.get(valve), potential_routes,
                                      remaining_valves_to_open, current_route + [valve], new_rate, new_flow)
            else:
                new_flow = new_flow + new_rate * (remaining_time - distance - 1)
                potential_routes.append((current_route + [valve], new_flow))
        else:
            new_flow = flow + (rate * remaining_time)
            potential_routes.append((current_route + [valve], new_flow))


def find_max_flow(potential_routes):
    max_flow = (None, 0)
    for p in potential_routes:
        if p[1] > max_flow[1]:
            max_flow = p
    return max_flow[1]


if __name__ == "__main__":
    # Construction
    lines = read_input("day16", str)
    number_valves = len(lines)
    a = [[float('inf') for x in range(number_valves)] for y in range(number_valves)]

    counter = 0
    valve_to_number_dict = {}
    number_to_valve_dict = {}
    valve_to_rate_dict = {}
    vale_rate_connections = []
    valves_to_open = set()

    for line in lines:
        line = line.replace(",", "")
        separated = line.split(" ")
        valve = separated[1]
        rate = int(str(separated[4].split("=")[1]).replace(";", ""))
        connections = separated[9:]
        valve_to_number_dict.update({valve: counter})
        number_to_valve_dict.update({counter: valve})
        valve_to_rate_dict.update({valve: rate})
        a[counter][counter] = 0
        counter += 1
        vale_rate_connections.append((valve, rate, connections))
        if rate > 0:
            valves_to_open.add(valve)

    for vrc in vale_rate_connections:
        valve, rate, connections = vrc
        for c in connections:
            a[valve_to_number_dict.get(valve)][valve_to_number_dict.get(c)] = 1

    # Floyd-Warshall Algorithm
    # A^k[i, j] = min (A^(k-1)[i, j], A^(k-1)[i, k] + A^(k-1)[k, j])
    for k in range(number_valves):
        for i in range(number_valves):
            for j in range(number_valves):
                a[i][j] = min(a[i][j], a[i][k] + a[k][j])

    # Part 1
    # build all the possible routes that you can cover in less than 30
    potential_routes = []

    move_to_another_valve(remaining_time=30, current_position=valve_to_number_dict.get("AA"),
                          potential_routes=potential_routes, valves_to_open=valves_to_open, current_route=["AA"],
                          rate=0, flow=0)

    max_pressure_released = find_max_flow(potential_routes)
    print("Part 1: ", max_pressure_released)

    # part 1 (['AA', 'YW', 'OM', 'VX', 'WI', 'ZL', 'NG', 'IS', 'MX'], 1751)

    # Part 2
    # you teach an elephant and so now you have 26 minutes not 30
    # need to divide the valves between you and the elephant from the list of valves_to_open
    # as it turns out this completed with a 50/50 split but I added a check for all values just incase

    valve_counter = len(valves_to_open)
    potential_routes = []
    max_pressure_released = 0
    for i in range(valve_counter // 2):
        for c in combinations(valves_to_open, i):
            yours = set(c)
            elephants = set(valves_to_open) - set(c)

            potential_routes = []
            move_to_another_valve(26, valve_to_number_dict.get("AA"), potential_routes, yours, ["AA"], 0, 0)
            your_max = find_max_flow(potential_routes)

            potential_routes = []
            move_to_another_valve(26, valve_to_number_dict.get("AA"), potential_routes, elephants, ["AA"], 0, 0)
            elephants_max = find_max_flow(potential_routes)

            max_pressure_released = max(max_pressure_released, your_max + elephants_max)

    print("Part 2: ", max_pressure_released)
