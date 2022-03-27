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
        self.image = self.game.character_spritesheet.get_sprite(320, 0, self.width // 2, self.height)
        # will make it be interpreted as a rectangle so edges can be found
        # will NOT place character on map
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

        Player_animation(self)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'



# this update allows for the character to be updated based on key press, then updates the maps image BEHIND the character so the key presses make the character appear to walk
    def update(self):
        self.movement()

        #this allows the animation to update
        self.animate()

        # this code allows the map to update as events are triggered     
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        # now the x and y need to be set back to zero so its not just the character moving
        self.x_change = 0
        self.y_change = 0

    
# this is where we make the animation in the character
    def animate(self):
        Player_animation_animate(self)