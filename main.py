"""
This file will contain code to create the different screens
of the project (game start, game over, and game in progress),
and will form a cohesive project together with the rest of the code.
"""
import sys
import sudoku_generator
from board import Board
from button import Button
import pygame
from constants  import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((0,0,0))
difficulty = 0

def welcome_screen():
    font = pygame.font.Font("freesansbold.ttf", 52)
    text = font.render("Welcome to Sudoku!", True, GRAY)
    text_rect = text.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 500))
    screen.blit(text,text_rect)

    text = font.render("Select Game Mode: ", True, GRAY)
    text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    screen.blit(text, text_rect)

    # makes the easy button
    easy_button = pygame.Rect(100,100,BUTTON_WIDTH,BUTTON_HEIGHT)
    easy_button = Button(50,500, BUTTON_WIDTH, BUTTON_HEIGHT, GRAY, "EASY", WHITE, screen)
    easy_button.draw()

    # makes the medium button
    medium_button = pygame.Rect(100, 100, BUTTON_WIDTH, BUTTON_HEIGHT)
    medium_button = Button(200, 500, BUTTON_WIDTH, BUTTON_HEIGHT, GRAY, "MEDIUM", WHITE, screen)
    medium_button.draw()

    # makes the hard button
    hard_button = pygame.Rect(400, 100, BUTTON_WIDTH, BUTTON_HEIGHT)
    hard_button = Button(345, 500, BUTTON_WIDTH, BUTTON_HEIGHT, GRAY, "HARD", WHITE, screen)
    hard_button.draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if easy_button.clicked_button(event):
                sudoku_screen(1)
            elif medium_button.clicked_button(event):
                sudoku_screen(2)
            elif hard_button.clicked_button(event):
                sudoku_screen(3)
        pygame.display.update()
    pygame.display.flip()

def sudoku_screen(difficulty):
    Board(SCREEN_HEIGHT, SCREEN_WIDTH, screen, difficulty).draw()


def main():
    running = True
    while running:
        welcome_screen()
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()


if __name__ == '__main__':
    main()
