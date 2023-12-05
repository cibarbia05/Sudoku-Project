# This class represents a single cell in the Sudoku board. There are 81 Cells in a Board.
import pygame
from constants import *


class Cell:
    def __init__(self, value, row, col, screen):
        """
        Constructor for the Cell class
        """
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        """
        Setter for this cell’s values
        """
        self.value = value

    def set_sketched_value(self, value):
        """
        Setter for this cell’s sketched value
        """
        self.sketched_value = value

    def draw(self):
        """
        Draws this cell, along with the value inside it.
        If this cell has a nonzero value, that value is displayed.
        Otherwise, no value is displayed in the cell.
        The cell is outlined red if it is currently selected.
        """
        if self.selected:  # outlines the cell red when selected
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.col * SQUARE_SIZE, self.row * SQUARE_SIZE,
                                                           SQUARE_SIZE, SQUARE_SIZE), 2)

        if self.value == 0 and self.sketched_value != 0:
            pygame.draw.rect(self.screen, BLUE,
                             pygame.Rect(self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 0)
            pygame.draw.rect(self.screen, BLACK,
                             pygame.Rect(self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)
            chip_font = pygame.font.Font(None, 20)  # creates font for sketched value
            chip_surf = chip_font.render(str(self.sketched_value), 0, GRAY)  # defines surface with gray color
            chip_rect = chip_surf.get_rect(
                center=(self.col * SQUARE_SIZE + 10, self.row * SQUARE_SIZE + 10))  # specifies location of upper
            # right corner for sketch
            self.screen.blit(chip_surf, chip_rect)  # draws surface

        elif self.value != 0 and self.sketched_value == 0:
            chip_font = pygame.font.Font(None, 52)  # creates font for value
            chip_surf = chip_font.render(str(self.value), 0, BLACK)  # defines surface with black color
            chip_rect = chip_surf.get_rect(center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE +
                                                   SQUARE_SIZE // 2))  # specifies location
            self.screen.blit(chip_surf, chip_rect)  # draws surface

        elif self.value != 0 and self.sketched_value != 0:
            pygame.draw.rect(self.screen, BLUE,
                             pygame.Rect(self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 0)
            pygame.draw.rect(self.screen, BLACK, pygame.Rect(self.col * SQUARE_SIZE, self.row * SQUARE_SIZE,SQUARE_SIZE, SQUARE_SIZE ), 2)
            chip_font = pygame.font.Font(None, 52)  # creates font for value
            chip_surf = chip_font.render(str(self.value), 0, GRAY)  # defines surface with black color
            chip_rect = chip_surf.get_rect(center=(self.col * SQUARE_SIZE + SQUARE_SIZE // 2, self.row * SQUARE_SIZE +
                                                   SQUARE_SIZE // 2))  # specifies location
            self.screen.blit(chip_surf, chip_rect)  # draws surface
