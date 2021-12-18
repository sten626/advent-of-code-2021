import fileinput
import itertools
import math
from collections import defaultdict
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
    map.append(row)

start = (0, 0)
end = (len(map) - 1, len(map[0]) - 1)


def get_neighbours(graph, v):
    neighbours = set()
    v_i, v_j = v

    for i, j in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        n_i = v_i + i
        n_j = v_j + j

        if 0 <= n_i < len(graph) and 0 <= n_j < len(graph[n_i]):
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

    while not queue.isEmpty():
        u = queue.pop()

        for n in get_neighbours(graph, u).intersection(queue.entry_finder):
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
