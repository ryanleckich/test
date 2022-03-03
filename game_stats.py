class GameStats:
    def __init__(self, ai_game):

        self.settings = ai_game.settings
        self.reset_stats()

        # game over when ships are 0
        self.game_active = False

        # keep high scores
        self.high_score = 0

    def reset_stats(self):
        # live stats
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
