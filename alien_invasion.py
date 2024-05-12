import pygame
from settings import Settings
import sys

def run_game():
    #initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien_invasion')



    #start the main loop for the game
    while True:

        #watch for keyboard or mouse event
        for event in pygame.event.get():
            screen.fill(ai_settings.bg_color)
            if event.type == pygame.QUIT:
                sys.exit()
            # make the most recently screen visible
            pygame.display.flip()

run_game()