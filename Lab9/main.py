import numpy as np


class Stage(object):
    def __init__(self, start, end, dimension, danger_points):
        self.start = start
        self.current = tuple(list(start))
        self.end = end
        self.dimension = dimension
        self.board = np.zeros((dimension, dimension), dtype=int)
        for danger_point in danger_points:
            self.board[danger_point[0], danger_point[1]] = -1
        self.board[start] = 1
        self.board[end] = 2

    def next(self, direction):
        self.board[self.current] = 0

        new_position = (self.current[0] + direction[0], self.current[1] + direction[1])
        self.current = new_position

        self.board[self.current] = 1

    def show_board(self):
        print(self.board)


if __name__ == '__main__':
    stage = Stage((0, 0), (3, 3), 4, [(1, 1), (1, 3), (2, 3), (3, 0)])
    stage.show_board()
    stage.next((1, 0))
    stage.show_board()


