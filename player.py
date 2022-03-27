import pygame
from sprites import *
import maps
from sounds import *
import random

# creates player, brings player into game
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        # pulls our starting information from our build map
        self.x, self.y = x * TILESIZE, y * TILESIZE
        #creates width and height of player
        self.width, self.height = TILESIZE, TILESIZE

        self.x_change = 0
        self.y_change = 0
        #this will be used in animation multiple images depending on direction
        self.facing = 'down'
        #starts animation loop over when initialized
        self.animation_loop = 1
        #will pull this from the image at these positions, needs character sprite sheet
        self.image = self.game.character_spritesheet.get_sprite(48, 0, self.width // 2, self.height)
        # will make it be interpreted as a rectangle so edges can be found
        # will NOT place character on map
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y