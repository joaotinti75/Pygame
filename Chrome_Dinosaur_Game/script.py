import pygame
from sys import exit
from random import randrange, choice
import os

'''
x = 800 #500
y = 700 #400

os.environ['SDL_VIDEO_WINDOW_POS'] = f'{(x, y)}'
'''
os.environ['SDL_VIDEO_CENTERED'] = '0'

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

pygame.init()

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 680

WHITE = (255,255,255)
BLACK = (0,0,0)

FPS = 30
GAME_SPEED = 10
FLOOR_SPEED = 10
GAME_OVER = False

points = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

song = 0

font = pygame.font.SysFont('comicsansms', 40, True, True)
score_sound = pygame.mixer.Sound(os.path.join(THIS_FOLDER,'score_sound.wav'))
score_sound.set_volume(0.2)

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.jump_sound = pygame.mixer.Sound(os.path.join(THIS_FOLDER,'jump_sound.wav'))
        self.death_sound = pygame.mixer.Sound(os.path.join(THIS_FOLDER, 'death_sound.wav'))
        
        self.up = False
        self.stop = False
        self.xpos = 50
        self.ypos = (SCREEN_HEIGHT // 2) + 140
        self.dino_imgs = [os.path.join(THIS_FOLDER,f'dinossaur{i}.png') for i in range(3)]

        self.index = 0
        self.image = pygame.image.load(self.dino_imgs[self.index]).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.image = pygame.transform.scale(self.image, (84, 84))
        self.rect = self.image.get_rect()
        self.rect[0], self.rect[1] = self.xpos, self.ypos
    
    def collision(self):
        global GAME_SPEED, FLOOR_SPEED
        if pygame.sprite.spritecollide(dino, obstacle_group, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(dino, flying_dino_group, False, pygame.sprite.collide_mask):
            GAME_SPEED = 0
            FLOOR_SPEED = 0
            self.stop = True
            flying_dino.stop = True
            
    def jump(self):
        self.jump_sound.play()
        self.up = True
        
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

class Flying_dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()        
        self.flying_dino_imgs = [os.path.join(THIS_FOLDER, f'fly_dino{i}.png') for i in range(2)]
        self.stop = False
        self.index = 0
        self.image = pygame.image.load(self.flying_dino_imgs[self.index]).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        
        self.image = pygame.transform.scale(self.image, (84, 84))
        self.rect = self.image.get_rect()
        self.rect[0], self.rect[1] = SCREEN_WIDTH, (SCREEN_HEIGHT // 2) 

    def update(self):
        #SPRITES
        if self.stop == False:
            if self.index >= len(self.flying_dino_imgs) - 1:
                self.index = 0

            self.index += 0.25
            self.image = pygame.image.load(self.flying_dino_imgs[int(self.index)]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (128, 128))
            self.mask = pygame.mask.from_surface(self.image)
        else:
            pass

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.obstacle_imgs = [os.path.join(THIS_FOLDER,'obstacle0.png')]

        self.image = pygame.image.load(self.obstacle_imgs[0]).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.image = pygame.transform.scale(self.image, (84, 84))
        self.rect = self.image.get_rect()
        self.rect[0], self.rect[1] = SCREEN_WIDTH, (SCREEN_HEIGHT // 2) + 162
        self.mask = pygame.mask.from_surface(self.image)

class Clouds(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.cloud_imgs = [os.path.join(THIS_FOLDER,'clouds0.png')]

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
        self.floor_imgs = [os.path.join(THIS_FOLDER,'floor0.png')]

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

flying_dino = Flying_dino()
flying_dino_group = pygame.sprite.Group()
flying_dino_group.add(flying_dino)

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

obstacle_choice = choice([obstacle, flying_dino])

while True:
    clock.tick(FPS)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                exit()

            if event.key == pygame.K_SPACE:
                if dino.rect[1] < dino.ypos:
                    pass
                else:
                    dino.jump()
        
            if event.key == pygame.K_r and GAME_OVER == True:
                GAME_SPEED = 10
                FLOOR_SPEED = 10
                points = 0
                song = 0
                obstacle.rect[0] = SCREEN_WIDTH
                flying_dino.rect[0] = SCREEN_WIDTH
                dino.stop = False
                dino.rect[1] = dino.ypos
                flying_dino.stop = False

    dino_group.draw(screen)
    dino_group.update()
    dino.collision()

    flying_dino_group.draw(screen)
    flying_dino_group.update()

    obstacle_group.draw(screen)
    obstacle_group.update()

    clouds_group.draw(screen)
    clouds_group.update()

    floor_group.draw(screen)
    floor_group.update()

    text = font.render(f'{points}', True, BLACK)
    screen.blit(text, (700, 40))

    if obstacle_choice.rect.topright[0] < 0:
        flying_dino.rect[0] = SCREEN_WIDTH
        obstacle.rect[0] = SCREEN_WIDTH
        obstacle_choice = choice([obstacle, flying_dino])
    else:
        obstacle_choice.rect[0] -= GAME_SPEED

    if GAME_SPEED != 0:
        points += 1
        if (points % 100) == 0:
            score_sound.play()
            if GAME_SPEED == 46:
                pass
            else:
                GAME_SPEED += 2
        
    else:
        points += 0
        if song > 1:
            song = 2
        else:
            song += 1
        dino.jump_sound.stop()
        txt = ['GAME OVER', 'Press R to play again']
        line1 = font.render(txt[0], True, BLACK)
        line2 = font.render(txt[1], True, BLACK)
        screen.blit(line1, ((SCREEN_WIDTH // 2) - (line1.get_width()//2), (SCREEN_HEIGHT // 2) - 100))
        screen.blit(line2, ((SCREEN_WIDTH // 2) - (line2.get_width()//2), (SCREEN_HEIGHT // 2) - 50))
        GAME_OVER = True

    if song == 1:
        dino.death_sound.play()
        
    pygame.display.flip()

