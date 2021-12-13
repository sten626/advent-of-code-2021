import fileinput
from typing import DefaultDict

vectors = DefaultDict(set)

for line in fileinput.input():
    start, end = line.strip().split("-")
    vectors[start].add(end)
    vectors[end].add(start)

visited_lower = set()
visited_twice = None


def dfs(v: str):
    global visited_twice
    if v == "end":
        return 1

    if v.islower():
        if v in visited_lower:
            visited_twice = v
        else:
            visited_lower.add(v)

    n_paths = 0

    for dest in vectors[v]:
        if (dest in visited_lower and visited_twice is not None) or dest == "start":
            continue

        n_paths += dfs(dest)

    if visited_twice == v:
        visited_twice = None
    elif v in visited_lower:
        visited_lower.remove(v)

    return n_paths


print(dfs("start"))
