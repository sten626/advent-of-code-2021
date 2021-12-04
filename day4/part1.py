from typing import Deque


class Spot:
    def __init__(self, number) -> None:
        self.number = number
        self.marked = False

    def __repr__(self) -> str:
        return "{}{}".format("M" if self.marked else "", self.number)


def main():
    numbers = Deque()
    board = []
    boards = []

    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if len(numbers) == 0:
                # First line
                for number in line.split(","):
                    numbers.append(int(number))

                continue

            if line == "":
                continue

            row = [Spot(int(num)) for num in line.split()]
            board.append(row)

            if len(board) == 5:
                boards.append(board)
                board = []

    winning_board, last_number = findWinningBoard(numbers, boards)
    unmarked_sum = sumUnmarkedNumbers(winning_board)
    print(unmarked_sum * last_number)


def findWinningBoard(numbers, boards):
    while numbers:
        number = numbers.popleft()

        for board in boards:
            for row_i in range(len(board)):
                row = board[row_i]
                for col_i in range(len(row)):
                    spot = row[col_i]
                    if spot.number == number:
                        spot.marked = True

                        if all(spot.marked for spot in row):
                            return board, number
                        if all(row[col_i].marked for row in board):
                            return board, number


def sumUnmarkedNumbers(board):
    sum = 0

    for row in board:
        for spot in row:
            if not spot.marked:
                sum += spot.number

    return sum


if __name__ == "__main__":
    main()
