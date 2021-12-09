import functools
from statistics import mean, median
from functools import lru_cache


def parseFile(filename):
    with open(filename) as f:
        return [int(n) for n in next(f).strip().split(",")]


def totalFuel(total_movement):
    return sum(range(1, total_movement + 1))


def main():
    crab_positions = parseFile("input.txt")
    # print(crab_positions)
    median_pos = int(median(crab_positions))
    mean_pos = round(mean(crab_positions))
    start = min(median_pos, mean_pos)
    end = max(median_pos, mean_pos)
    fuels = set()

    for i in range(start, end + 1):
        fuel = sum(totalFuel(abs(i - pos)) for pos in crab_positions)
        print("{} -> {}".format(i, fuel))
        fuels.add(fuel)

    print(min(fuels))


if __name__ == "__main__":
    main()
