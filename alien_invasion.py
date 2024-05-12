import pygame

import sys

def run_game():
    #initialize game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Alien_invasion')

    #set background color
    bg_color = (230,230,230)

    #start the main loop for the game
    while True:

        #watch for keyboard or mouse event
        for event in pygame.event.get():
            screen.fill(bg_color)
            if event.type == pygame.QUIT:
                sys.exit()
            # make the most recently screen visible
            pygame.display.flip()

run_game()