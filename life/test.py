"""
    Authors: Mthabisi Ndlovu, Cedric Murairi

    This file implements the test cases for the Board and Cell class and their methods.
"""

import unittest
from boards import Board, Glider, LightWeightShip, MiddleWeightShip, HeavyWeightShip
from cell import Cell


class TestCell(unittest.TestCase):
    def setUp(self):
        """This method sets up default board and cell to use for the tests"""
        self.board = Board(8, 8)
        self.cell = Cell((2, 4), self.board)

    def test_default_status(self):
        """This method checks for the default status of the cell -> dead (0)"""
        self.assertFalse(self.cell.is_alive())

    def test_alive(self):
        """This method checks if a cell is indeed alive when we set it alive"""
        self.cell.set_alive()
        self.assertTrue(self.cell.is_alive())

    def test_dead(self):
        """This method checks if a cell is indeed dead when we set it dead"""
        self.cell.set_dead()
        self.assertFalse(self.cell.is_alive())

    def test_position(self):
        """This method checks if the position of the cell after creation is indeed the expected pos"""
        self.assertEqual(self.cell.pos, (2, 4))

    def test_cell_board(self):
        """This method checks if a cell is on the right board"""
        self.assertTrue(isinstance(self.cell.board, Board))
        self.assertEqual(self.cell.board.width, 8)

    def test_count_neighbors(self):
        """This method checks for live neighbors, we assume a single cell on the board (alive or dead)
           would have no live neighbors, all the cells around are dead -> expecting 0
        """
        self.assertEqual(self.cell.count_live_neighbors(), 0)

class TestBoard(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()