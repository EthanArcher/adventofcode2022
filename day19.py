import re

from aoc import read_input

ORE, CLAY, OBSIDIAN, GEODE = "ORE", "CLAY", "OBSIDIAN", "GEODE"


def collect(robots):
    collected = {}
    for robot, count in robots.items():
        collected.update({robot: count})
    return collected


def get_state(current_robots, collected, time_passed):
    return (current_robots.get(ORE),
            current_robots.get(CLAY),
            current_robots.get(OBSIDIAN),
            current_robots.get(GEODE),
            collected.get(ORE),
            collected.get(CLAY),
            collected.get(OBSIDIAN),
            collected.get(GEODE),
            time_passed)


def build_robots(robots, collected, blueprint, collected_in_minute, time_passed, max_robots):
    potential_states = set()
    collected_after = collected.copy()
    for material in collected_in_minute:
        collected_after.update({material: collected_after.get(material) + collected_in_minute.get(material)})

    # if its not enough material to build a geode robot then add the new state
    if collected.get(ORE) < blueprint.get(GEODE).get(ORE) or collected.get(OBSIDIAN) < blueprint.get(GEODE).get(
            OBSIDIAN):
        potential_states.add(get_state(robots, collected_after, time_passed))

    for robot, costings in blueprint.items():
        can_build = True
        for material, cost in costings.items():
            # check if the number of ore robots is less than the max cost 
            if collected.get(material) >= cost:
                can_build = can_build and True
            else:
                can_build = False
        if can_build and robots.get(robot) < max_robots.get(robot):
            collected_update = collected_after.copy()
            for material in costings:
                collected_update.update({material: collected_update.get(material) - costings.get(material)})
            robots_update = current_robots.copy()
            robots_update.update({robot: current_robots.get(robot) + 1})
            potential_states.add(get_state(robots_update, collected_update, time_passed))

    return potential_states


if __name__ == "__main__":
    lines = read_input("day19", str)
    blueprints = {}
    quality_level = 0
    max_geodes_list = list()
    for line in lines:
        q = list(map(int, re.findall("\d+", line)))
        ore_robot_cost = {ORE: q[1]}
        clay_robot_cost = {ORE: q[2]}
        obsidian_robot_cost = {ORE: q[3], CLAY: q[4]}
        geode_robot_cost = {ORE: q[5], OBSIDIAN: q[6]}
        blueprint = {
            ORE: ore_robot_cost,
            CLAY: clay_robot_cost,
            OBSIDIAN: obsidian_robot_cost,
            GEODE: geode_robot_cost
        }
        blueprints.update({q[0]: blueprint})

    # for each blueprint discover how many geodes we have after 24 mins
    for id, blueprint in blueprints.items():
        print(id, " ", blueprint)

        blueprint = blueprints.get(id)
        max_ore = max(blueprint.get(ORE).get(ORE), blueprint.get(CLAY).get(ORE), blueprint.get(OBSIDIAN).get(ORE),
                      blueprint.get(GEODE).get(ORE))
        max_clay = int(blueprint.get(OBSIDIAN).get(CLAY))
        max_obsidian = int(blueprint.get(GEODE).get(OBSIDIAN))
        max_robots = {ORE: max_ore, CLAY: max_clay, OBSIDIAN: max_obsidian, GEODE: 100}
        time_passed = 0
        starting_robots = {ORE: 1, CLAY: 0, OBSIDIAN: 0, GEODE: 0}

        current_robots = starting_robots.copy()
        collected = {ORE: 0, CLAY: 0, OBSIDIAN: 0, GEODE: 0}
        potential_states = set()
        potential_states.add(get_state(current_robots, collected, time_passed))

        for i in range(32):
            previous_states_copy = potential_states.copy()
            time_passed += 1
            potential_states = set()
            for p in previous_states_copy:
                collected = {ORE: p[4], CLAY: p[5], OBSIDIAN: p[6], GEODE: p[7]}
                current_robots = {ORE: p[0], CLAY: p[1], OBSIDIAN: p[2], GEODE: p[3]}
                collected_in_minute = collect(current_robots)
                potential_states.update(build_robots(current_robots, collected, blueprint,
                                                     collected_in_minute, time_passed, max_robots))

            max_geodes_so_far = 0
            for state in potential_states:
                max_geodes_so_far = max(max_geodes_so_far, state[7])

            states_with_max_geodes = set()
            for state in potential_states:
                if state[7] >= max_geodes_so_far:
                    states_with_max_geodes.add(state)

            # filter the list down
            optimal_states = set()
            potential_states = states_with_max_geodes.copy()
            for state in potential_states:
                # if it is the max position then add it
                max_state = True
                for other_state in potential_states:
                    if (len(potential_states) > 1 and
                            state != other_state and
                            state[0] <= other_state[0] and
                            state[1] <= other_state[1] and
                            state[2] <= other_state[2] and
                            state[3] <= other_state[3] and
                            state[4] <= other_state[4] and
                            state[5] <= other_state[5] and
                            state[6] <= other_state[6] and
                            state[7] <= other_state[7]):
                        max_state = False
                if max_state:
                    optimal_states.add(state)
            potential_states = optimal_states.copy()

        print(max_geodes_so_far)
        max_geodes_list.append(max_geodes_so_far)
        quality_level += max_geodes_so_far * id
        print(max_geodes_so_far * id)

    print(quality_level)
    # P1 == 1382
    print(max_geodes_list[0] * max_geodes_list[1] * max_geodes_list[2])
    # P2 == 31740
