class Settings:
    # //A class to store all settings for Alien invasions"

    def __init__(self):
        "Initialize the game's settings"
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship setting
        self.ship_speed = 1.5

        # bullet setting
        self.bullet_sped = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
