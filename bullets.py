import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # class to manage bullet fired from ship
    def __init__(self, ai_game):
        super().__init__()
