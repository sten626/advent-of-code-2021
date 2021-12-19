import fileinput
import itertools
import math
from heapq import heappop, heappush


class PriorityQueue:
    pq = []
    entry_finder = {}
    REMOVED = "!!"
    counter = itertools.count()

    def add(self, v, priority):
        if v in self.entry_finder:
            self.remove(v)

        count = next(self.counter)
        entry = [priority, count, v]
        self.entry_finder[v] = entry
        heappush(self.pq, entry)

    def remove(self, v):
        entry = self.entry_finder.pop(v)
        entry[-1] = self.REMOVED

    def pop(self):
        while self.pq:
            priority, count, v = heappop(self.pq)
            if v is not self.REMOVED:
                del self.entry_finder[v]
                return v

        raise KeyError("pop from empty queue")

    def isEmpty(self):
        return not self.entry_finder


map = []

for line in fileinput.input():
    row = [int(x) for x in line.strip()]
    row_l = len(row)
    new_row = [x + i // row_l for i, x in enumerate(row * 5)]
    map.append([x - 9 if x > 9 else x for x in new_row])

num_rows = len(map)

for i in range(num_rows, num_rows * 5):
    map.append([x1 - 9 if (x1 := x + 1) > 9 else x1 for x in map[i - num_rows]])

# for row in map:
#     print(row)

start = (0, 0)
end = (len(map) - 1, len(map[0]) - 1)


def get_neighbours(i_len, j_len, v):
    neighbours = set()
    v_i, v_j = v

    for i, j in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        n_i = v_i + i
        n_j = v_j + j

        if 0 <= n_i < i_len and 0 <= n_j < j_len:
            neighbours.add((n_i, n_j))

    return neighbours


def dijkstra(graph, source, goal):
    dist = {source: 0}
    prev = {}
    queue = PriorityQueue()

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            v = (i, j)
            if v != source:
                dist[v] = math.inf
                prev[v] = None
            queue.add(v, dist[v])

    i_len = len(graph)
    j_len = len(graph[0])

    while not queue.isEmpty():
        u = queue.pop()

        for n in get_neighbours(i_len, j_len, u):
            if n not in queue.entry_finder:
                continue

            alt = dist[u] + graph[n[0]][n[1]]

            if alt < dist[n]:
                dist[n] = alt
                prev[n] = u
                queue.add(n, dist[n])

            if n == goal:
                return dist[n]

    return None


cost = dijkstra(map, start, end)

print(cost)
