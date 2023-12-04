import pygame


class Button:
    def __init__(self, x, y, width, height, color, text, text_color, screen):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.screen = screen
        self.clicked = False

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=self.rect.center)
        self.screen.blit(text, text_rect)

    def clicked_button(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return True
        return False