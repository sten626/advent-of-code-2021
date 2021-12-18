import fileinput
import re
from collections import Counter

TEMPLATE = re.compile("\w+")
RULE = re.compile("(\w{2}) -> (\w)")

template = None
rules = {}

for line in fileinput.input():
    match = RULE.search(line)
    if match:
        rules[match[1]] = match[2]
        continue

    match = TEMPLATE.search(line)
    if match:
        template = match[0]


def dfs(a, b, n_steps):
    if n_steps == 0:
        return Counter({b: 1})

    x = rules[a + b]

    return Counter(dfs(a, x, n_steps - 1) + dfs(x, b, n_steps - 1))


counter = Counter({template[0]: 1})

for a, b in zip(template, template[1:]):
    counter.update(dfs(a, b, 10))

print(max(counter.values()) - min(counter.values()))
