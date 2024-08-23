#Import pygame, constants, other files needed to run in main
import pygame
from constants import *
import os
import math

def main():

    #Init pygame & Set Display
    print("Game Starting")
    os.environ['SDL_VIDEO_WINDOW_POS'] = "1920,0"
    pygame.init()
    clock = pygame.time.Clock()
    FPS = 60
    pygame.display.set_caption("Endless Scroll")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #load image & variables
    bg = pygame.image.load("bg.png").convert()
    bg_width = bg.get_width()
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
    scroll = 0

    #game loop
    running = True
    while running:

        #every tick?
        clock.tick(FPS)

        #drawing background
        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll , 0))
        scroll -= 5
        #resetting scroll
        if abs(scroll) > bg_width:
            scroll = 0
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #update check / loop
        pygame.display.update()

    #quit game loop (Look into how this works)
    pygame.quit()

if __name__ == "__main__":
    main()


