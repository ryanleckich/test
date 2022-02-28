import sys

import pygame

from settings import Settings

from ship import Ship

# from bullet import Bullet


class AlienInvasion:
    """Overall Class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settigns = Settings()
        # backgroubd color

        self.screen = pygame.display.set_mode(
            ((self.settings.screen_width, self.settigns.screen_height))
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.bg_color = self.settings.bg_color

    def run_game(self):
        "Start the main  loop for the game."
        while True:
            self._shcek_events()
            self._update_screeen()
            # self.update_bullets()
            self.ship.update()

    # for bullet in self.bullets.copy():
    # if bullet.rect.bottom <= 0:
    # self.bullets.remove(bullet)
    # print(len(self.bullets))

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_q:
            sys.exit()

            # elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # def _fire_bullet(self):
    # if len(self.bullets) < self.settings.bullets_allowed:
    # new_bullet = Bullet(self)
    # self.bullets.add(new_bullet)

    # def _update_bullets(self):
    # self.bullets.update()
    # for bullet in self.bullets.copy():
    # if bullet.rect.bottom <= 0:
    # self.bullets.remove(bullet)
    # print(len(self.bullets))

    def _update_screeen(self):
        self.screen.fill(self.bg_color)
        self.ship.bltime()
        # for bullet in self.bullets.sprites():
        # bullet.draw.bullet()
        pygame.display.flip()

        # self.screen.fill(self.settings.bg_color)


if __name__ == " __main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
