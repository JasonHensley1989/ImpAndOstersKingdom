# imports pygame and sys window
from termios import TAB1
import pygame, sys

# names window and game
pygame.display.set_caption("Imp and Osters Kingdom")

# sets window height and width and FPS
WIN_WIDTH = 800
WIN_HEIGHT = 600
TILESIZE = 32
FPS = 60

# in order to build out map below we need a class
class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = 1
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
        return sprite

# function to create map, will make every row an i and every column a j which will separate
# each spot of the tilemap
def build_map(self, tilemap):
    for i, row in enumerate(tilemap):
        for j, column in enumerate(row):
            Ground(self, j, i)

# Initializes game and creates clock to run game
class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        # asset for ground terrain
        self.terrainsheet = Spritesheet('terrain1.png')

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


# Create Tilemap, just an enumerated list to lay map on
TILEMAP = [
    '.....................................',
    '.....................................',
    '.....................................',
    '.....................................',
    '.....................................',
    '.....................................',
    '.....................................',
    '.....................................',
    '.....................................',
    '.....................................',
    '.....................................',
    '.....................................',
    '.....................................',
    '.....................................',
    '.....................................',
    '.....................................',
    '.....................................',
    '.....................................',
    '.....................................',
    '.....................................',
]

# tells game what to run and when in relation to starting and stopping
game = Game()
game.new(TILEMAP)
while game.running:
    game.main()

pygame.quit()
sys.exit()

