"""
    This program implements the Game of Life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
    We assumme that cells at the edges of the board are dead.
"""

import boards
import sys

def select_board():
    boards_ = [boards.Glider, boards.LightWeightShip, boards.MiddleWeightShip, boards.HeavyWeightShip]
    print("Boards: \n"
          "1. Glider\n"
          "2. Light Weight Ship\n"
          "3. Middle Weight Ship\n"
          "4. Heavy Weight Ship\n")

    bd_index = int(input("Enter a corresponding number to choose a board: ")) - 1

    if bd_index < 0 or bd_index > 3:
        raise IndexError("Could not find a board with that index.")

    def make_board(width, height):
        print("Creating your board...")
        board = boards_[bd_index](width, height)
        print("Done!")
        return board

    return make_board

def main():
    print("Welcome to Conway's Game of Life, select a board to start the game.")
    make_board = select_board()
    n = int(input("How many rows or columns should your board have? "))
    board = make_board(n, n)
    gen = boards.next_gen(board)
    nxt = 'next'

    while nxt.lower() == 'next':
        print('\n{}\n'.format('--' * board.height))
        print(next(gen))
        nxt = input("< type next to see the next generation > OR < type anything you want to quit >")
    sys.exit()


if __name__ == '__main__':
    main()
