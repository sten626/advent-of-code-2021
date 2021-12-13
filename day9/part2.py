import fileinput
from math import prod

mapping = []

for line in fileinput.input():
    mapping.append(list(map(int, line.strip())))

height = len(mapping)
width = len(mapping[0])
all_seen = set()
basin_sizes = []

for a in range(height):
    for b in range(width):
        pos = mapping[a][b]

        if pos == 9 or (a, b) in all_seen:
            continue

        visited = set()
        all_seen.add((a, b))
        visiting = {(a, b)}

        while visiting:
            a1, b1 = visiting.pop()
            visited.add((a1, b1))

            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ai = a1 + i
                bj = b1 + j

                if 0 <= ai < height and 0 <= bj < width:
                    n = mapping[ai][bj]

                    if n < 9 and (ai, bj) not in visited:
                        all_seen.add((ai, bj))
                        visiting.add((ai, bj))

        basin_sizes.append(len(visited))

print(prod(sorted(basin_sizes)[-3:]))
