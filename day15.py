from tqdm import tqdm

from aoc import read_input


def positions_on_line_taken(location, line, line_coverage):
    # The Manhattan Distance between two points is given by |X1 – X2| + |Y1 – Y2|.
    sensor_x, sensor_y, beacon_x, beacon_y = location
    manhattan_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

    sensor_location_and_range.append((sensor_x, sensor_y, manhattan_distance))

    if line in range(sensor_y - manhattan_distance, sensor_y + manhattan_distance + 1):
        lines_away = sensor_y - line
        d = manhattan_distance - abs(lines_away)
        for i in range(sensor_x - d, sensor_x + d + 1):
            line_coverage.add(i)

    return line_coverage


def point_is_covered_refined(point):
    # if the distance from the beacon to the point is less than the manhatten distance then its covered
    p_x, p_y = point
    for sensor in sensor_location_and_range:
        sensor_x, sensor_y, mh = sensor
        if abs(sensor_x - p_x) + abs(sensor_y - p_y) <= mh:
            return True
    print(point)
    print(point[0] * 4000000 + point[1])
    return False


def check_edges_of_scanners(location):
    # The Manhattan Distance between two points is given by |X1 – X2| + |Y1 – Y2|.
    sensor_x, sensor_y, beacon_x, beacon_y = location
    manhattan_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

    # add top right bottom left (x,y)
    top = (sensor_x, sensor_y - manhattan_distance)
    right = (sensor_x + manhattan_distance, sensor_y)
    bottom = (sensor_x, sensor_y + manhattan_distance)
    left = (sensor_x - manhattan_distance, sensor_y)
    beacon_coverage.append((top, right, bottom, left))

    outside = 4000000

    for i in range(manhattan_distance + 1):
        top_top = (top[0] + i, top[1] - 1 + i)
        right_right = (right[0] + 1 - i, right[1] + i)
        bottom_bottom = (bottom[0] - i, bottom[1] + 1 - i)
        left_left = (left[0] - 1 + i, left[1] - i)
        # top of top -> right
        if 0 <= top_top[0] <= outside and 0 <= top_top[1] <= outside:
            if not point_is_covered_refined(top_top): return False
        # right of right to bottom
        if 0 <= right_right[0] <= outside and 0 <= right_right[1] <= outside:
            if not point_is_covered_refined(right_right): return False
        # bottom of bottom to left
        if 0 <= bottom_bottom[0] <= outside and 0 <= bottom_bottom[1] <= outside:
            if not point_is_covered_refined(bottom_bottom): return False
        # left of left to top
        if 0 <= left_left[0] <= outside and 0 <= left_left[1] <= outside:
            if not point_is_covered_refined(left_left): return False
    return True


if __name__ == "__main__":
    # Construction
    lines = read_input("day15", str)
    locations = []
    beacon_coverage = []
    sensor_location_and_range = []
    for line in lines:
        coordinates = line.split("at ")
        sensor = coordinates[1].split(":")[0]
        beacon = coordinates[2]
        sensor_coordinates = sensor.split(",")
        beacon_coordinates = beacon.split(",")
        sensor_x, sensor_y = sensor_coordinates[0].split("=")[1], sensor_coordinates[1].split("=")[1]
        beacon_x, beacon_y = beacon_coordinates[0].split("=")[1], beacon_coordinates[1].split("=")[1]
        locations.append((int(sensor_x), int(sensor_y), int(beacon_x), int(beacon_y)))

    # Part 1
    line_coverage = set()
    line_to_check = 2000000
    for location in locations:
        line_coverage.update(positions_on_line_taken(location, line_to_check, line_coverage))

    for location in locations:
        # remove all sensors
        if location[1] == line_to_check:
            line_coverage.discard(location[0])
        # remove all beacons
        if location[3] == line_to_check:
            line_coverage.discard(location[2])

    print(len(line_coverage))

    # Part 2
    '''
    the distress beacon must have x and y coordinates each
    no lower than 0 and no larger than 4000000
    '''
    for location in tqdm(locations):
        if not check_edges_of_scanners(location):
            break
           