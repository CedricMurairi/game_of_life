"""
This program implements the Game of Life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
We assumme that cells at the edges of the board are dead.
"""

# CORE CLASSES
class Board:
    def __init__(self, width, height):
        """Initialize the Board class.

        width -- number of columns
        height -- number of rows
        """
        self.width = width
        self.height = height
        self.live_cells = []
        # generate an n * n grid where n = self.width = self.height
        self.grid = [[Cell((x, y), self) for y in range(self.width)] for x in range(self.height)]

    def get_cell(self, pos):
        """Return a cell given its coordinates.

        pos -- tuple representing the cell's position on the board
        """
        x, y = pos
        return self.grid[x][y]

    # specify the rules for finding neighboring cells on a board
    def find_neighbors(self, cell):
        """Return the coordinates of the neighboring cells.

        cell -- coordinates of the position of the cell on the board e.g. [0, 1]
        """
        x, y = cell.pos
        grid_length = self.height

        neighbors = []
        x_max = x + 1 if x + 1 < grid_length else x
        x_min = x - 1 if x - 1 >= 0 else x
        y_max = y + 1 if y + 1 < grid_length else y
        y_min = y - 1 if y - 1 >= 0 else y

        for i in range(x_min, x_max + 1):
            for j in range(y_min, y_max + 1):
                if i != x or j != y:  # DeMorgan's 1st Law: negating conjuctions
                    neighbors.append((i, j))

        return neighbors

    def update(self):
        """Update the cells' status for the next generation.

        Uses the Conway's Game of Life rules (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
        """
        # write code to update the board
        birth_row, death_row = [], []

        for x in range(self.height):
            for y in range(self.width):
                cell = self.grid[x][y]
                n = cell.count_live_neighbors()

                if cell.status and (n == 2 or n == 3):
                    continue
                elif not cell.status and n == 3:
                    birth_row.append([x, y])
                else:
                    if cell.status:
                        death_row.append((x, y))

        for pos in birth_row:  # cells that will be born
            self.get_cell(pos).set_alive()

        for pos in death_row:  # cells that will die
            self.get_cell(pos).set_dead()

    def __str__(self):
        """Return string representation of the board."""
        return '\n'.join([' '.join([str(cell.status) for cell in row]) for row in self.grid])

class Glider(Board):
    """Define template for SpaceShipBoard class creation

    This class inherits all of its the properties from the main Board class,
    and declare couple of its own methods
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        self.live_cells = [[2, 5], [3, 5], [4, 5], [4, 4], [3, 3]]
        activate_cells(self, self.live_cells)

class LightWeightShip(Board):
    """Define template for the LightWeightShip Board class creation

    This class inherits all of its the properties from the main Board class
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        self.live_cells = [[3, 3], [3, 4], [3, 5], [3, 6], [4, 6], [5, 6], [6, 5], [4, 2], [6, 2]]
        activate_cells(self, self.live_cells)

class MiddleWeightShip(Board):
    """Define template for the MiddleWeightShip Board class creation

    This class inherits all of its the properties from the main Board class
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        self.live_cells = [[3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [4, 7], [5, 7], [6, 6], [7, 4], [4, 2], [6, 2]]
        activate_cells(self, self.live_cells)

class HeavyWeightShip(Board):
    """Define template for the HeavyWeightShip Board class creation

    This class inherits all of its the properties from the main Board class
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        self.live_cells = [[3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [4, 8], [5, 8], [6, 7], [7, 4], [7, 5], [4, 2], [6, 2]]
        activate_cells(self, self.live_cells)

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
        self.status = 0

    def set_alive(self):
        """Change status to 1 (alive)."""
        self.status = 1

    def is_alive(self):
        """Return if a cell has a status of 1 (alive)."""
        return bool(self.status)

def activate_cells(board, positions):
    """Change cells' status to alive (1) given their coordinates.

    positions -- list of cell coordinates to activate (make alive)
    """
    for pos in positions:
        cell = board.get_cell(pos)
        cell.set_alive()
    return board

def next_gen(board):
    """Yield the next generation of the Game of Life board."""
    while True:
        yield board
        board.update()

def main():
    heavy_weight_ship = HeavyWeightShip(15, 15)
    gen = next_gen(heavy_weight_ship)

    for _ in range(10):
        print('\n----------------\n')
        print(next(gen))


if __name__ == '__main__':
    main()
