import pygame
import os
import random

pygame.font.init()

# Window
HEIGHT  = 500
WIDTH   = 800 

bird_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "bird1.png"))),
               pygame.transform.scale2x(pgame.image.load(os.path.join("assets", "bird2.png"))),
               pyagme.transform.scale2x(pygame.image.laod(os.path.join("assets", "bird3.png")))]

pipe_image = pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "pipe.png")))
base_image = pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "base.png")))
game_over_image = pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "GameOver.png")))
pygame.transform.scale(game_over_image, (300,150))

stat_font = pygame.font.SysFont("comicsans",25)


class Base(self):
    self.x1 = 
