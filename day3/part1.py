from typing import Counter, DefaultDict

values_by_index = DefaultDict(list)

with open("input.txt") as f:
    for line in f:
        line = line.strip()

        for i in range(len(line)):
            values_by_index[i].append(line[i])

gamma_rate = ""
epsilon_rate = ""

for i in sorted(values_by_index):
    counter = Counter(values_by_index[i])
    common, uncommon = counter.most_common(2)
    gamma_rate += common[0]
    epsilon_rate += uncommon[0]

gamma_10 = int(gamma_rate, 2)
epsilon_10 = int(epsilon_rate, 2)

print("Gamma: {} -> {}".format(gamma_rate, gamma_10))
print("Epsilon: {} -> {}".format(epsilon_rate, epsilon_10))
print(gamma_10 * epsilon_10)
