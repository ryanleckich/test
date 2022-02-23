import pygame


class Ship:
    "A class to manage the ship"

    def __init__(self, ai_game):
        "Initialize the ship and st its starting postion"
        self.screen = ai_game.screen
        self.screeen_rect = ai_game.screen.get_rect()

        # load ths ship image and get its rect
        self.image = pygame.image.load("/Users/ryanleckich/Downloads/ship.bmp")
        self.rect = self.image.get_rect()

        # start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rct.midbottom

    def bltime(self):
        "Draw ship at its current location"
        self.screen.blit(self.image, self.rect)
