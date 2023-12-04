import pygame

import sudoku_generator
from cell import Cell
from constants import *


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
            self.board = sudoku_generator.generate_sudoku(9, 30)
        elif difficulty == 2:
            self.board = sudoku_generator.generate_sudoku(9, 40)
        elif difficulty == 3:
            self.board = sudoku_generator.generate_sudoku(9, 50)
        self.rows = len(self.board)
        self.cols = len(self.board[0])
        self.original_board = self.board
        self.selected = None
        self.cells = [[Cell(self.board[row][col], row, col, self.screen) for row in range(self.rows)] * 9 for col in
                      range(self.cols)]

    """
            Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
            Draws every cell on this board.
    """

    def draw(self):
        self.screen.fill((173, 216, 230))
        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(self.screen, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, SCREEN_HEIGHT - 60), 8)
                pygame.draw.line(self.screen, BLACK, (0, i * SQUARE_SIZE), (SCREEN_WIDTH, i * SQUARE_SIZE), 8)
            else:
                pygame.draw.line(self.screen, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, SCREEN_HEIGHT - 60), 2)
                pygame.draw.line(self.screen, BLACK, (0, i * SQUARE_SIZE), (SCREEN_WIDTH, i * SQUARE_SIZE), 2)

        for row_cells in self.cells:
            for cell in row_cells:
                cell.draw()

    """
        Marks the cell at (row, col) in the board as the current selected cell.
        Once a cell has been selected, the user can edit its value or sketched value.
        """

    def select(self, row, col):
        self.selected = self.board[row][col]
        return self.selected

    """
    If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
    of the cell which was clicked. Otherwise, this function returns None.
    """

    def click(self, x, y):
        if 0 < x < self.width and 0 < y < self.width:
            clicked_row = y // SQUARE_SIZE
            clicked_col = x // SQUARE_SIZE
            return (clicked_row, clicked_col)
        return None

    """
    Clears the value cell. Note that the user can only remove the cell values and sketched value that are
    filled by themselves.
    """

    def clear(self):
        row, col = self.selected
        if self.cells[row][col].value != self.original_board[row][col]:
            self.cells[row][col].set_cell_value(0)
            self.cells[row][col].set_sketched_value(0)

    """
    Sets the sketched value of the current selected cell equal to user entered value.
    It will be displayed at the top left corner of the cell using the draw() function.
    """

    def sketch(self, value):
        row, col = self.selected
        self.cells[row][col].set_sketched_value(value)

    """
    Sets the value of the current selected cell equal to user entered value.
    Called when the user presses the Enter key.
    """

    def place_number(self, value):
        if self.selected:
            row, col = self.selected
            cell = self.cells[row][col]
            if cell.value == 0:
                cell.set_cell_value(value)
            cell.set_sketched_value(0)

    """
    Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
    """

    def reset_to_original(self):
        for row_cells in self.cells:
            for cell in row_cells:
                cell.set_cell_value(self.original_board[row_cells][cell])

    """
    Returns a Boolean value indicating whether the board is full or not.
    """

    def is_full(self):
        for row_cells in self.cells:
            for cell in row_cells:
                if cell.value == 0:
                    return False
        return True

    """
    Updates the underlying 2D board with the values in all cells.
    """

    def update_board(self):
        for row in range(self.row):
            for col in range(self.cols):
                self.board[row][col] = self.cells[row][col].value

    """
    Finds an empty cell and returns its row and col as a tuple (x, y).
    """

    def find_empty(self):
        for row_index, row_cells in enumerate(self.cells):
            for col_index, cell in enumerate(row_cells):
                if cell.value == 0:
                    return (row_index, col_index)
        return None

    """
    Check whether the Sudoku board is solved correctly.
    """

    def check_board(self):
        sudoku_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # checks rows
        for row in range(self.rows):
            self.board[row].sort()
            if self.board[row] != sudoku_numbers:
                return False

        # checks columns
        for col in range(self.cols):
            column = [self.board[row][col] for row in range(self.board)]
            column.sort()
            if column != sudoku_numbers:
                return False

        # checks 3x3 grid
        for i in range(0, self.rows, 3):
            for j in range(0, self.cols, 3):
                grid = [self.board[i][j] for i in range(row, row + 3) for j in range(col, col + 3)]
                grid.sort()
                if grid != sudoku_numbers:
                    return False

        return True



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    board = Board(SCREEN_WIDTH, SCREEN_HEIGHT,screen, 1)
    print(board.check_board())
    pygame.display.set_caption("Sudoku")
    while True:
        board.draw()
        board.select(0, 0)
        board.select(0, 3)
        board.click(150, 150)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
