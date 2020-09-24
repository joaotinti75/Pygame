import pygame
from pygame.locals import *
from sys import exit
from random import randrange

import os

x = 500
y = 400

os.environ['SDL_VIDEO_WINDOW_POS'] = f'{(x, y)}'

pygame.init()

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 680

WHITE = (255,255,255)
BLACK = (0,0,0)

FPS = 30

initial_time = 0
current_time = 0

points = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont('arial', 40, True, True)

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.up = False
        self.xpos = 50
        self.ypos = (SCREEN_HEIGHT // 2) + 140
        root = 'dino_google_game/sprites/dino'
        self.dino_imgs = [f'{root}/dinossaur{i}.png' for i in range(3)]

        self.index = 0
        self.image = pygame.image.load(self.dino_imgs[self.index]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (84, 84))
        self.rect = self.image.get_rect()
        self.rect[0], self.rect[1] = self.xpos, self.ypos
        #self.rect.center = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]

    def jump(self):
        self.up = True
        #self.rect[1] = self.ypos - 10
        
    def update(self):
        #JUMP CONDITION
        if self.up == False:
            if self.rect[1] < self.ypos:
                self.rect[1] += 20
            else:
                self.rect[1] = self.ypos
        if self.up == True:
            if self.rect[1] <= self.ypos - 200:
                self.up = False
            else:
                self.rect[1] -= 30
        #SPRITES
        if self.index >= len(self.dino_imgs) - 1:
            self.index = 0
        self.index += 0.25

        self.image = pygame.image.load(self.dino_imgs[int(self.index)]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (128, 128))


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        root = 'dino_google_game/sprites/obstacle'
        self.obstacle_imgs = [f'{root}/obstacle0.png']

        self.image = pygame.image.load(self.obstacle_imgs[0]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (84, 84))
        self.rect = self.image.get_rect()
        self.rect[0], self.rect[1] = (SCREEN_WIDTH // 2) + 300, (SCREEN_HEIGHT // 2) + 162

    def update(self):
        self.rect[0] -= 10

class Clouds(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        root_clouds = 'dino_google_game/sprites/background/clouds'
        self.cloud_imgs = [f'{root_clouds}/clouds0.png']

        self.image = pygame.image.load(self.cloud_imgs[0]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (148, 148))
        self.rect = self.image.get_rect()
        self.rect[0], self.rect[1] = (SCREEN_WIDTH // 2) + randrange(-400, 400, 100) , (SCREEN_HEIGHT // 2) - randrange(100, 400, 100)

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        root_floor = 'dino_google_game/sprites/background/floor'
        self.floor_imgs = [f'{root_floor}/floor0.png']

        self.image = pygame.image.load(self.floor_imgs[0]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect[0], self.rect[1] = 0 , SCREEN_HEIGHT // 2  + 200

dino = Dino()
dino_group = pygame.sprite.Group()
dino_group.add(dino)

obstacle = Obstacle()
obstacle_group = pygame.sprite.Group()
obstacle_group.add(obstacle)

clouds_group = pygame.sprite.Group()
for c in range(10):
    clouds = Clouds()
    clouds_group.add(clouds)

floor_group = pygame.sprite.Group()
for c in range(0, SCREEN_WIDTH, 64):
    floor = Floor()
    floor.rect[0] = c
    floor_group.add(floor)


clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                exit()

            if event.key == K_SPACE:
                dino.jump()

    dino_group.draw(screen)
    dino_group.update()

    obstacle_group.draw(screen)
    obstacle_group.update()

    clouds_group.draw(screen)

    floor_group.draw(screen)

    text = font.render(f'{points}', True, BLACK)
    screen.blit(text, (700, 40))
    points += 1
    
    pygame.display.flip()

