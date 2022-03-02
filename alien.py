from symtable import SymbolTableFactory
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        # puts alien in starting spot
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # load image of alien
        self.image = pygame.image.load("/Users/ryanleckich/Downloads/alien.bmp")
        self.rect = self.image.get_rect()
        # location of the alien
        # top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        # return alien away from edge
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        # moves alien right
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
