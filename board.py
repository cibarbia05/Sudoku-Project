import pygame

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

    """
            Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
            Draws every cell on this board.
    """

    def draw(self):
        screen.fill((173, 216, 230))
        for i in range(1, 9):
            if i % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.width / 9), (self.width, i * self.width / 9), 8)
                pygame.draw.line(self.screen, (0, 0, 0), (i * self.height / 9, 0), (i * self.height / 9, self.height), 8)
            else:
                pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.width / 9), (self.width, i * self.width / 9), 2)
                pygame.draw.line(self.screen, (0, 0, 0), (i * self.height / 9, 0), (i * self.height / 9, self.height),2)

    """
        Marks the cell at (row, col) in the board as the current selected cell.
        Once a cell has been selected, the user can edit its value or sketched value.
        """

    def select(self, row, col):
        current_cell =
        chip_font = pygame.font.Font("freesansbold.ttf", 52)
        chip_x_surf = chip_font.render("x", 0, (255,255,0))
        chip_x_rect = chip_x_surf.get_rect(center=(450,300))
        self.screen.blit(chip_x_surf,chip_x_rect)

        pass

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
        """
        Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
        """

    def is_full(self):
        """
        Returns a Boolean value indicating whether the board is full or not.
        """

    def update_board(self):
        """
        Updates the underlying 2D board with the values in all cells.
        """

    def find_empty(self):
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
    height = 900
    screen = pygame.display.set_mode((width, height))
    board = Board(width, height, screen, "easy")
    pygame.display.set_caption("Sudoku")
    print(board.click(600, 300))
    while True:
        board.draw()
        board.select(9,9)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
