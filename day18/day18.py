import fileinput
import json
from math import ceil


def add(left, right):
    return [left, right]


def add_left(node, x):
    if isinstance(node, int):
        return node + x

    l, r = node
    return [add_left(l, x), r]


def add_right(node, x):
    if isinstance(node, int):
        return node + x

    l, r = node
    return [l, add_right(r, x)]


def explode(node, depth=0):
    if isinstance(node, int):
        return node, False, 0, 0

    l, r = node

    if depth >= 4 and isinstance(l, int) and isinstance(r, int):
        return 0, True, l, r

    l, exploded, exp_l, exp_r = explode(l, depth=depth + 1)

    if exploded:
        if exp_r != 0:
            r = add_left(r, exp_r)
            exp_r = 0
    else:
        r, exploded, exp_l, exp_r = explode(r, depth=depth + 1)

        if exploded and exp_l != 0:
            l = add_right(l, exp_l)
            exp_l = 0

    if exploded:
        return [l, r], True, exp_l, exp_r

    return node, False, 0, 0


def magnitude(node):
    if isinstance(node, int):
        return node

    l, r = node

    return 3 * magnitude(l) + 2 * magnitude(r)


def parseFile() -> list:
    return [json.loads(line) for line in fileinput.input()]


def split(node):
    if isinstance(node, int):
        if node >= 10:
            return [node // 2, ceil(node / 2)], True

        return node, False

    l, r = node

    l, was_split = split(l)

    if was_split:
        return [l, r], True

    r, was_split = split(r)

    if was_split:
        return [l, r], True

    return [l, r], False


def part1():
    numbers = parseFile()
    numbers.reverse()
    added = numbers.pop()

    while numbers:
        added = add(added, numbers.pop())

        while True:
            while True:
                added, exploded, _, _ = explode(added)

                if not exploded:
                    break

            added, was_split = split(added)

            if not was_split:
                break

    print(added)
    print(magnitude(added))


def part2():
    numbers = parseFile()
    mag_map = {}
    n_numbers = len(numbers)

    for i in range(n_numbers):
        for j in range(n_numbers):
            if i == j:
                continue

            added = add(numbers[i], numbers[j])

            while True:
                while True:
                    added, exploded, _, _ = explode(added)

                    if not exploded:
                        break

                added, was_split = split(added)

                if not was_split:
                    break

            mag_map[(i, j)] = magnitude(added)

    print(max(mag_map.values()))


part1()
part2()
