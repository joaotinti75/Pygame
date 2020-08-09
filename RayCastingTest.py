import pygame
from pygame.locals import *
from sys import exit

WHITE = (255,255,255)

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
xpos = 0
ypos = 0
control = True


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def clockwise_mov_func():
    global xpos, ypos, control
    
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), (xpos, ypos))

    if xpos <= SCREEN_WIDTH and ypos <= SCREEN_HEIGHT and control == True:
        xpos += 1
        
    elif xpos >= SCREEN_WIDTH and ypos <= SCREEN_HEIGHT and control == True:
        ypos += 1
        
    elif ypos >= SCREEN_HEIGHT and control == True:
        if xpos <= 0:
            control = False
        else:
            xpos -= 1
            
    elif xpos == 0 and control == False:
        if ypos <= 0:
            control = True
            screen.fill((0,0,0))
        else:
            ypos -= 1
            
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    clockwise_mov_func()
    
    pygame.display.update()
