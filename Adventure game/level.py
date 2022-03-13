import pygame
from tile import Tile
from player import Player
from settings import *

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        ##sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for column_index, column in enumerate(row):
                x = column_index * TILESIZE
                y = row_index * TILESIZE
                if column == 'x':
                    Tile((x,y), [self.visible_sprites])

    def run(self):
        ## update and redraw
        self.visible_sprites.draw(self.display_surface)