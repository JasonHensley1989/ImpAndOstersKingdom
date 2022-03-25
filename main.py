import pygame, sys

# general setup
pygame.init()
clock = pygame.time.Clock()

#sets up main window
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')


rec_width = 40
rec_height = 60
speed = 10

still_playing = True

while still_playing:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         still_playing = False

#updates window
    pygame.display.flip()
    clock.tick(60)

