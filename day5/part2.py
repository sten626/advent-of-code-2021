from collections import namedtuple
from itertools import zip_longest


Point = namedtuple("Point", "x y")
Vector = namedtuple("Vector", "start end")


def buildMap(max_value):
    sea_map = []

    for _ in range(max_value):
        row = ["." for _ in range(max_value)]
        sea_map.append(row)

    return sea_map


def countHighRiskPoints(sea_map):
    count = 0

    for x in range(len(sea_map)):
        row = sea_map[x]
        for y in range(len(row)):
            if row[y] != "." and row[y] >= 2:
                count += 1

    return count


def main():
    vectors, max_value = parseInput("input.txt")
    sea_map = buildMap(max_value + 1)
    process(sea_map, vectors)
    high_risk = countHighRiskPoints(sea_map)
    print(high_risk)


def parseInput(filename):
    vent_vectors = []
    values = set()

    with open(filename) as f:
        for line in f:
            start, end = line.strip().split(" -> ")
            x0, y0 = start.split(",")
            x0, y0 = int(x0), int(y0)
            p0 = Point(x0, y0)
            x1, y1 = end.split(",")
            x1, y1 = int(x1), int(y1)
            p1 = Point(x1, y1)
            v = Vector(p0, p1)
            vent_vectors.append(v)
            values.update({x0, y0, x1, y1})

    return vent_vectors, max(values)


def process(sea_map, vectors):
    for start, end in vectors:
        if start.x == end.x:
            x = start.x

            if start.y < end.y:
                r_start = start.y
                r_end = end.y
            else:
                r_start = end.y
                r_end = start.y

            for y in range(r_start, r_end + 1):
                if sea_map[x][y] == ".":
                    sea_map[x][y] = 1
                else:
                    sea_map[x][y] += 1
        elif start.y == end.y:
            y = start.y

            if start.x < end.x:
                r_start = start.x
                r_end = end.x
            else:
                r_start = end.x
                r_end = start.x

            for x in range(r_start, r_end + 1):
                if sea_map[x][y] == ".":
                    sea_map[x][y] = 1
                else:
                    sea_map[x][y] += 1
        else:
            # Diagonal
            x_step = 1 if start.x < end.x else -1
            y_step = 1 if start.y < end.y else -1

            for x, y in zip_longest(
                range(start.x, end.x + x_step, x_step),
                range(start.y, end.y + y_step, y_step),
            ):
                if sea_map[x][y] == ".":
                    sea_map[x][y] = 1
                else:
                    sea_map[x][y] += 1


if __name__ == "__main__":
    main()
