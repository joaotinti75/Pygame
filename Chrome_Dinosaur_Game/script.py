import pygame
from pygame.locals import *
from sys import exit
from random import randrange, choice

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
GAME_SPEED = 10
FLOOR_SPEED = 10

points = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont('arial', 40, True, True)
score_sound = pygame.mixer.Sound('dino_google_game/songs/score_sound.wav')

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.jump_sound = pygame.mixer.Sound('dino_google_game/songs/jump_sound.wav')
        self.death_sound = pygame.mixer.Sound('dino_google_game/songs/death_sound.wav')
        
        self.up = False
        self.stop = False
        self.xpos = 50
        self.ypos = (SCREEN_HEIGHT // 2) + 140
        root = 'dino_google_game/sprites/dino'
        self.dino_imgs = [f'{root}/dinossaur{i}.png' for i in range(3)]

        self.index = 0
        self.image = pygame.image.load(self.dino_imgs[self.index]).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.image = pygame.transform.scale(self.image, (84, 84))
        self.rect = self.image.get_rect()
        self.rect[0], self.rect[1] = self.xpos, self.ypos
        #self.rect.center = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
    
    def collision(self):
        #if pygame.sprite.spritecollide(dino, obstacle_group, False, pygame.sprite.collide_mask):
        global GAME_SPEED, FLOOR_SPEED
        if pygame.sprite.spritecollide(dino, obstacle_group, False, pygame.sprite.collide_mask):
            self.death_sound.play()
            GAME_SPEED = 0
            FLOOR_SPEED = 0
            self.stop = True
            
            #self.death_sound.set_volume(0)
    
    def jump(self):
        self.jump_sound.play()
        self.up = True
        #self.rect[1] = self.ypos - 10
        
    def update(self):
        #JUMP CONDITION
        if self.stop == False:
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
            self.mask = pygame.mask.from_surface(self.image)

        else:
            pass
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        root = 'dino_google_game/sprites/obstacle'
        self.obstacle_imgs = [f'{root}/obstacle0.png']

        self.image = pygame.image.load(self.obstacle_imgs[0]).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.image = pygame.transform.scale(self.image, (84, 84))
        self.rect = self.image.get_rect()
        self.rect[0], self.rect[1] = (SCREEN_WIDTH // 2) + 300, (SCREEN_HEIGHT // 2) + 162
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect[0] = SCREEN_WIDTH
        self.rect[0] -= GAME_SPEED

class Clouds(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        root_clouds = 'dino_google_game/sprites/background/clouds'
        self.cloud_imgs = [f'{root_clouds}/clouds0.png']

        self.image = pygame.image.load(self.cloud_imgs[0]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (148, 148))
        self.rect = self.image.get_rect()
        self.rect[0], self.rect[1] = (SCREEN_WIDTH // 2) + randrange(-400, 400, 100) , (SCREEN_HEIGHT // 2) - randrange(200, 400, 100)
    
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect[0] = SCREEN_WIDTH
            self.rect[1] = (SCREEN_HEIGHT // 2) - randrange(200, 400, 100)
        self.rect[0] -= GAME_SPEED

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        root_floor = 'dino_google_game/sprites/background/floor'
        self.floor_imgs = [f'{root_floor}/floor0.png']

        self.image = pygame.image.load(self.floor_imgs[0]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect[0], self.rect[1] = 0 , SCREEN_HEIGHT // 2  + 200
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect[0] = SCREEN_WIDTH
        self.rect[0] -= FLOOR_SPEED

dino = Dino()
dino_group = pygame.sprite.Group()
dino_group.add(dino)

obstacle = Obstacle()
obstacle_group = pygame.sprite.Group()
obstacle_group.add(obstacle)

numb_of_clouds = 5
clouds_group = pygame.sprite.Group()
for c in range(numb_of_clouds):
    clouds = Clouds()
    clouds_group.add(clouds)

floor_group = pygame.sprite.Group()
for c in range(-64, SCREEN_WIDTH, 60):
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
    dino.collision()

    obstacle_group.draw(screen)
    obstacle_group.update()

    clouds_group.draw(screen)
    clouds_group.update()

    floor_group.draw(screen)
    floor_group.update()

    text = font.render(f'{points}', True, BLACK)
    screen.blit(text, (700, 40))
    
    if GAME_SPEED != 0:
        points += 1
        if (points % 100) == 0:
            score_sound.play()
            GAME_SPEED += 2
        
    else:
        points += 0

    pygame.display.flip()

