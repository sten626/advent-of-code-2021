import fileinput
import re

dot_pattern = re.compile("(\d+),(\d+)")
fold_pattern = re.compile("fold along ([xy])=(\d+)")
dots = set()
folds = []

for line in fileinput.input():
    dot_match = dot_pattern.match(line)

    if dot_match:
        x, y = int(dot_match.groups()[0]), int(dot_match.groups()[1])
        dots.add((x, y))
        continue

    fold_match = fold_pattern.match(line)
    if fold_match:
        axis = fold_match.groups()[0]
        line = int(fold_match.groups()[1])
        folds.append((axis, line))

for axis, line in folds:
    new_dots = set()

    if axis == "y":
        for x, y in dots:
            if y > line:
                y = line - (y - line)

            new_dots.add((x, y))
    elif axis == "x":
        for x, y in dots:
            if x > line:
                x = line - (x - line)

            new_dots.add((x, y))

    dots = new_dots

max_x = max(dot[0] for dot in dots)
max_y = max(dot[1] for dot in dots)
paper = []

for y in range(max_y + 1):
    row = []

    for x in range(max_x + 1):
        if (x, y) in dots:
            row.append("#")
        else:
            row.append(".")

    paper.append(row)

for row in paper:
    print(row)
