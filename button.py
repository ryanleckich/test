import pygame.font


class Button:
    def __init__(self, ai_game, msg):
        # these are button attributes
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #  set the dimensions of button in the game
        self.width, self.height = 150, 100
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(
            None, 48
        )  # none is the default font, and 48 is the size of the text

        # this code sets the button as a rect and positions
        # it in the center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # this is the button message
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # turns msg into an image and centers it
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw a blank button with a message drawn on it
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
