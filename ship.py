import pygame


class Ship:
    "A class to manage the ship"

    def __init__(self, ai_game):
        # Initialize the ship and at its starting postion
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ths ship image and get its rect
        self.image = pygame.image.load("/Users/ryanleckich/Downloads/ship.bmp")
        self.rect = self.image.get_rect()

        # start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        "Update the ship's postion based on the movement flag"
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x += self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        "Draw ship at its current location"
        self.screen.blit(self.image, self.rect)
