from queue import PriorityQueue

from aoc import read_input


def get_neighbours(x):
    neighbours = []
    if not x // cols == 0:
        neighbours.append(x - cols)
    if not x // cols == (rows - 1):
        neighbours.append(x + cols)
    if not x % cols == 0:
        neighbours.append(x - 1)
    if not x % cols == cols - 1:
        neighbours.append(x + 1)
    return neighbours


def perform_the_search(start_position):
    dijkstra_graph = {v: float('inf') for v in range(vertices)}
    dijkstra_graph[start_position] = 0
    visited = set()

    pq = PriorityQueue()
    #   distance, vertex
    pq.put((0, start_position))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.add(current_vertex)
        current_height = elevation[current_vertex]
        for neighbour in get_neighbours(current_vertex):
            neighbour_height = elevation[neighbour]

            if neighbour_height - current_height <= 1 and neighbour not in visited:
                old_cost = dijkstra_graph[neighbour]
                new_cost = dijkstra_graph[current_vertex] + 1
                if new_cost < old_cost:
                    pq.put((new_cost, neighbour))
                    dijkstra_graph[neighbour] = new_cost

    if not dijkstra_graph[end] == float('inf'):
        possibilities.update({start_position: dijkstra_graph[end]})


lines = read_input("day12", str)
rows = len(lines)
cols = len(lines[0])
vertices = rows * cols
elevation = {}
start = 0
end = 0
possibilities = {}

for r in range(rows):
    for c in range(cols):
        p = (r * cols) + c 
        if lines[r][c] == "S":
            start = p
            elevation.update({p:1})
        elif lines[r][c] == "E":
            end = p
            elevation.update({p: 26})
        else:
            elevation.update({p: ord(lines[r][c]) - 96})


for possibility in elevation:
    if elevation[possibility] == 1:
        perform_the_search(possibility)

values = list(possibilities.values())
values.sort()

# part 1
print(possibilities[start])
# part 2
print(min(values))