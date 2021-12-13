import fileinput

adjacents = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)
octopusus = [list(map(int, list(line.strip()))) for line in fileinput.input()]
max_i = len(octopusus)
max_j = len(octopusus[0])
total = max_i * max_j
step = 0

while True:
    step += 1
    flashing = set()
    flashed = set()

    for i in range(max_i):
        for j in range(max_j):
            if (octopus := octopusus[i][j] + 1) > 9:
                flashing.add((i, j))

            octopusus[i][j] = octopus

    while flashing:
        i, j = flashing.pop()
        flashed.add((i, j))

        for a_i, a_j in adjacents:
            x = i + a_i
            y = j + a_j

            if 0 <= x < max_i and 0 <= y < max_j:
                octopus = octopusus[x][y] + 1
                octopusus[x][y] = octopus

                if octopus > 9 and (x, y) not in flashed:
                    flashing.add((x, y))

    n_flashes = len(flashed)
    print("Step {}: {}/{} flashes".format(step, n_flashes, total))

    if n_flashes >= total:
        break

    while flashed:
        i, j = flashed.pop()
        octopusus[i][j] = 0
