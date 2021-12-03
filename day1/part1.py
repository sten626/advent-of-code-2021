with open("input.txt") as f:
    prev = None
    n_inc = 0

    for line in f:
        num = int(line)

        if prev is None:
            prev = num
            continue

        if num > prev:
            n_inc += 1

        prev = num

    print(n_inc)
