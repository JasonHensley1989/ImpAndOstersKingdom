# imports pygame, system, animation, config, map, map build, our character, sprites, and sounds

from termios import TAB1
import pygame
import sys
from sounds import *
from player import *
from map_build import *
import maps
from sprites import *
from config import *
pygame.font.init()

# names window and game
pygame.display.set_caption("Imp and Osters Kingdom")

# Initializes game and creates clock to run game
class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        # asset for ground terrain
        self.terrainsheet = Spritesheet('img/terrain1.png')
        # asset for character
        self.character_spritesheet = Spritesheet('img/Alex_run_16x16.png')
        # asset for trees
        self.treesheet = Spritesheet('img/Serene_Village_XP.png')
        # asset for enemy
        self.enemy_spritesheet = Spritesheet('img/0x72_DungeonTilesetII_v1.3.png')
        # asset for attack animation
        self.attack_spritesheet = Spritesheet('img/attack.png')
        # asset for font style
        self.font = pygame.font.SysFont('comicsans', 32)
        # asset for character choice menu
        self.intro_background = pygame.image.load('img/characterpick.png')

    # creates tilemap, to place objects and borders
    def createTilemap(self, tilemap):
        build_map(self, tilemap)

    # allows sprites to play and update
    def new(self, tilemap):  
        self.playing = True 
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.trees = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.createTilemap(tilemap)
        
        
    # create events
    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE :
                    if self.player.facing == 'up':
                        Attack(self, self.player.rect.x, self.player.rect.y - TILESIZE)
                    if self.player.facing == 'down':
                        Attack(self, self.player.rect.x, self.player.rect.y + TILESIZE)
                    if self.player.facing == 'left':
                        Attack(self, self.player.rect.x - TILESIZE, self.player.rect.y)
                    if self.player.facing == 'right':
                        Attack(self, self.player.rect.x  + TILESIZE, self.player.rect.y)
                
               
            
    
    # defines update
    def update(self):
        self.all_sprites.update()

    # defines draw, simply moving the image and limits speed across machines
    def draw(self):
       self.screen.fill('black')
       self.all_sprites.draw(self.screen)
       self.clock.tick(FPS)
    
       pygame.display.update()

    # this defines what happens WHILE the main game is playing which is just events, updates, and drawing which is a loop
    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()

    # defines intro screen, and brings over the top of the game
    
    def intro_screen(self, startresume):
        intro = True

        title = self.font.render("Main Menu", True, 'black')
        title_rect = title.get_rect(x = 280, y = 100)

        play_button = Button(WIN_WIDTH/2 - BTN_W/2, 200, BTN_W, BTN_H, 'black', 'white', f"{startresume} Game", 32)
        # (self, x, y, width, height, fg, bg, content, fontsize)
        exit_button = Button(WIN_WIDTH/2 - BTN_W/2, 400, BTN_W, BTN_H, 'black', 'white', "Exit Game", 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
            elif exit_button.is_pressed(mouse_pos, mouse_pressed):
                self.running = False
                pygame.quit()
                sys.exit()



            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()


# tells game what to run and when in relation to starting and stopping
TILEMAP = maps.world_1.stage_1
game = Game()

# this will create our menu buttons and background
game.intro_screen("Start")

game.new(TILEMAP)
while game.running:
    game.main()

pygame.quit()
sys.exit()

