import pygame
from pygame.locals import *
from sys import exit
from random import choice, randrange

pygame.init()

SCREEN_WIDTH = 540
SCREEN_HEIGHT = 480
FONT_SIZE = 8
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
COLORS = [GREEN, RED, BLUE]
color_change = 0

FPS = 12
generate = False

letter = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','z','x','y','z']

initial_time = 0
current_time = 0
color_time = 0
counter = 20

fonte = pygame.font.SysFont('arial', FONT_SIZE, True, True)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
pygame.display.set_caption('Matrix')

class Codeline:
    def __init__(self):
        self.color = GREEN
        self.fill = 1
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
            text = fonte.render(message, True, self.color)
            #screen.fill(BLACK, (self.xpos, y, text.get_width() + FONT_SIZE, text.get_height()))
            screen.blit(text, (self.xpos, y))

    def desloc_codeline(self): #method that moves the letters on screen
        if self.ypos > SCREEN_HEIGHT or len(self.lista_ypos) > 20:
            message = ' '
            text = fonte.render(message, True, WHITE)
            screen.fill(BLACK, (self.xpos, self.lista_ypos[0], text.get_width() + FONT_SIZE, text.get_height()*self.fill))
            if text.get_height() * self.fill > len(self.lista_ypos) * text.get_height():
                self.lista_letters.clear()
            else:
                self.fill += 1

        else:
            self.ypos += FONT_SIZE 
            self.lista_ypos.append(self.ypos)
            message = f'{self.lista_letters[-1]}'
            text = fonte.render(message, True, WHITE)
            screen.fill(BLACK, (self.xpos, self.lista_ypos[-1], text.get_width() + FONT_SIZE, text.get_height()))
            screen.blit(text, (self.xpos, self.lista_ypos[-1]))

obj_list = []
repeat_list = []

def insert_obj(obj_list, generate, counter, color_change):
    if generate: #if generate is True, the for loop will continuously create new objects
        for i in range(counter): #creating objects and saving them in a list
            obj = Codeline()
            if obj.xpos in repeat_list or obj.ypos > SCREEN_HEIGHT:
                repeat_list.remove(obj.xpos)
                obj.lista_letters.clear()
                del obj
                #pass
            else:
                repeat_list.append(obj.xpos)
                obj_list.append(obj)
            
        for i in obj_list: #drawing the objects and moving them on the screen
            i.color = COLORS[color_change]
            i.draw_codeline()
            i.desloc_codeline()
            
    else: #if generate is False new objects won't be created anymore
        for i in obj_list:
            i.color = COLORS[color_change]
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
    
    current_time = pygame.time.get_ticks()

    insert_obj(obj_list, generate, counter, color_change)

    if current_time - color_time > 3000:
        color_change = (color_change + 1) % len(COLORS)
        color_time = pygame.time.get_ticks()

    if current_time - initial_time > 200:
        generate = True
        initial_time = pygame.time.get_ticks()

    pygame.display.flip()
