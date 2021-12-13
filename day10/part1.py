import fileinput

open_to_close = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

score = 0

for line in fileinput.input():
    chunk_stack = []

    for char in line.strip():
        if char in {"(", "[", "{", "<"}:
            chunk_stack.append(char)
        else:
            opener = chunk_stack.pop()

            if open_to_close[opener] == char:
                # Valid
                continue
            else:
                # Corrupted
                score += points[char]
                break

print(score)
