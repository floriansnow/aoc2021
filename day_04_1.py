import numpy


class Board:
    def __init__(self, lines):
        self.board = numpy.array(lines)
        self._marked = []

    def __repr__(self):
        return '\n'.join([str(line)[1:-1] for line in self.board])

    def _is_winner(self, board):
        for row in board:
            if all([-1 == num for num in row]):
                return True
        return False

    def mark(self, num):
        self.board = numpy.where(self.board == num, -1, self.board)
        self._marked.append(num)

    def is_winner(self):
        if self._is_winner(self.board):
            return True
        board = numpy.rot90(self.board)[::-1]
        return self._is_winner(board)

    def get_score(self):
        return numpy.sum(numpy.where(self.board == -1, 0, self.board)) * self._marked[-1]




boards = []
board = []
with open('day_04_input_1') as f:
    inp = f.readlines()
    draws = list(map(int, inp[0].split(',')))
    for line in inp[2:]:
        if not line.strip():
            boards.append(Board(board))
            board = []
        else:
            board.append(list(map(int, line.strip().split())))
    boards.append(Board(board))

winning_boards = []
for num in draws:
    if len(winning_boards) >= len(boards):
        break
    for index, board in enumerate(boards):
        if index in winning_boards:
            continue
        board.mark(num)
        if board.is_winner():
            print(board.get_score())
            winning_boards.append(index)