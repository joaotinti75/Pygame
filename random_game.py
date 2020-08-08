import pygame
from pygame.locals import *
from sys import exit

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_SPEED = 10
state = 0
current_pos_list = []
direction = 'none'
x1 = 0
x2 = SCREEN_WIDTH
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Animation')

background_image_filename = pygame.image.load('Assets/background_asset_boy.png').convert()
background = pygame.transform.scale(background_image_filename, (SCREEN_WIDTH, SCREEN_HEIGHT))

background2 = pygame.transform.scale(background_image_filename, (SCREEN_WIDTH, SCREEN_HEIGHT))
background2 = pygame.transform.flip(background_image_filename, True, False)


class Boy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images_state0 = [pygame.image.load(f'Assets/Idle ({i}).png').convert_alpha() for i in range(1,16)]  
        self.images_state0 = [pygame.transform.scale(element, (307, 282)) for element in self.images_state0]
        
        self.images_state1 = [pygame.image.load(f'Assets/Run ({i}).png').convert_alpha() for i in range(1,16)]  
        self.images_state1 = [pygame.transform.scale(element, (307, 282)) for element in self.images_state1]
        
        self.images_state2 = [pygame.image.load(f'Assets/Jump ({i}).png').convert_alpha() for i in range(1,16)]  
        self.images_state2 = [pygame.transform.scale(element, (307, 282)) for element in self.images_state2]
        
        self.images_state3 = [pygame.image.load(f'Assets/Run ({i}).png').convert_alpha() for i in range(1,16)]  
        self.images_state3 = [pygame.transform.scale(element, (307, 282)) for element in self.images_state3]
        self.images_state3 = [pygame.transform.flip(element, True, False) for element in self.images_state3]
        
        self.images_state4 = [pygame.image.load(f'Assets/Jump ({i}).png').convert_alpha() for i in range(1,16)]  
        self.images_state4 = [pygame.transform.scale(element, (307, 282)) for element in self.images_state4]
        self.images_state4 = [pygame.transform.flip(element, True, False) for element in self.images_state4]
        
        
        self.current_image = 0
        self.image = pygame.image.load('Assets/Idle (1).png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 2 - 40
        self.rect[1] = SCREEN_HEIGHT / 2 - 20
        
    def update(self, state=0):
        self.current_image = (self.current_image + 1) % 15
        if state == 0: 
            self.image = self.images_state0[self.current_image]
        elif state == 1:
            self.image = self.images_state1[self.current_image]
        elif state == 2:
            self.image = self.images_state2[self.current_image]
        elif state == 3:
            self.image = self.images_state3[self.current_image]
        elif state == 4:
            self.image = self.images_state4[self.current_image]
        
boy_group = pygame.sprite.Group()
boy = Boy()
boy_group.add(boy)

clock = pygame.time.Clock()
while True:
    clock.tick(20)
    screen.blit(background, (x1, 0))
    screen.blit(background2, (x2, 0))
    #screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    if pygame.key.get_pressed()[pygame.K_RIGHT]: #run right
        state = 1
        direction = 'right'
        boy.rect[0] = SCREEN_WIDTH / 2 - 40 #original position
    elif pygame.key.get_pressed()[pygame.K_LEFT]: #run left
        state = 3
        direction = 'left'
        boy.rect[0] = SCREEN_WIDTH / 2 - 40 - boy.rect[1]/2 #adjusted position
    elif pygame.key.get_pressed()[pygame.K_SPACE]: #jump right
        state = 2
        boy.rect[1] = 160
    else:
        state = 0
        direction = 'none'
        boy.rect[0] = SCREEN_WIDTH / 2 - 40
    
    boy_group.update(state)
    if direction == 'right':
        if x1 < -background.get_rect().width:
            x1 = x1 + 2 * background.get_rect().width
        if x2 < -background.get_rect().width:
            x2 = x2 + 2 * background2.get_rect().width 
        x1 -= GAME_SPEED
        x2 -= GAME_SPEED
    elif direction == 'left':
        if x1 > background.get_rect().width:
            x1 = x1 - 2 * background.get_rect().width
        if x2 > background.get_rect().width:
            x2 = x2 - 2 * background.get_rect().width
        x1 += GAME_SPEED
        x2 += GAME_SPEED
    elif direction == 'none':
        pass

    boy_group.draw(screen)
    pygame.display.update()
    
