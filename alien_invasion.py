import sys

import pygame

from settings import Settings

from ship import Ship


class AlienInvasion:
    "Overall Class to manage game assets and behavior"

    def __init__(self):
        "Initialize the game, and create game resources."
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # set background color
        self.bg_color = self.settings.bg_color

    def run_game(self):
        "Start the main  loop for the game."
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        "Respond to keypresses and mouse events."
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # redraw the screen during each pass through the loop

    def _update_screen(self):
        "Update images on the screen and flip to the new screen"
        self.screen.fill(self.settings.bg_color)
        self.ship.bltime()

        # MAke the most recently drawwn screen visible.
        pygame.display.flip()


if __name__ == " _main_":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
