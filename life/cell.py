"""
    This file implements the Cell class with all its methods. Each cell has a status, a board
    and position.

    We considered the initial status of a cell to be 0 (dead cell).
"""

class Cell:
    """Define template for creating a Cell object.

    A cell's position on the board is a tuple containing the cell's x, y coordinates
    e.g (x, y); x represents the row number while y represents the column number.
    A cell is either dead or alive, these states are represented as 0 or 1 respectively.
    """
    def __init__(self, pos, board):
        """Initialize the Cell class.

        pos -- cell's position on the board
        board -- the Board object which the cell belongs to
        """
        self.status = 0  # cells are dead by default
        self.board = board
        self.pos = pos

    def count_live_neighbors(self):
        """Count the number of neighboring cells with a status of 1 (alive).

        Uses the find_neighbors function defined in life.py to get the
        positions of the neighboring cells.

        Sums the values of each cell's status to get the number of live
        cells.
        """
        neighbors = self.board.find_neighbors(self)
        return sum([self.board.get_cell(pos).status for pos in neighbors])

    def set_dead(self):
        """Change status to 0 (dead)."""
        print('Cell at {} dies.'.format(self.pos))
        self.status = 0

    def set_alive(self):
        """Change status to 1 (alive)."""
        print('Cell at {} lives.'.format(self.pos))
        self.status = 1

    def is_alive(self):
        """Return if a cell has a status of 1 (alive)."""
        return bool(self.status)
