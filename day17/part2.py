import re
from collections import namedtuple
import fileinput
import math

Target = namedtuple("Target", ["x_min", "x_max", "y_min", "y_max"])


class TooFarError(BaseException):
    pass


class Probe:
    def __init__(self, vel_x: int, vel_y: int, target: Target) -> None:
        self.x = 0
        self.y = 0
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.target = target

    def move(self) -> bool:
        self.x += self.vel_x
        self.y += self.vel_y
        # print(self.x, self.y)
        self.vel_x = self.vel_x - 1 if self.vel_x > 0 else 0
        self.vel_y -= 1

        if self.x > self.target.x_max or self.y < self.target.y_min:
            raise TooFarError()

        if self.x >= self.target.x_min and self.y <= self.target.y_max:
            return True

        return False


def parse_file() -> Target:
    match = re.search("x=(\d+)\.\.(\d+), y=(-*\d+)\.\.(-*\d+)", next(fileinput.input()))
    return Target(int(match[1]), int(match[2]), int(match[3]), int(match[4]))


target = parse_file()
successes = 0

for x in range(1, target.x_max + 1):
    for y in range(target.y_min, target.x_max):
        probe = Probe(x, y, target)

        try:
            while True:
                found = probe.move()

                if found:
                    successes += 1
                    # print("Success!")
                    break
        except TooFarError:
            # print("Went too far!")
            pass

print(successes)
