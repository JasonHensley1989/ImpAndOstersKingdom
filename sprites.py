import pygame
from config import *
import random
from animation import *
import maps

# in order to build out map below we need a class
class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width, self.height = TILESIZE, TILESIZE
        # actual location on sprite sheet of asset being used
        self.image = self.game.terrainsheet.get_sprite(0, 96, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

        
# Also need a class for sprite sheets, aka assets to bring in
class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey('black')
        return sprite

# Creates trees
class Tree(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        # this line creates a new layer between the ground and player
        self._layer = BLOCK_LAYER
        # this allows the loop to include this in the all sprites update
        self.groups = self.game.all_sprites, self.game.trees
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width, self.height = TILESIZE + 250, TILESIZE + 45
        self.image = self.game.treesheet.get_sprite(0, 1500, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        #this line of code will probably be removed this is in case the background of the image does not come out right, this needs to be put into maps
        self.image.set_colorkey('black')