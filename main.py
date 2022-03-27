# imports pygame, system, animation, config, map, map build, our character, sprites, and sounds
import imp
from termios import TAB1
import pygame, sys
from sounds import *
from player import *
from map_build import *
import maps
from sprites import *
from config import *

# names window and game
pygame.display.set_caption("Imp and Osters Kingdom")

# Initializes game and creates clock to run game
class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        # asset for ground terrain
        self.terrainsheet = Spritesheet('terrain1.png')
        # asset for character
        self.character_spritesheet = Spritesheet('Alex_idle_16x16.png')

    # creates tilemap, to place objects and borders
    def createTilemap(self, tilemap):
        build_map(self, tilemap)

    # allows sprites to play and update
    def  new(self, tilemap):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.createTilemap(tilemap)

    # create events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    
    # defines update
    def update(self):
        self.all_sprites.update()

    # defines draw, simply moving the image and limits speed across machines
    def draw(self):
       self.screen.fill('black')
       self.all_sprites.draw(self.screen)
       self.clock.tick(FPS)
    
       pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()




# tells game what to run and when in relation to starting and stopping
TILEMAP = maps.world_1.stage_1
game = Game()
game.new(TILEMAP)
while game.running:
    game.main()

pygame.quit()
sys.exit()

