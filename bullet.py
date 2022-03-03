import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        # bullet from current postion
        super().__init__()
        self.screen = ai_game.screen

        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        # bullet at middle top of ships
        self.rect.midtop = ai_game.ship.rect.midtop
        # bulet as decimal on y axis
        self.y = float(self.rect.y)

    def update(self):
        # moves bullet up to alien
        self.y -= self.settings.bullet_speed

        self.rect.y = self.y

    def draw_bullet(self):

        pygame.draw.rect(self.screen, self.color, self.rect)
