class Position:
    def __init__(self) -> None:
        self.x = 0
        self.depth = 0
        self.aim = 0


position = Position()

with open("input.txt") as f:
    for line in f:
        command, amount = line.strip().split(" ")
        amount = int(amount)

        if command == "forward":
            position.x += amount
            position.depth += position.aim * amount
        elif command == "down":
            position.aim += amount
        elif command == "up":
            position.aim -= amount

print("Horizontal: {}, Depth: {}".format(position.x, position.depth))
print(position.x * position.depth)
