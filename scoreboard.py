import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    #this is for scoring purposes

    def __init__(self, ai_game):
        #initializes the attributes
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #this is to initialize the font settings 
        #for the scoreboard we are making
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #prepare the initial score image
        self.prep_score() #this turns the text into an image
        self.prep_high_score()#prepares the initial score images  
        self.prep_level()
        self.prep_ships()
    
    def prep_score(self):
        #this puts the score as an image
        #render means you pass the screen bg color and text color 
        rounded_score = round(self.stats.score,-1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,self.text_color, self.settings.bg_color)

        #the next line makes sure that the score lines up with the right side of the scren 
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 #20 pixels from right send of the screen 
        self.score_rect.top = 20 #sets 20 pixels from the top of the screen 
    
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)#this draws the score to the screen 
        self.screen.blit(self.high_score_image, self.high_score_rect)#draw high score to screen
        self.screen.blit(self.level_image,self.level_rect) #draws image to the screen
        self.ships.draw(self.screen)



    def prep_high_score(self):
        #turns high score into a rendered image 
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.settings.bg_color)

        #centers the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        #turns level into a rendered image for screen use
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str,True,self.text_color,self.settings.bg_color)

        #this puts the level underneath the score you have in the game 
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right #sets image to the right of the score attribute 
        self.level_rect.top = self.score_rect.bottom + 10 #10 pixels beneath bottom of score image 

    def prep_ships(self): #creates an empty group for ships
        #show how many ships we have left
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10 #10 pixels from top