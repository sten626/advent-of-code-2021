import fileinput

mapping = []

for line in fileinput.input():
    mapping.append(list(map(int, line.strip())))

height = len(mapping)
width = len(mapping[0])
risk_sum = 0

for a in range(height):
    for b in range(width):
        pos = mapping[a][b]

        for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ai = a + i
            bj = b + j

            if 0 <= ai < height and 0 <= bj < width:
                if pos >= mapping[ai][bj]:
                    break
        else:
            risk_sum += pos + 1

print(risk_sum)
