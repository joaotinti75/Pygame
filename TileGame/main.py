import pygame
from sys import exit
from pygame.locals import *
from setup import *

pygame.init()


tela = pygame.display.set_mode((WIDTH, HEIGHT))

def load_crop_image(img, x, y, w, h, transform=True):
    img_original = img.subsurface((x,y),(w,h))
    if transform:
        img_scaled = pygame.transform.scale(img_original, (LARGURA_BLOCO, ALTURA_BLOCO))
        return img_scaled
    else:
        return img_original


tiles = pygame.image.load('./img/Overworld.png').convert_alpha()
personagem = pygame.image.load('./img/character.png').convert_alpha()


img_grama = load_crop_image(tiles, 0, 48, 16, 16)
img_parede = load_crop_image(tiles, 22*16, 48, 16, 16)
img_casa = load_crop_image(tiles, 6*16, 0, 5*16, 5*16, False)
img_casa = pygame.transform.scale(img_casa, (5*15*2, 5*16*2))

def desenha_mapa(mapa, caracter_imagem):
    for linha_index, linha in enumerate(mapa):
        for coluna_index, caracter in enumerate(linha):
            if caracter in caracter_imagem:
                x = coluna_index * LARGURA_BLOCO
                y = linha_index * ALTURA_BLOCO
                img = caracter_imagem[caracter]
                tela.blit(img, (x,y))

def teste_colisao_mapa(personagem, mapa, lista_caracteres):
    colisoes = []
    for linha_index, linha in enumerate(mapa):
        for coluna_index, caracter in enumerate(linha):
            if caracter in lista_caracteres:
                x = coluna_index * LARGURA_BLOCO
                y = linha_index * ALTURA_BLOCO
                r = pygame.Rect((x,y), (LARGURA_BLOCO, ALTURA_BLOCO))
                r2 = personagem.rect.copy()
                r2.move_ip(personagem.vel_x, personagem.vel_y)
                if r.colliderect(r2):
                    colisao = {'linha':linha_index, 'coluna':coluna_index, 'caracter':caracter}
                    colisoes.append(colisao)
    return colisoes

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.vel_x = 0
        self.vel_y = 0
        self.images_down = []
        self.images_up = []
        self.images_left = []
        self.images_right = []

        for c in range(0, 64, 16):
            left = load_crop_image(personagem, c, 96, 16, 32, False)
            left = pygame.transform.scale(left, (48,96))
            self.images_left.append(left)
            
            up = load_crop_image(personagem, c, 64, 16, 32, False)
            up = pygame.transform.scale(up, (48,96))
            self.images_up.append(up)
            
            right = load_crop_image(personagem, c, 32, 16, 32, False)
            right = pygame.transform.scale(right, (48,96))
            self.images_right.append(right)
            
            down = load_crop_image(personagem, c, 0, 16, 32, False)
            down = pygame.transform.scale(down, (48,96))
            self.images_down.append(down)
    
        self.i = 0
        self.image = self.images_down[self.i]
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
    
    
    def update(self):   
        self.i += 0.20
        if self.i >= len(self.images_down):
            self.i = 0
        self.image = self.images_down[int(self.i)]
        
        colisoes_movimento = teste_colisao_mapa(self, mapa, ['p']) 

        if len(colisoes_movimento) == 0: #se n houve colisao
            self.rect.move_ip(self.vel_x, self.vel_y)

        colisoes = teste_colisao_mapa(self, mapa_casa, ['c'])
        for colisao in colisoes:
            linha = colisao['linha']
            mapa_casa[linha] = '' #faz a casa sumir quando ocorre a colisao
            #self.kill() para matar a sprite(a remove de todos os grupos)
            print(mapa_casa)
            print(f'Linha: {colisao["linha"]}, Coluna: {colisao["coluna"]}, Caracter: {colisao["caracter"]}')

    
        
        #Para explicar melhor como funciona a colisão, eu desenhei
        #pygame.draw.rect(tela, (255,0,0), (r2))
        #pygame.draw.rect(tela, (0,0,255), self.rect)

    def processar_evento(self, event):
        if event.type == KEYDOWN:
            if event.key == K_d:
                self.vel_x = VELOCIDADE
                self.vel_y = 0
            if event.key == K_a:
                self.vel_x = -VELOCIDADE
                self.vel_y = 0
            if event.key == K_w:
                self.vel_y = -VELOCIDADE
                self.vel_x = 0
            if event.key == K_s:
                self.vel_y = VELOCIDADE
                self.vel_x = 0
        if event.type == KEYUP:
            if event.key in [pygame.K_a, pygame.K_d]:
                self.vel_x = 0
            if event.key in [pygame.K_w, pygame.K_s]:
                self.vel_y = 0



heroi = Personagem()
grupo_heroi = pygame.sprite.Group(heroi)


mapa = [
    'pppppppppppppppppppp',
    'p                  p',
    'p                  p',
    'p                  p',
    'p                  p',
    'p                  p',
    'p                  p',
    'p                  p',
    'p                  p',
    'p                  p',
    'p                  p',
    'p                  p',
    'p                  p',
    'p                  p',
    'p                  p',
    'p                  p',
    'p                  p',
    'p                  p',
    'p                  p',
    'pppppppppppppppppppp'
]

mapa_casa = [
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '        c           ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    '
]


clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        heroi.processar_evento(event)
        
  
    desenha_mapa(mapa, {'p':img_parede, ' ':img_grama})
    desenha_mapa(mapa_casa, {'c':img_casa})
    grupo_heroi.update()
    grupo_heroi.draw(tela)
    pygame.display.flip()