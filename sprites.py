import pygame
from config import *
import random
from animation import *
import maps
# there is a basic layout in the clases below they are first implemented into the game, then they layer is declared, then the update is performed
# and initiliazed. Then finally the dimensions are set for the asset to be used in the loop of the main game
# when using asset sheets in order to remove the background color that is not transparent use self.image.set_colorkey('color of background in image used')


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
        self.image = self.game.terrainsheet.get_sprite(0, 96, self.width * 2, self.height * 2)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

# This class creates the enemy to be brought into the game
class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
        # sets our enemies as tilesize
        self.x, self.y = x * TILESIZE, y * TILESIZE
        self.width, self.height = TILESIZE, TILESIZE
        self.x_change, self.y_change = 0, 0
        # creates a list of left and right and randomly selects for initial facing, then continue left to right after
        self.facing = random.choice(['left', 'right'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(7, 30)
        self.image = self.game.enemy_spritesheet.get_sprite(0, 96, self.width, self.height)
        self.image.set_colorkey('black')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

        # this creates the enemy animation
        enemy_animation(self)

    # this is a function to update player image
    def update(self):
        self.movement()
        self.animate()
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change, self.y_change = 0, 0

    # defines enemy movement
    def movement(self):
        if self.facing == 'left':
            self.x_change -= ENEMY_SPEED
            self.movement_loop -= 1
            # this is set to max travel negative because it takes the distance that its allowed to travel and replaces it with a negative value
            if self.movement_loop <= -self.max_travel:
                self.facing = 'right'

        if self.facing == 'right':
            self.x_change += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = 'left'

    # defines animation for enemy
    def animate(self):
        enemy_animation_animate(self)


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
        self.width, self.height = TILESIZE + 120, TILESIZE + 65
        self.image = self.game.treesheet.get_sprite(10, 1480, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        #this line of code will probably be removed, this is in case the background of the image does not come out right, this needs to be put into maps
        self.image.set_colorkey('black')