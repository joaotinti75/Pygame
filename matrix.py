import pygame
from pygame.locals import *
from sys import exit
from random import choice, randint

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FONT_SIZE = 10
generate = False

letter = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','z','x','y','z']

initial_time = 0
current_time = 0
counter = 1

fonte = pygame.font.SysFont('arial', FONT_SIZE, False, True)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    

class Codeline:
    def __init__(self):
        self.lista_ypos = []
        self.lista_letters = []
        self.xpos = randint(FONT_SIZE, SCREEN_WIDTH-FONT_SIZE) 
        self.ypos = randint(0, SCREEN_HEIGHT-FONT_SIZE)
        self.lista_ypos.append(self.ypos)

    def draw_codeline(self):
        randomic_letter = choice(letter)
        self.lista_letters.append(randomic_letter)

        for msg, y in zip(self.lista_letters, self.lista_ypos):
            message = f'{msg}'
            text = fonte.render(message, True, (0,160,0))
            screen.blit(text, (self.xpos, y))

    def desloc_codeline(self):
        self.ypos += FONT_SIZE - 6
        self.lista_ypos.append(self.ypos)

obj_list = []
'''
for i in range(200):
    obj = Codeline()
    obj_list.append(obj)'''

def insert_obj(obj_list, generate):
    if generate:
        for i in range(1):
            obj = Codeline()
            obj_list.append(obj)
        for i in obj_list:
            i.draw_codeline()
            i.desloc_codeline()
    else:
        for i in obj_list:
            i.draw_codeline()
            i.desloc_codeline()

clock = pygame.time.Clock()

while True:
    screen.fill((0,0,0))
    clock.tick(18)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    if counter < 10:    
        if current_time - initial_time > 1000:
            generate = True
            initial_time = pygame.time.get_ticks()
            counter += 1
    else:
        generate = False

    current_time = pygame.time.get_ticks()


    insert_obj(obj_list, generate)

    '''for i in obj_list:
        i.draw_codeline()
        i.desloc_codeline()'''

    pygame.display.flip()
