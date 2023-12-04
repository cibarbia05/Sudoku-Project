import sudoku_generator
from board import Board
import pygame
from constants  import *
"""
This file will contain code to create the different screens
of the project (game start, game over, and game in progress),
and will form a cohesive project together with the rest of the code.
"""
if __name__ == '__main__':
    # THIS WILL BE REMOVED (Sample Boards With Different Difficulties)
    sudoku_generator.generate_sudoku(9, 30)
    sudoku_generator.generate_sudoku(9, 40)
    sudoku_generator.generate_sudoku(9, 50)

