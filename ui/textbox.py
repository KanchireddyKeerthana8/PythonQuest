import pygame


class TextBox:

    def __init__(self, x, y, width, height):

        self.rect = pygame.Rect(
            x,
            y,
            width,
            height
        )

        self.text = ""

        self.active = False

        self.font = pygame.font.Font(
            None,
            40
        )

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            self.active = self.rect.collidepoint(
                event.pos
            )

        if event.type == pygame.KEYDOWN:

            if self.active:

                if event.key == pygame.K_BACKSPACE:

                    self.text = self.text[:-1]

                else:

                    self.text += event.unicode

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            self.rect,
            2
        )

        text_surface = self.font.render(
            self.text,
            True,
            (255, 255, 255)
        )

        screen.blit(
            text_surface,
            (
                self.rect.x + 10,
                self.rect.y + 10
            )
        )