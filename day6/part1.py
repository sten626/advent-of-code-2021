def parseInput(filename):
    with open(filename) as f:
        return [int(i) for i in next(f).strip().split(",")]


def populate(fish: list, n_days: int):
    print("Initial state: {}".format(fish))

    for i in range(1, n_days + 1):
        live(fish)
        # print("After {:2d} day{}: {}".format(i, " " if i == 1 else "s", fish))

    print("{} fish".format(len(fish)))


def live(fish: list):
    n_new_fish = 0

    for i, n in enumerate(fish):
        if n == 0:
            fish[i] = 6
            n_new_fish += 1
        else:
            fish[i] -= 1

    fish.extend([8] * n_new_fish)


def main():
    fish = parseInput("input.txt")
    populate(fish, 80)


if __name__ == "__main__":
    main()
