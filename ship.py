import pygame


class Ship:
    "A class to manage the ship"

    def __init__(self, ai_game):
        "Initialize the ship and at its starting postion"
        self.screen = ai_game.screen
        self.screeen_rect = ai_game.screen.get_rect()

        # load ths ship image and get its rect
        self.image = pygame.image.load("/Users/ryanleckich/Downloads/ship.bmp")
        self.rect = self.image.get_rect()

        # start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rct.midbottom

        # movement flag
        self.moving_right = False

    def update(self):
        "Update the ship's postion based on the movement flag"
        if self.moving_right:
            self.rect.x += 1

    def bltime(self):
        "Draw ship at its current location"
        self.screen.blit(self.image, self.rect)
