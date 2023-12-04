import pygame

import sudoku_generator
from constants import *
from cell import Cell


# This class represents an entire Sudoku board. A Board object has 81 Cell objects.


class Board(Cell):
    """
            Constructor for the Board class.
            screen is a window from PyGame.
            difficulty is a variable to indicate if the user chose easy, medium, or hard.
    """

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        if difficulty == 1:
            self.board = sudoku_generator.generate_sudoku(9,30)
        elif difficulty == 2:
            self.board = sudoku_generator.generate_sudoku(9, 40)
        elif difficulty == 3:
            self.board == sudoku_generator.generate_sudoku(9, 50)
        self.cells = [[Cell(self.board[row][col],row, col, self.screen) for row in range(9)] * 9 for col in range(9)]

    """
            Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
            Draws every cell on this board.
    """

    def draw(self):
        screen.fill((173, 216, 230))
        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0), (0, i * 100), (900, i * 100), 8)
                pygame.draw.line(self.screen, (0, 0, 0), (i * 100, 0), (i * 100, 900),8)
            else:
                pygame.draw.line(self.screen, (0, 0, 0), (0, i * 100), (900, i * 100), 2)
                pygame.draw.line(self.screen, (0, 0, 0), (i * 100, 0), (i * 100, 900),2)

        for row_cells in self.cells:
            for cell in row_cells:
                cell.draw()


    """
        Marks the cell at (row, col) in the board as the current selected cell.
        Once a cell has been selected, the user can edit its value or sketched value.
        """

    def select(self, row, col):
        current_cell = self.board[row][col]
        return current_cell

    def click(self, x, y):
        if 0 < x < self.width and 0 < y < self.width:
           clicked_row = y // 100
           clicked_col = x // 100
           return (clicked_row,clicked_col)
        return None
        """
        If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
        of the cell which was clicked. Otherwise, this function returns None.
        """

    def clear(self):
        pass
        """
        Clears the value cell. Note that the user can only remove the cell values and sketched value that are
        filled by themselves.
        """


    def sketch(self, value):
        """
        Sets the sketched value of the current selected cell equal to user entered value.
        It will be displayed at the top left corner of the cell using the draw() function.
        """

    def place_number(self, value):
        """
        Sets the value of the current selected cell equal to user entered value.
        Called when the user presses the Enter key.
        """

    def reset_to_original(self):
        for row_cells in self.cells:
            for cell in row_cells:
                cell.set_cell_value()
        """
        Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
        """

    def is_full(self):
        for row_cells in self.cells:
            for cell in row_cells:
                if cell.value == 0:
                    return False
        return True
        """
        Returns a Boolean value indicating whether the board is full or not.
        """

    def update_board(self):
        """
        Updates the underlying 2D board with the values in all cells.
        """

    def find_empty(self):
        for row_index,row_cells in enumerate(self.cells):
            for col_index,cell in enumerate(row_cells):
                if cell.value == 0:
                    return (row_index,col_index)
        return -1
        """
        Finds an empty cell and returns its row and col as a tuple (x, y).
        """

    def check_board(self):
        """
        Check whether the Sudoku board is solved correctly.
        """


if __name__ == "__main__":
    pygame.init()
    width = 900
    height = 1000
    height = 900
    screen = pygame.display.set_mode((width, height))
    board = Board(width, height, screen, 1)
    print(board.find_empty())
    pygame.display.set_caption("Sudoku")
    while True:
        board.draw()
        board.select(0, 0)
        board.select(0,3)
        board.click(150,150)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
