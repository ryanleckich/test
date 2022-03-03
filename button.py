import pygame.font


class Button:
    def __init__(self, ai_game, msg):
        # button attributes
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #  dimensions of button
        self.width, self.height = 150, 100
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 50)
        # none default font
        # and 50  text size

        # sets the button  it in the center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # button message
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # msg to an image and centers it
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw blank button and puts image on it
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
