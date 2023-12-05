"""
This file will contain code to create the different screens
of the project (game start, game over, and game in progress),
and will form a cohesive project together with the rest of the code.
"""
import sys
import sudoku_generator
from board import Board
import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((0, 0, 0))
difficulty = 1
background_image_start_screen = pygame.image.load("start_screen_background.jpg")
sudoku_logo = pygame.image.load("sudoku_logo.png")
resized_suduko_logo = pygame.transform.scale(sudoku_logo, (200,200))
easy_button = pygame.Rect(50, 500, BUTTON_WIDTH, BUTTON_HEIGHT)
medium_button = pygame.Rect(225, 500, BUTTON_WIDTH, BUTTON_HEIGHT)
hard_button = pygame.Rect(400, 500, BUTTON_WIDTH, BUTTON_HEIGHT)


def welcome_screen():
    screen.blit(background_image_start_screen, (0, 0))
    screen.blit(resized_suduko_logo, (175,125))
    font = pygame.font.Font("freesansbold.ttf", 52)
    text = font.render("Welcome to Sudoku!", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 550))
    screen.blit(text, text_rect)

    text = font.render("Select Game Mode: ", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)

    # makes the easy button
    button_font = pygame.font.Font("freesansbold.ttf", 18)
    pygame.draw.rect(screen, GRAY, easy_button)
    text = button_font.render("EASY", True, WHITE)
    text_rect = text.get_rect(center=(100, 525))
    screen.blit(text, text_rect)

    # makes the medium button
    button_font = pygame.font.Font("freesansbold.ttf", 18)
    pygame.draw.rect(screen, GRAY, medium_button)
    text = button_font.render("MEDIUM", True, WHITE)
    text_rect = text.get_rect(center=(275, 525))
    screen.blit(text, text_rect)

    # makes the hard button
    button_font = pygame.font.Font("freesansbold.ttf", 18)
    pygame.draw.rect(screen, GRAY, hard_button)
    text = button_font.render("HARD", True, WHITE)
    text_rect = text.get_rect(center=(450, 525))
    screen.blit(text, text_rect)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    sudoku_screen(1)
                elif medium_button.collidepoint(event.pos):
                    sudoku_screen(2)
                elif hard_button.collidepoint(event.pos):
                    sudoku_screen(3)
        pygame.display.update()

def sudoku_screen(difficulty):
    board = Board(SCREEN_HEIGHT, SCREEN_WIDTH, screen, difficulty)
    board.draw()

    # creates the reset button
    button_font = pygame.font.Font("freesansbold.ttf", 18)
    reset_button = pygame.Rect(75, 575, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(screen, GRAY, reset_button)
    text = button_font.render("RESET", True, WHITE)
    text_rect = text.get_rect(center=(125, 600))
    screen.blit(text, text_rect)

    # creates the restart button
    button_font = pygame.font.Font("freesansbold.ttf", 18)
    restart_button = pygame.Rect(225, 575, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(screen, GRAY, restart_button)
    text = button_font.render("RESTART", True, WHITE)
    text_rect = text.get_rect(center=(275, 600))
    screen.blit(text, text_rect)

    # creates the exit button
    button_font = pygame.font.Font("freesansbold.ttf", 18)
    exit_button = pygame.Rect(370, 575, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(screen, GRAY, exit_button)
    text = button_font.render("EXIT", True, WHITE)
    text_rect = text.get_rect(center=(420, 600))
    screen.blit(text, text_rect)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle mouse clicks
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if reset_button.collidepoint(event.pos):
                    board.reset_to_original()
                    board.update_board()
                    sudoku_screen(difficulty)
                elif restart_button.collidepoint(event.pos):
                    welcome_screen()
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                mouse_x, mouse_y = pygame.mouse.get_pos()
                selected_row, selected_col = board.click(mouse_x, mouse_y)
                if board.select(selected_row, selected_col) == 0:
                    board.cells[selected_row][selected_col].selected = True
                    board.cells[selected_row][selected_col].draw()

            # Handle arrow keys
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and selected_row > 0:
                    selected_row -= 1
                    if board.cells[selected_row][selected_col].value == 0:
                        board.cells[selected_row][selected_col].selected = True
                        board.cells[selected_row][selected_col].draw()
                elif event.key == pygame.K_DOWN and selected_row < 8:
                    selected_row += 1
                    if board.cells[selected_row][selected_col].value == 0:
                        board.cells[selected_row][selected_col].selected = True
                        board.cells[selected_row][selected_col].draw()
                elif event.key == pygame.K_LEFT and selected_col > 0:
                    selected_col -= 1
                    if board.cells[selected_row][selected_col].value == 0:
                        board.cells[selected_row][selected_col].selected = True
                        board.cells[selected_row][selected_col].draw()
                elif event.key == pygame.K_RIGHT and selected_col < 8:
                    selected_col += 1
                    if board.cells[selected_row][selected_col].value == 0:
                        board.cells[selected_row][selected_col].selected = True
                        board.cells[selected_row][selected_col].draw()

                # Handle numeric keys
                elif event.unicode and event.unicode.isnumeric() and '1' <= event.unicode <= '9':
                    integer_value = int(event.unicode)
                    board.cells[selected_row][selected_col].set_sketched_value(integer_value)
                    board.cells[selected_row][selected_col].draw()

                # Handle enter keys
                elif event.key == pygame.K_RETURN:
                    board.cells[selected_row][selected_col].set_cell_value(integer_value)
                    board.cells[selected_row][selected_col].set_sketched_value(integer_value)
                    board.place_number(integer_value)
                    board.board[selected_row][selected_col] = integer_value
                    board.cells[selected_row][selected_col].draw()

                    # checks if there is a winner
                    if board.is_full() and board.check_board():
                        print("You win!")
                    elif board.is_full() == True and board.check_board() == False:
                        print("You lose")
        pygame.display.update()

def won_game():
    pass

def lost_game():
    pass


def main():
    pygame.display.set_caption("Sudoku")
    running = True
    welcome_screen()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()


if __name__ == '__main__':
    main()
