import pygame
from pygame.locals import *
from sys import exit
from random import choice, randrange

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FONT_SIZE = 20
WHITE = (255,255,255)
GREEN = (0, 160, 0)
BLACK = (0, 0, 0)
FPS = 15
generate = False

letter = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','z','x','y','z']

initial_time = 0
current_time = 0
counter = 1

fonte = pygame.font.SysFont('arial', FONT_SIZE, False, True)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
pygame.display.set_caption('Matrix')

class Codeline:
    def __init__(self):
        self.lista_ypos = []
        self.lista_letters = []
        self.xpos = randrange(FONT_SIZE, SCREEN_WIDTH + FONT_SIZE, FONT_SIZE) 
        self.ypos = randrange(0, SCREEN_HEIGHT+FONT_SIZE, FONT_SIZE)
        self.lista_ypos.append(self.ypos)
        
    def draw_codeline(self): #method that draws letters on sreen
        randomic_letter = choice(letter)
        self.lista_letters.append(randomic_letter)

        for msg, y in zip(self.lista_letters, self.lista_ypos):
            message = f'{msg}'
            text = fonte.render(message, True, GREEN)
            screen.blit(text, (self.xpos, y))

    def desloc_codeline(self): #method that moves the letters on screen
        self.ypos += FONT_SIZE - 6 
        self.lista_ypos.append(self.ypos)
        message = f'{self.lista_letters[-1]}'
        text = fonte.render(message, True, WHITE)
        screen.blit(text, (self.xpos, self.lista_ypos[-1]))

obj_list = []
repeat_list = []

def insert_obj(obj_list, generate, counter):
    if generate: #if generate is True, the for loop will continuously create new objects
        for i in range(counter): #creating objects and saving them in a list
            obj = Codeline()
            if obj.xpos in repeat_list or obj.ypos > SCREEN_HEIGHT:
                del obj
            else:
                repeat_list.append(obj.xpos)
                obj_list.append(obj)
            
        for i in obj_list: #drawing the objects and moving them on the screen
            i.draw_codeline()
            i.desloc_codeline()
    else: #if generate is False new objects won't be created anymore
        for i in obj_list:
            i.draw_codeline()   
            i.desloc_codeline()

clock = pygame.time.Clock()

while True:
    screen.fill((0,0,0))
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    for c in range(counter): 
        if current_time - initial_time > 1000:
            generate = True
            initial_time = pygame.time.get_ticks()
            counter += 1
    '''    
    if counter < 20:    
        if current_time - initial_time > 1000:
            generate = True
            initial_time = pygame.time.get_ticks()
            counter += 1
    else:
        generate = False
    '''
    current_time = pygame.time.get_ticks()

    insert_obj(obj_list, generate, counter)

    pygame.display.flip()
