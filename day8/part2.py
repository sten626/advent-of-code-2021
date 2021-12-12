# from typing import Deque
import fileinput


# digits_by_segments = {5: {2, 3, 5}, 6: {0, 6, 9}}
# unique = {2: 1, 3: 7, 4: 4, 7: 8}

# Subsets
# - 0: 1, 7
# - 1: None
# 2: None
# - 3: 1, 7
# - 4: 1
# 5: None
# 6: 5
# - 7: 1
# - 8: 0, 1, 2, 3, 4, 5, 6, 7, 9
# 9: 1, 3, 4, 5, 7

# Supersets
# - 0: 8
# - 1: 0, 4, 7, 8, 9
# 2: 8
# - 3: 8, 9
# - 4: 8, 9
# 5: 6, 8, 9
# 6: 8
# - 7: 0, 3, 8, 9
# - 8: None
# 9: 8


# def countDigitsWithUniqueSegments(outputs):
#     unique_amounts = {2, 3, 4, 7}
#     return len([i for i in outputs if len(i) in unique_amounts])


# def parseOutputValues(filename):
#     outputs = []

#     with open(filename) as f:
#         for line in f:
#             output = line.split("|")[1].split()
#             outputs.extend(output)

#     return outputs


# def parseSignalPatterns(filename):
#     patterns = []

#     with open(filename) as f:
#         for line in f:
#             patterns_for_line = line.split("|")[0].split()
#             patterns.append(patterns_for_line)

#     return patterns


for line in fileinput.input():
    signals, output = line.strip().split(" | ")
    # print("{} => {}".format(signals, output))
    d = {l: set(s) for s in signals.split() if (l := len(s)) in {2, 4}}
    print(d)
