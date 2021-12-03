from typing import Deque


depths = Deque(maxlen=3)
n_inc = 0

with open("input.txt") as f:
    for line in f:
        num = int(line)

        if len(depths) < 3:
            depths.append(num)
            continue

        prev = sum(depths)
        depths.append(num)

        if sum(depths) > prev:
            n_inc += 1

    print(n_inc)
