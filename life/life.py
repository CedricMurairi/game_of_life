"""
    This program implements the Game of Life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
    We assumme that cells at the edges of the board are dead.
"""

import boards

def main():
    board = boards.HeavyWeightShip(15, 15)
    gen = boards.next_gen(board)

    for _ in range(5):
        print('\n----------------\n')
        print(next(gen))


if __name__ == '__main__':
    main()