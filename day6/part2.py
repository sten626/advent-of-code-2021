def parseInput(filename):
    with open(filename) as f:
        return [int(i) for i in next(f).strip().split(",")]


def populate(fish: list, n_days: int):
    # print("Initial state: {}".format(fish))
    fish_counts = {i: 0 for i in range(9)}

    for f in fish:
        fish_counts[f] += 1

    # print(fish_counts)

    for i in range(1, n_days + 1):
        fish_counts = live(fish_counts)
    # print("After {:2d} day{}: {}".format(i, " " if i == 1 else "s", fish))

    print("{} fish".format(sum(fish_counts.values())))


def live(fish_counts: dict):
    result = {i - 1: n for i, n in fish_counts.items()}
    birthing = result[-1]
    del result[-1]

    try:
        result[6] += birthing
    except KeyError:
        result[6] = birthing

    result[8] = birthing

    return result


def main():
    fish = parseInput("input.txt")
    populate(fish, 256)


if __name__ == "__main__":
    main()
