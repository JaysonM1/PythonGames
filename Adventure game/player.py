import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rectangle = self.image.get_rect(topleft = position)
