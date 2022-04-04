# from tkinter import font
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

# Creates healthbar class to be used by player
class HealthBar(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        # this line selects a new layer between the ground and player
        self._layer = PLAYER_LAYER
        # this allows the loop to include this in the all sprites update
        self.groups = self.game.all_sprites, self.game.health
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width, self.height = TILESIZE + 130, TILESIZE + 65
        self.image = self.game.health.get_sprite(0, 1475, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        #this line of code will probably be removed, this is in case the background of the image does not come out right, this needs to be put into maps
        self.image.set_colorkey('black')

# Creates trees
class Tree(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        # this line selects a new layer between the ground and player
        self._layer = BLOCK_LAYER
        # this allows the loop to include this in the all sprites update
        self.groups = self.game.all_sprites, self.game.trees
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width, self.height = TILESIZE + 130, TILESIZE + 65
        self.image = self.game.treesheet.get_sprite(0, 1475, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        #this line of code will probably be removed, this is in case the background of the image does not come out right, this needs to be put into maps
        self.image.set_colorkey('black')


# this creates a class to implement a  red house
class House(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.house
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width, self.height = TILESIZE + 115, TILESIZE + 75
        self.image = self.game.housesheet.get_sprite(0, 800, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

# creates blue hosue
class Blue_House(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blue_house
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width, self.height = TILESIZE + 150, TILESIZE + 80
        self.image = self.game.blue_housesheet.get_sprite(5, 1200, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

# creates a small pond
class Pond(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.pond
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width, self.height = TILESIZE + 60, TILESIZE + 60 
        self.image = self.game.pond_spritesheet.get_sprite(65, 130, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

# creates a small island surrounded by water
class Water_With_Island(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.water_with_island
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width, self.height = TILESIZE + 100, TILESIZE + 70 
        self.image = self.game.water_with_island_spritesheet.get_sprite(96, 352, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

# creates a Bridge over Water
class Bridge_Over_Water(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.bridge_over_water
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width, self.height = TILESIZE + 75, TILESIZE + 35 
        self.image = self.game.bridge_over_water_spritesheet.get_sprite(3, 366, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

# creates water
class Water(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.water
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width, self.height = TILESIZE, TILESIZE  
        self.image = self.game.water_spritesheet.get_sprite(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

# creates rock path
class Dirt(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.dirt
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width, self.height = TILESIZE, TILESIZE  
        self.image = self.game.dirt_spritesheet.get_sprite(0, 65, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

# This creates a button class for the menu options
class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.SysFont('comicsans', fontsize)
        self.content  = content
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.fg, self.bg = fg, bg
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y
        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center = (self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False