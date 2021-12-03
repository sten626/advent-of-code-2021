class Position:
    def __init__(self) -> None:
        self.x = 0
        self.depth = 0


position = Position()

with open("input.txt") as f:
    for line in f:
        command, amount = line.strip().split(" ")
        amount = int(amount)

        if command == "forward":
            position.x += amount
        elif command == "down":
            position.depth += amount
        elif command == "up":
            position.depth -= amount

print("Horizontal: {}, Depth: {}".format(position.x, position.depth))
print(position.x * position.depth)
