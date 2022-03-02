import sys

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet
from alien import Alien
from button import Button


class AlienInvasion:
    """Overall Class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        # backgroubd color

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_heigth = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.bg_color = self.settings.bg_color

    def run_game(self):
        # Start the main  loop for the game."
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

            # get rid of bullets that hvae dissappeared
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))

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

        # game ends when you press q
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_h:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # update bullet postion
        self.bullets.update()
        # get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # print(len(self.bullets))

    def _create_fleet(self):
        # alien creation
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # fleeting of aliens creating
        alien_width = alien.rect.width
        # width aviable subtracting two widths of aliens
        available_space_x = self.settings.screen_width - (2 * alien_width)

        # puts aliens of screen.
        # it calculates the aviable space and divides by 2 * aliens
        number_aliens_x = available_space_x // (2 * alien_width)

        # how many rows of aliens fit on screen
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)

        # creates alien row
        for row_number in range(number_rows):
            # creates the first row of aliens
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        if not self.state.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == "__main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
