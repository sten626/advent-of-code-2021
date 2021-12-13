import fileinput

open_to_close = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

scores = []

for line in fileinput.input():
    chunk_stack = []
    score = 0

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
                break
    else:
        # Not corrupted, non-empty stack means incomplete.
        while chunk_stack:
            opener = chunk_stack.pop()
            closer = open_to_close[opener]
            score = score * 5 + points[closer]

        scores.append(score)

print(sorted(scores)[len(scores) // 2])
