from typing import Counter, DefaultDict


def main():
    values = []

    with open("input.txt") as f:
        for line in f:
            values.append(line.strip())

    i = 0

    most_common = values.copy()

    while len(most_common) > 1:
        most_common = filter_most_common(most_common, i)
        i += 1

    oxygen = most_common[0]
    oxygen_10 = int(oxygen, 2)
    print(oxygen, oxygen_10)

    least_common = values.copy()
    i = 0

    while len(least_common) > 1:
        least_common = filter_least_common(least_common, i)
        i += 1

    co2 = least_common[0]
    co2_10 = int(co2, 2)
    print(co2, co2_10)

    print(co2_10 * oxygen_10)


def filter_most_common(values, i):
    n_0 = 0
    n_1 = 0
    values_by_bit = DefaultDict(list)

    for value in values:
        bit = value[i]

        if bit == "0":
            n_0 += 1
        else:
            n_1 += 1

        values_by_bit[bit].append(value)

    if n_1 >= n_0:
        return values_by_bit["1"]

    return values_by_bit["0"]


def filter_least_common(values, i):
    n_0 = 0
    n_1 = 0
    values_by_bit = DefaultDict(list)

    for value in values:
        bit = value[i]

        if bit == "0":
            n_0 += 1
        else:
            n_1 += 1

        values_by_bit[bit].append(value)

    if n_1 >= n_0:
        return values_by_bit["0"]

    return values_by_bit["1"]


if __name__ == "__main__":
    main()
