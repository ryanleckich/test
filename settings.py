class Settings:
    def __init__(self):
        # replaced
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # bullet settings
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # this limits the number of bullets on the screen

        # how fast ships moves left and right
        self.ship_speed = 5
        # this sets the number of ships the player starts with
        self.ship_limit = 3

        # how fast aliens moves
        self.alien_speed = 2.0
        # how fast fleet moves down
        self.fleet_drop_speed = 80
        # 1  move right and -1  move left
        self.fleet_direction = 1
        # how quickly the game speeds up
        self.speedup_scale = 1.1

        # increase point value of alien when difficulty increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

        self.ship_speed = 7.0
        self.bullet_speed = 7.0
        self.alien_speed = 1.0

        # fleet direction
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    # everything is increased once you pass the level
    def increase_speed(self):

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
