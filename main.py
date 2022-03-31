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
from pygame import mixer
pygame.font.init()
pygame.mixer.init()

# names window and game
pygame.display.set_caption("Imp and Osters Kingdom")

# background music
mixer.music.load('AutumnLeaves.mp3')
mixer.music.play(-1)

# Initializes game and creates clock to run game
class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.char_selection = 1
        self.running = True
        # asset for ground terrain
        self.terrainsheet = Spritesheet('img/terrain1.png')
        # asset for character selection menu pics
        self.char_select_spritesheet = Spritesheet('img/charselection.png')
        # asset for character
        self.char_dictionary = {
            1: Spritesheet('img/Alex_run_16x16.png'),
            2: Spritesheet('img/Amelia_run_16x16.png'),
        }

        self.character_spritesheet = self.char_dictionary[self.char_selection]
        #asset for character selection bg
        self.choosecharacterbg = pygame.image.load('img/charsel.png')
        # asset for trees
        self.treesheet = Spritesheet('img/Serene_Village_XP.png')
        # asset for enemy
        self.enemy_spritesheet = Spritesheet('img/0x72_DungeonTilesetII_v1.3.png')
        # asset for attack animation
        self.attack_spritesheet = Spritesheet('img/attack.png')
        # asset for font style
        self.font = pygame.font.SysFont('comicsans', 70)
        # asset for character choice menu
        self.intro_background = pygame.image.load('img/imps_background.png')


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
        self.all_sprites.update()\

    # defines update for main menu char selection
    def char_update(self):
          self.char_dictionary = {
            1: Spritesheet('img/Alex_run_16x16.png'),
            2: Spritesheet('img/Amelia_run_16x16.png'),
        }   

          self.character_spritesheet = self.char_dictionary[self.char_selection]
          game.new(TILEMAP)


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

        title = self.font.render("Imp and Oster's Kingdom", True, 'black')
        title_rect = title.get_rect(x = 100, y = 100)

        BLACK = (0, 0, 0)

        play_button = Button(WIN_WIDTH/2 - BTN_W/2, 200, BTN_W, BTN_H, 'black', 'white', f"{startresume} Game", 32)
        # (self, x, y, width, height, fg, bg, content, fontsize)
        exit_button = Button(WIN_WIDTH/2 - BTN_W/2, 400, BTN_W, BTN_H, 'black', 'white', "Exit Game", 32)

        # this loop allows our mouse and events to take place on the menu screen
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
                if startresume == "Start":
                    self.character_select()

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

    # this allows for the character selection menu
    def character_select(self):
        char_select = True
        title = self.font.render("Choose your character", True, "white")
        title_rect = title.get_rect(x=100, y=100)

        object_dictionary = {
            "Odinn": [30, 10],
            "Freyja": [30, 10]
        }

        odinn_pic = self.char_select_spritesheet.get_sprite(object_dictionary["Odinn"][0], object_dictionary["Odinn"][1], TILESIZE - 12, TILESIZE + 20)
        odinn_rect = odinn_pic.get_rect(x = 290, y = 200)

        freyja_pic = self.char_select_spritesheet.get_sprite(object_dictionary["Freyja"][0], object_dictionary["Freyja"][1], TILESIZE -12, TILESIZE + 20)
        freyja_rect = freyja_pic.get_rect(x = 440, y = 200)

        odinn_button = Button(260, 320, TILESIZE + 80, TILESIZE, 'white', "black", "Odinn", 20)
        freyja_button = Button(410, 320, TILESIZE + 80, TILESIZE, 'white', "black", "Freyja", 20)

        exit_button = Button(WIN_WIDTH / 2 - BTN_W /2, 400, BTN_W, BTN_H, 'black', "white", "Exit", 32)
        # this code makes all of these things fucntional
        while char_select:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    char_self = False
                    self.running = False
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            # updates character based on mouse press on button of character
            if exit_button.is_pressed(mouse_pos, mouse_pressed):
                self.running = False
                pygame.quit()
                sys.exit()
            elif odinn_button.is_pressed(mouse_pos, mouse_pressed):
                char_select = False
                self.char_selection = 1
                self.char_update()
            elif freyja_button.is_pressed(mouse_pos, mouse_pressed):
                char_select = False
                self.char_selection = 2
                self.char_update()

            #places items on screen menu
            self.screen.blit(self.choosecharacterbg, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(exit_button.image, exit_button.rect)
            self.screen.blit(odinn_button.image, odinn_button.rect)
            self.screen.blit(freyja_button.image, freyja_button.rect)
            self.screen.blit(odinn_pic, odinn_rect)
            self.screen.blit(freyja_pic, freyja_rect)
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

