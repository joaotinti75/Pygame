import pygame
from pygame.locals import *
from sys import exit
from random import randint, choice

pygame.init()
#RECT'S COLOR
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
PINK = (255,0,255)
WHITE = (255,255,255)
GRAY = (125,125,125)

COLORS = [RED, GREEN, BLUE, YELLOW, CYAN, PINK, WHITE]
SHAPES = [0,1,2,3,4,5,6,7,8]

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 600
RECT_SIZE = 30
thickness = 7
size = 0 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')
grid = [i for i in range(2 * RECT_SIZE, SCREEN_WIDTH - 2 * RECT_SIZE, RECT_SIZE)]
x_pos = choice(grid)
y_pos = 0
color = choice(COLORS)
teste = 5
shape = teste
pos_list_final = []

def block_shape_func(shape):
    if shape == 0: #draws a horizontal 2 blocks line
        pygame.draw.rect(screen, color, (x_pos, y_pos, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos + RECT_SIZE, y_pos, RECT_SIZE, RECT_SIZE), thickness)
        
    elif shape == 1: #draws a vertical 2 blocks line
        pygame.draw.rect(screen, color, (x_pos, y_pos, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos, y_pos + RECT_SIZE, RECT_SIZE, RECT_SIZE), thickness)
        
    elif shape == 2: #draws a horizontal 3 blocks line
        pygame.draw.rect(screen, color, (x_pos, y_pos, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos - RECT_SIZE, y_pos, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos + RECT_SIZE, y_pos, RECT_SIZE, RECT_SIZE), thickness)
        
    elif shape == 3: #draws a vertical 3 blocks line
        pygame.draw.rect(screen, color, (x_pos, y_pos, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos, y_pos + RECT_SIZE, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos, y_pos - RECT_SIZE, RECT_SIZE, RECT_SIZE), thickness)
        
    elif shape == 4: #draws a 4 block square
        pygame.draw.rect(screen, color, (x_pos, y_pos, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos + RECT_SIZE, y_pos, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos, y_pos + RECT_SIZE, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos + RECT_SIZE, y_pos + RECT_SIZE, RECT_SIZE, RECT_SIZE), thickness)  
        
    elif shape == 5: #draws a 4 blocks L
        pygame.draw.rect(screen, color, (x_pos, y_pos, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos, y_pos + RECT_SIZE, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos, y_pos + 2 * RECT_SIZE, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos + RECT_SIZE, y_pos + 2 * RECT_SIZE, RECT_SIZE, RECT_SIZE), thickness)  
        
    elif shape == 6: #draws a 4 blocks inverted L
        pygame.draw.rect(screen, color, (x_pos, y_pos, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos, y_pos + RECT_SIZE, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos, y_pos + 2 * RECT_SIZE, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos - RECT_SIZE, y_pos + 2 * RECT_SIZE, RECT_SIZE, RECT_SIZE), thickness)   
        
    elif shape == 7: #draws a 4 blocks upward triangle
        pygame.draw.rect(screen, color, (x_pos, y_pos, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos, y_pos - RECT_SIZE, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos - RECT_SIZE, y_pos, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos + RECT_SIZE, y_pos, RECT_SIZE, RECT_SIZE), thickness)
        
    elif shape == 8: #draws a 4 blocks downward triangle
        pygame.draw.rect(screen, color, (x_pos, y_pos, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos, y_pos + RECT_SIZE, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos - RECT_SIZE, y_pos, RECT_SIZE, RECT_SIZE), thickness)
        pygame.draw.rect(screen, color, (x_pos + RECT_SIZE, y_pos, RECT_SIZE, RECT_SIZE), thickness)
        
def list_append_func(pos_list, shape_number, color, horizontal=False, size=0):
    #size 0 = left
    #size 1 = right
    if shape_number == 0: #appends a horizontal 2 blocks line in the list
        if horizontal == False:
            pos_list.append([x_pos, y_pos, color])
            pos_list.append([x_pos + RECT_SIZE, y_pos, color])
        else:
            if size == 0:
                y_min_dif = find_near_func(y_pos, pos_list)
                pos_list.append([x_pos, y_min_dif , color])
                pos_list.append([x_pos - RECT_SIZE, y_min_dif , color])
            else:
                y_min_dif = find_near_func(y_pos, pos_list)
                pos_list.append([x_pos + 2 * RECT_SIZE, y_min_dif , color])
                pos_list.append([x_pos + RECT_SIZE, y_min_dif , color])
            
    elif shape_number == 1: #appends a vertical 2 blocks line
        if horizontal == False:
            pos_list.append([x_pos, y_pos, color])
            pos_list.append([x_pos, y_pos + RECT_SIZE, color])
        else:
            if size == 0:
                y_min_dif = find_near_func(y_pos, pos_list)
                pos_list.append([x_pos - RECT_SIZE, y_min_dif, color])
                pos_list.append([x_pos - RECT_SIZE, y_min_dif + RECT_SIZE, color])
            else:
                y_min_dif = find_near_func(y_pos, pos_list)
                pos_list.append([x_pos + RECT_SIZE, y_min_dif, color])
                pos_list.append([x_pos + RECT_SIZE, y_min_dif + RECT_SIZE, color])
                
                
    elif shape_number == 2:
        if horizontal == False:
            pos_list.append([x_pos, y_pos, color])
            pos_list.append([x_pos - RECT_SIZE, y_pos, color])
            pos_list.append([x_pos + RECT_SIZE, y_pos, color])
        else:
            if size == 0:
                y_min_dif = find_near_func(y_pos, pos_list)
                pos_list.append([x_pos, y_min_dif, color])
                pos_list.append([x_pos - RECT_SIZE, y_min_dif, color])
                pos_list.append([x_pos - 2 * RECT_SIZE, y_min_dif, color])
            else:
                y_min_dif = find_near_func(y_pos, pos_list)
                pos_list.append([x_pos, y_min_dif, color])
                pos_list.append([x_pos + RECT_SIZE, y_min_dif, color])
                pos_list.append([x_pos + 2 * RECT_SIZE, y_min_dif, color])

    elif shape_number == 3:
        if horizontal == False:
            pos_list.append([x_pos, y_pos, color])
            pos_list.append([x_pos, y_pos + RECT_SIZE, color])
            pos_list.append([x_pos, y_pos - RECT_SIZE, color])
        else:
            if size == 0:
                y_min_dif = find_near_func(y_pos, pos_list)
                pos_list.append([x_pos - RECT_SIZE, y_min_dif, color])
                pos_list.append([x_pos - RECT_SIZE, y_min_dif + RECT_SIZE, color])
                pos_list.append([x_pos - RECT_SIZE, y_min_dif + 2 * RECT_SIZE, color])
            else:
                y_min_dif = find_near_func(y_pos, pos_list)
                pos_list.append([x_pos + RECT_SIZE, y_min_dif, color])
                pos_list.append([x_pos + RECT_SIZE, y_min_dif + RECT_SIZE, color])
                pos_list.append([x_pos + RECT_SIZE, y_min_dif + 2 * RECT_SIZE, color])
        
    elif shape_number == 4:
        if horizontal == False:
            pos_list.append([x_pos, y_pos, color])
            pos_list.append([x_pos + RECT_SIZE, y_pos, color])
            pos_list.append([x_pos, y_pos + RECT_SIZE, color])
            pos_list.append([x_pos + RECT_SIZE, y_pos + RECT_SIZE, color])
        else:
            if size == 0:
                y_min_dif = find_near_func(y_pos, pos_list)
                pos_list.append([x_pos, y_min_dif, color])
                pos_list.append([x_pos - RECT_SIZE, y_min_dif, color])
                pos_list.append([x_pos, y_min_dif + RECT_SIZE, color])
                pos_list.append([x_pos - RECT_SIZE, y_min_dif + RECT_SIZE, color])
            else:
                y_min_dif = find_near_func(y_pos, pos_list)
                pos_list.append([x_pos + RECT_SIZE, y_min_dif, color])
                pos_list.append([x_pos + 2 * RECT_SIZE, y_min_dif, color])
                pos_list.append([x_pos + RECT_SIZE, y_min_dif + RECT_SIZE, color])
                pos_list.append([x_pos + 2 * RECT_SIZE, y_min_dif + RECT_SIZE, color])
                

    elif shape_number == 5:
        if horizontal == False:
            pos_list.append([x_pos, y_pos, color])
            pos_list.append([x_pos, y_pos + RECT_SIZE, color])
            pos_list.append([x_pos, y_pos + 2 * RECT_SIZE, color])
            pos_list.append([x_pos + RECT_SIZE, y_pos + 2 * RECT_SIZE, color])
        else:
            if size == 0:
                y_min_dif = find_near_func(y_pos, pos_list)
                pos_list.append([x_pos - RECT_SIZE, y_min_dif, color])
                pos_list.append([x_pos - RECT_SIZE, y_min_dif + RECT_SIZE, color])
                pos_list.append([x_pos - RECT_SIZE, y_min_dif + 2 * RECT_SIZE, color])
                pos_list.append([x_pos, y_min_dif + 2 * RECT_SIZE, color])
            else:
                y_min_dif = find_near_func(y_pos, pos_list)
                pos_list.append([x_pos + RECT_SIZE, y_min_dif, color])
                pos_list.append([x_pos + RECT_SIZE, y_min_dif + RECT_SIZE, color])
                pos_list.append([x_pos + RECT_SIZE, y_min_dif + 2 * RECT_SIZE, color])
                pos_list.append([x_pos + 2 * RECT_SIZE, y_min_dif + 2 * RECT_SIZE, color])
            

    elif shape_number == 6:
        pos_list.append([x_pos, y_pos, color])
        pos_list.append([x_pos, y_pos + RECT_SIZE, color])
        pos_list.append([x_pos, y_pos + 2 * RECT_SIZE, color])
        pos_list.append([x_pos - RECT_SIZE, y_pos + 2 * RECT_SIZE, color])
        
    elif shape_number == 7:
        pos_list.append([x_pos, y_pos, RED])
        pos_list.append([x_pos, y_pos - RECT_SIZE, color])
        pos_list.append([x_pos - RECT_SIZE, y_pos, color])
        pos_list.append([x_pos + RECT_SIZE, y_pos, color])
        
    elif shape_number == 8:
        pos_list.append([x_pos, y_pos, color])
        pos_list.append([x_pos, y_pos + RECT_SIZE, color])
        pos_list.append([x_pos - RECT_SIZE, y_pos, color])
        pos_list.append([x_pos + RECT_SIZE, y_pos, color])
        
def find_near_func(y_pos, pos_list):
    first_list = []
    second_list = []
    negative_list = []
    for num, element in enumerate(pos_list):
        first_list.append(y_pos - element[1])
    for element in first_list:
        if element > 0:
            second_list.append(element)
        else:
            negative_list.append(element)
    if second_list == []:
        negative_list = [abs(element) for element in negative_list]
        return y_pos + min(negative_list)
    else:
        return y_pos - min(second_list)

def draw_func(pos_list):
    for num, element in enumerate(pos_list): 
        pygame.draw.rect(screen, element[2], (element[0], element[1], RECT_SIZE, RECT_SIZE), thickness)
    
clock = pygame.time.Clock()
#======================MAIN LOOP=====================================#
while True:
    clock.tick(30)
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                if x_pos == RECT_SIZE and shape in [0,1,3,4,5]:
                    size = 1
                    #pass #x_pos = RECT_SIZE
                elif x_pos - RECT_SIZE == RECT_SIZE  and shape not in [0,1,3,4,5]:
                    size = 1
                    #pass #x_pos = x_pos
                else:
                    size = 1
                    x_pos -= RECT_SIZE
                
            if event.key == K_RIGHT or event.key == K_d:
                if x_pos + RECT_SIZE == SCREEN_WIDTH - RECT_SIZE and shape in [1,3,6]:
                    size = 0
                    #pass
                elif x_pos + 2 * RECT_SIZE == SCREEN_WIDTH - RECT_SIZE and shape not in [1,3,6]:
                    size = 0
                    #pass
                else:
                    size = 0
                    x_pos += RECT_SIZE
                
    block_shape_func(teste)
    #pygame.draw.rect(screen, color, (x_pos, y_pos, RECT_SIZE, RECT_SIZE), 7)
    
    if shape == 0:
        if y_pos + RECT_SIZE >= SCREEN_HEIGHT:  #Passando a tela
            list_append_func(pos_list_final, shape, color)
            x_pos = choice(grid)
            y_pos = 0
            color = choice(COLORS)
            shape = teste
        else:   #Encostando em um bloco abaixo do mesmo
            for num, element in enumerate(pos_list_final):
                if x_pos == element[0] and y_pos + RECT_SIZE == element[1]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                elif x_pos + RECT_SIZE == element[0] and y_pos + RECT_SIZE == element[1]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                # Encostando em um bloco ao lado pela direita
                elif x_pos + RECT_SIZE == element[0] and element[1] - RECT_SIZE < y_pos < element[1] + RECT_SIZE and size in [0,1]:
                    list_append_func(pos_list_final, shape, color, True, size=0)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                # Encostando em um bloco ao lado pela esquerda
                elif x_pos == element[0] and element[1] - RECT_SIZE < y_pos < element[1] + RECT_SIZE and size in [0,1]:  
                    list_append_func(pos_list_final, shape, color, True, size=1)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break

    elif shape == 1:    
        if y_pos + 2 * RECT_SIZE >= SCREEN_HEIGHT:  #Passando a tela
            list_append_func(pos_list_final, shape, color)
            x_pos = choice(grid)
            y_pos = 0
            color = choice(COLORS)
            shape = teste
        else:   #Encostando em um bloco
            for num, element in enumerate(pos_list_final):
                if x_pos == element[0] and y_pos + 2 * RECT_SIZE == element[1]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                # Encostando em um bloco pelo lado pela direita ou pela esquerda
                elif x_pos == element[0] and element[1] - 2 * RECT_SIZE< y_pos < element[1] + RECT_SIZE and size in [0,1]:  
                    list_append_func(pos_list_final, shape, color, True, size)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break 
    elif shape == 2:    
        if y_pos + RECT_SIZE >= SCREEN_HEIGHT:  #Passando a tela
            list_append_func(pos_list_final, shape, color)
            x_pos = choice(grid)
            y_pos = 0
            color = choice(COLORS)
            shape = teste
        else:   #Encostando em um bloco
            for num, element in enumerate(pos_list_final):
                if x_pos == element[0] and y_pos + RECT_SIZE == element[1]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                elif x_pos + RECT_SIZE == element[0] and y_pos + RECT_SIZE == element[1]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                elif x_pos - RECT_SIZE == element[0] and y_pos + RECT_SIZE == element[1]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                # Da esquerda para a direita
                elif x_pos + RECT_SIZE == element[0] and element[1] - RECT_SIZE < y_pos < element[1] + RECT_SIZE and size in [0,1]:
                    list_append_func(pos_list_final, shape, color, True, size=0)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                # Da direita para a esquerda
                elif x_pos - RECT_SIZE == element[0] and element[1] - RECT_SIZE < y_pos < element[1] + RECT_SIZE and size in [0,1]:  
                    list_append_func(pos_list_final, shape, color, True, size=1)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
    
    elif shape == 3:    
        if y_pos + 2 * RECT_SIZE >= SCREEN_HEIGHT:  #Passando a tela
            list_append_func(pos_list_final, shape, color)
            x_pos = choice(grid)
            y_pos = 0
            color = choice(COLORS)
            shape = teste
        else:   #Encostando em um bloco por cima
            for num, element in enumerate(pos_list_final):
                if x_pos == element[0] and y_pos + 2 * RECT_SIZE == element[1]:#and size not in [0,1]
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                # Encostando em um bloco pelo lado pela direita ou pela esquerda
                elif x_pos == element[0] and element[1] - 3 * RECT_SIZE< y_pos < element[1] + 2 * RECT_SIZE and size in [0,1]:   
                    list_append_func(pos_list_final, shape, color, True, size)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break 
                    
    elif shape == 4:    
        if y_pos + 2 * RECT_SIZE >= SCREEN_HEIGHT:  #Passando a tela
            list_append_func(pos_list_final, shape, color)
            x_pos = choice(grid)
            y_pos = 0
            color = choice(COLORS)
            shape = teste
        else:   #Encostando em um bloco
            for num, element in enumerate(pos_list_final):
                if x_pos == element[0] and y_pos + 2 * RECT_SIZE == element[1] and size not in [0,1]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                elif x_pos + RECT_SIZE == element[0] and y_pos + 2 * RECT_SIZE == element[1] and size not in [0,1]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                # Encostando em um bloco ao lado pela direita
                elif x_pos + RECT_SIZE == element[0] and element[1] - 2 * RECT_SIZE < y_pos < element[1] + RECT_SIZE and size in [0,1]:
                    print('esquerda---direita')
                    list_append_func(pos_list_final, shape, color, True, size=0)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                # Encostando em um bloco ao lado pela esquerda
                elif x_pos == element[0] and element[1] - 2 * RECT_SIZE < y_pos < element[1] + RECT_SIZE and size in [0,1]: 
                    print('direita---esquerda')
                    list_append_func(pos_list_final, shape, color, True, size=1)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break

    elif shape == 5:    
        if y_pos + 3 * RECT_SIZE >= SCREEN_HEIGHT:  #Passando a tela
            list_append_func(pos_list_final, shape, color)
            x_pos = choice(grid)
            y_pos = 0
            color = choice(COLORS)
            shape = teste
        else:   #Encostando em um bloco
            for num, element in enumerate(pos_list_final):
                if x_pos == element[0] and y_pos + 3 * RECT_SIZE == element[1] and size not in [0,1]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                elif x_pos + RECT_SIZE == element[0] and y_pos + 3 * RECT_SIZE == element[1] and size not in [0,1]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                #Da esquerda para direita
                elif x_pos + RECT_SIZE == element[0] and element[1] - RECT_SIZE < y_pos < element[1] + RECT_SIZE and size in [0,1]:  
                    list_append_func(pos_list_final, shape, color, True, size=0)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                #Da direita para a esquerda
                elif x_pos == element[0] and element[1] - 3 * RECT_SIZE < y_pos < element[1] + RECT_SIZE and size in [0,1]:  
                    list_append_func(pos_list_final, shape, color, True, size=1)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                    
    elif shape == 6:    
        if y_pos + 3 * RECT_SIZE >= SCREEN_HEIGHT:  #Passando a tela
            list_append_func(pos_list_final, shape, color)
            x_pos = choice(grid)
            y_pos = 0
            color = choice(COLORS)
            shape = teste
        else:   #Encostando em um bloco
            for num, element in enumerate(pos_list_final):
                if y_pos + 3 * RECT_SIZE == element[1] and x_pos == element[0]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                elif y_pos + 3 * RECT_SIZE == element[1] and x_pos - RECT_SIZE == element[0]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                    
    elif shape == 7:    
        if y_pos + RECT_SIZE >= SCREEN_HEIGHT:  #Passando a tela
            list_append_func(pos_list_final, shape, color)
            x_pos = choice(grid)
            y_pos = 0
            color = choice(COLORS)
            shape = teste
        else:   #Encostando em um bloco
            for num, element in enumerate(pos_list_final):
                if y_pos + RECT_SIZE == element[1] and x_pos == element[0]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                elif y_pos + RECT_SIZE == element[1] and x_pos + RECT_SIZE == element[0]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                elif y_pos + RECT_SIZE == element[1] and x_pos - RECT_SIZE == element[0]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                    
    elif shape == 8:    
        if y_pos + 2 * RECT_SIZE >= SCREEN_HEIGHT:  #touching the screen bottom
            list_append_func(pos_list_final, shape, color)
            x_pos = choice(grid)
            y_pos = 0
            color = choice(COLORS)
            shape = teste
        else:   #touching a block
            for num, element in enumerate(pos_list_final):
                if y_pos + 2 * RECT_SIZE == element[1] and x_pos == element[0]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                elif y_pos + RECT_SIZE == element[1] and x_pos + RECT_SIZE == element[0]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                elif y_pos + RECT_SIZE == element[1] and x_pos - RECT_SIZE == element[0]:
                    list_append_func(pos_list_final, shape, color)
                    x_pos = choice(grid)
                    y_pos = 0
                    color = choice(COLORS)
                    shape = teste
                    break
                
    y_pos += 5
    
    draw_func(pos_list_final)
    # drawing borders
    pygame.draw.rect(screen, GRAY, (0, 0, RECT_SIZE, SCREEN_HEIGHT)) #left border
    pygame.draw.rect(screen, GRAY, (SCREEN_WIDTH - RECT_SIZE, 0, RECT_SIZE, SCREEN_HEIGHT)) #right border
    size = 2
    pygame.display.update()
