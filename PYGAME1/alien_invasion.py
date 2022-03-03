import sys
from time import sleep


import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    def __init__(self):
        # background setting
        pygame.init()
        self.settings = Settings()

        # full screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # self.screen  allows game elements to be displayed
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        # game stats
        self.stats = GameStats(self)
        # store game stats
        # create a scoreboard
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        # group the fleet of aliens
        self._create_fleet()
        # play button
        self.play_button = Button(self, "Play")

        # set the background color
        self.bg_color = self.settings.bg_color

    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # true means left or right press
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # buttons press = false
            # movement left and right is stopped
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        # start new game when butoon is pressed
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # resets the game settings
            self.settings.initialize_dynamic_settings()
            # see mouse
            pygame.mouse.set_visible(False)

            # reset game stats
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # empty
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet and center the new ship
            self._create_fleet()
            self.ship.center_ship()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # press q to quit
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
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
        # gets rid of bullets that have disappeared
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                # print(len(self.bullets))

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # see if bullets and aliens have collided
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        # repopulate fleet if screen empty
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        # updates the position of the aliens in the fleet
        self._check_fleet_edges()
        self.aliens.update()

        # aliens hit ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # when aliens hit buttom of screen
        self._check_aliens_bottom()

    def _create_fleet(self):
        # create alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # fleet of aliens
        alien_width = alien.rect.width
        # width  minus two alien widths
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # number of aliens  fior the aviable space
        number_aliens_x = available_space_x // (2 * alien_width)
        # how many rows of alien on screen
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)

        # creates rows of aliens
        for row_number in range(number_rows):
            # creates the first row of aliens
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)

        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    # if aliens are at edge
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    # fleet changes directions when hits wall
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
            # this moves the aliens left because of the -1
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        # ships disappear when are hit
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # deletes any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            # new fleet and center ship
            self._create_fleet()
            self.ship.center_ship()
            # stop between games
            sleep(0.5)
        else:
            self.stats.game_active = False
            # mouse is visible
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # adds alien to updated screen
        self.aliens.draw(self.screen)

        # uodates scoreboard to updated screen
        self.sb.show_score()

        # play button if game not live
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
