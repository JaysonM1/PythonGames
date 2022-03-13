from re import S
import pygame
import os
import time
import random

pygame.init()
Width, Height = 720, 800

Win = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Space Invaders")

red_space_ship = pygame.image.load("./Pictures/RedSpaceShip.png")
blue_space_ship = pygame.image.load("./Pictures/BlueSpaceShip.jpg")


red_laser = pygame.image.load("./Pictures/RedLaser.jfif")
blue_laser = pygame.image.load("./Pictures/BlueLaser.png")

background = pygame.image.load("./Pictures/Background.jpg")

class Ship:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
    
    def draw(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50, 50))



def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    
    ship = Ship(300, 600)
    def redraw_window():
        Win.blit(background, (0,0))

        lives_text = main_font.render(f"Lives: {lives}", 1, (255,0,0))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        Win.blit(lives_text, (10,10))
        Win.blit(level_label, (Width - level_label.get_width() - 10,10))

        ship.draw(Win)
        pygame.display.update()


    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            ship.x -=1




main()