import fileinput
from typing import DefaultDict

vectors = DefaultDict(set)

for line in fileinput.input():
    start, end = line.strip().split("-")
    vectors[start].add(end)
    vectors[end].add(start)

visited_lower = set()


def dfs(v: str):
    if v == "end":
        return 1

    if v.islower():
        visited_lower.add(v)

    n_paths = 0

    for dest in vectors[v]:
        if dest in visited_lower:
            continue

        n_paths += dfs(dest)

    if v in visited_lower:
        visited_lower.remove(v)

    return n_paths


print(dfs("start"))
