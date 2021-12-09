from statistics import mean, median


def parseFile(filename):
    with open(filename) as f:
        return [int(n) for n in next(f).strip().split(",")]


def main():
    crab_positions = parseFile("input.txt")
    print(crab_positions)
    # avg_pos = round(mean(crab_positions))
    avg_pos = int(median(crab_positions))
    print(avg_pos)
    fuel = sum(abs(avg_pos - pos) for pos in crab_positions)
    print(fuel)


if __name__ == "__main__":
    main()
