import pygame
from sprites import *
import maps
import random
from config import *

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
        self.image = self.game.character_spritesheet.get_sprite(320, 360, self.width, self.height)
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

        # this code creates sidesteps and jump action these are unique mechanics that can be added or adjusted i.e. speed burst, slow etc..
       
        jumping = False
        jump_height = 10
        y_velocity = jump_height // 2
        x_velocity = jump_height
        y_gravity = 1
        
        if keys[pygame.K_w]:
            jumping = True
            if jumping:
                self.y_change -= y_velocity
                y_velocity -= y_gravity
            if y_velocity < jump_height:
                jumping = False
                jump_height = y_gravity
        if keys[pygame.K_s]:
                jumping = True
                if jumping:
                    self.y_change += y_velocity
                    y_velocity += y_gravity
                if y_velocity < jump_height:
                    jumping = False
                    jump_height = y_gravity
        if keys[pygame.K_a]:
                jumping = True
                if jumping:
                    self.x_change -= x_velocity
                    x_velocity -= y_gravity
                if x_velocity < jump_height:
                    jumping = False
                    jump_height = y_gravity
        if keys[pygame.K_d]:
                jumping = True
                if jumping:
                    self.x_change += y_velocity
                    x_velocity += y_gravity
                if x_velocity < jump_height:
                    jumping = False
                    jump_height = y_gravity
        # this is code for an actual jump all of these are based off the same mechanic as required for jump
        if keys[pygame.K_x]:
                jumping = True
                if jumping:
                    self.y_change -= y_velocity
                    y_velocity -= y_gravity
                if y_velocity < jump_height:
                    jumping = False
                    jump_height = y_gravity


# this is where we make the animation in the character
    def animate(self):
        Player_animation_animate(self)

# this update allows for the character to be updated based on key press, then updates the maps image BEHIND the character so the key presses make the character appear to walk
    def update(self):
        self.movement()

        # this allows the animation to update
        self.animate()

        # this will set collisions and boundaries into the update with the trees 
        # this code allows the map to update as events are triggered     
        self.rect.x += self.x_change
        self.collide_trees('x')
        self.rect.y += self.y_change
        self.collide_trees('y')
        # collisions and boundaries update for houses   
        self.collide_house('x')
        self.collide_house('y')
        self.collide_blue_house('x')
        self.collide_blue_house('y')

        # now the x and y need to be set back to zero so its not just the character moving
        self.x_change = 0
        self.y_change = 0
        # collisions and boundaries update for enemies
       
    

    # this function will make a collision with the trees 

    def collide_trees(self, direction):
        if direction == 'x':
            # this will put it in group of trees, and false make sure it doesnt destroy object when we hit it, it checks the left and right edges of the image to see if collison
            # is occuring if it is it stops it with the player speed
            hits = pygame.sprite.spritecollide(self, self.game.trees, False)
            if hits:
                if self.x_change > 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
                    self.rect.x = hits[0].rect.right
                    
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.trees, False)
            if hits:
                if self.y_change > 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED
                    self.rect.y = hits[0].rect.bottom

    
    
    # this function will make a collision with the houses

    def collide_house(self, direction):
        if direction == 'x':
            # this will put it in group of houses, and false make sure it doesnt destroy object when we hit it, it checks the left and right edges 
            # of the image to see if collision is occuring if it is it stops it with the player speed
            hits = pygame.sprite.spritecollide(self, self.game.house, False)
            if hits:
                if self.x_change > 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
                    self.rect.x = hits[0].rect.right
                    
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.house, False)
            if hits:
                if self.y_change > 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED
                    self.rect.y = hits[0].rect.bottom
    # this function will make a collision with the houses

    def collide_blue_house(self, direction):
        if direction == 'x':
            # this will put it in group of blue houses, and false make sure it doesnt destroy object when we hit it, it checks the left and right edges 
            # of the image to see if collision is occuring if it is it stops it with the player speed
            hits = pygame.sprite.spritecollide(self, self.game.blue_house, False)
            if hits:
                if self.x_change > 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
                    self.rect.x = hits[0].rect.right
                    
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.blue_house, False)
            if hits:
                if self.y_change > 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED
                    self.rect.y = hits[0].rect.bottom




# this function will allow attacks
class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x, self.y = x, y
        self.width, self.height = TILESIZE, TILESIZE
    
        self.animation_loop = 0
        if self.animation_loop == 0:
            self.collidable = True
        self.image = self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

        attack_animation(self)
    # cause collision with enemy
    def update(self):
        self.animate()
        self.collide()
    #destroys enemy
    def collide(self):
        if self.collidable:
            hits = pygame.sprite.spritecollide(self, self.game.enemies, True)
            if hits:
                pass
    # attack animation
    def animate(self):
        attack_animation_animate(self)