import pygame
from pygame.sprite import Sprite

from settings import Settings


class Bullet(Sprite):
    # class to manage bullet fired from ship
    def __init__(self, ai_game):
        # creat bullets object at ship current postion
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.bullet_color

        # creat bullet at (0,0) and then set current postion
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # store bullet postion as decimal
        self.y = float(self.rect.y)

        def update(self):
            # move bullet up screen
            self.y -= self.settings.bullet_speed
            # update rect postion
            self.rect.y = self.y

        def draw_bullet(self):
            # draw bullet on screen
            pygame.draw.rect(self.screen, self.color, self.rect)
