from player import *
from sprites import *

# function to create map, will make every row an i and every column a j which will separate
# each spot of the tilemap
def build_map(self, tilemap):
    for i, row in enumerate(tilemap):
        for j, column in enumerate(row):
            Ground(self, j, i)
            # if statement will plug in coordinates according to where location is at p(player)
            if column == "P":
                self.Player = Player(self, j, i)