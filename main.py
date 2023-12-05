"""
This file will contain code to create the different screens
of the project (game start, game over, and game in progress),
and will form a cohesive project together with the rest of the code.
"""
import sys
from board import Board
from constants import *

# Initializes pygame and other variables that are used
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((0, 0, 0))
difficulty = 1
background = pygame.image.load("background.jpg")
sudoku_logo = pygame.image.load("sudoku_logo.png")
trophy = pygame.image.load("trophy.png")
easy = pygame.image.load("easy.png")
medium = pygame.image.load("medium.png")
hard = pygame.image.load("hard.png")
loser = pygame.image.load("loser.png")
resized_trophy = pygame.transform.scale(trophy, (400, 400))
resized_suduko_logo = pygame.transform.scale(sudoku_logo, (200, 200))
resize_easy = pygame.transform.scale(easy, (100, 100))
resize_medium = pygame.transform.scale(medium, (100, 100))
resize_hard = pygame.transform.scale(hard, (100, 100))
easy_button = pygame.Rect(50, 500, BUTTON_WIDTH, BUTTON_HEIGHT)
medium_button = pygame.Rect(225, 500, BUTTON_WIDTH, BUTTON_HEIGHT)
hard_button = pygame.Rect(400, 500, BUTTON_WIDTH, BUTTON_HEIGHT)


# creates the initial screen which allows the user to choose the difficulty of game
def welcome_screen():

    # adds the images and "Welcome to Sudoku!" message
    screen.blit(background, (0, 0))
    screen.blit(resized_suduko_logo, (175, 125))
    screen.blit(resize_easy, (50, 400))
    screen.blit(resize_medium, (220, 400))
    screen.blit(resize_hard, (400, 400))
    font = pygame.font.Font("freesansbold.ttf", 52)
    text = font.render("Welcome to Sudoku!", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 550))
    screen.blit(text, text_rect)

    # adds the "Select Game Mode: " message
    text = font.render("Select Game Mode: ", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25))
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

    # checks if the buttons got selected
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

# creates the screen with the sudoku
def sudoku_screen(difficulty):
    board = Board(SCREEN_HEIGHT, SCREEN_WIDTH, screen, difficulty) # creates a board object
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

    # checks for any events
    running = True
    while running:
        selected_col = None
        selected_row = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # handles mouse clicks
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

            # handles arrow keys
            elif event.type == pygame.KEYDOWN:
                if selected_row is not None and selected_col is not None:  # checks that a cell was clicked
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

                    # handles numeric keys
                    elif event.unicode and event.unicode.isnumeric() and '1' <= event.unicode <= '9':
                        integer_value = int(event.unicode)
                        board.cells[selected_row][selected_col].set_sketched_value(integer_value)
                        board.cells[selected_row][selected_col].draw()

                    # handles backspace
                    elif event.key == pygame.K_BACKSPACE:
                        board.clear(selected_row, selected_col)
                        board.cells[selected_row][selected_col].draw()

                    # handles enter keys
                    elif event.key == pygame.K_RETURN:
                        board.cells[selected_row][selected_col].set_cell_value(integer_value)
                        board.place_number(integer_value, selected_row, selected_col)
                        board.board[selected_row][selected_col] = integer_value
                        board.update_board()
                        board.cells[selected_row][selected_col].draw()

                        # checks if there is a winner, goes to the screen which displays that the user won the game
                        if board.is_full() and board.check_board():
                            won_game()

                        # else if there isn't a winner, goes to the screen that says the user did not win the game
                        elif board.is_full() == True and board.check_board() == False:
                            lost_game()
                else:
                    pass
        pygame.display.update()

# screen that displays when the user wins the game
def won_game():
    # adds images to the game
    screen.blit(background, (0, 0))
    screen.blit(resized_trophy, (75, 15))

    # creates the text "Game Won!"
    font = pygame.font.Font("freesansbold.ttf", 52)
    text = font.render("Game Won!", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 550))
    screen.blit(text, text_rect)

    # creates the exit button
    button_font = pygame.font.Font("freesansbold.ttf", 18)
    exit_button = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(screen, GRAY, exit_button)
    text = button_font.render("EXIT", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25))
    screen.blit(text, text_rect)

    # checks for any events
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()

# screen that displays when the user loses the game
def lost_game():

    # adds the images to the screen
    screen.blit(background, (0, 0))
    screen.blit(loser, (125, 125))

    # adds the text "Game Lost :("
    font = pygame.font.Font("freesansbold.ttf", 52)
    text = font.render("Game Lost :(", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 550))
    screen.blit(text, text_rect)

    # creates the restart button
    button_font = pygame.font.Font("freesansbold.ttf", 18)
    restart_button = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 50, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(screen, GRAY, restart_button)
    text = button_font.render("RESTART", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 75))
    screen.blit(text, text_rect)

    # checks for any events
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    welcome_screen()
        pygame.display.update()

# the main method
def main():
    pygame.display.set_caption("Sudoku")
    running = True
    welcome_screen()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

# calls the main method
if __name__ == '__main__':
    main()
