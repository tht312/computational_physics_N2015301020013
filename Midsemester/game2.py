import pygame
from pygame.locals import *
from sys import exit
import time

pygame.init()
screen=pygame.display.set_mode((960,508),0,32)
pygame.display.set_caption("Hello, World!")
background = pygame.image.load(r'D:\back.jpg').convert()
zhadan=pygame.image.load(r'D:\zhadan.png').convert_alpha()
lang=pygame.image.load(r'D:\lang.png').convert_alpha()
yang=pygame.image.load(r'D:\yang.png').convert_alpha()
feiyangyang=pygame.image.load(r'D:\feiyangyang.png').convert_alpha()
wenzi=pygame.image.load(r'D:\wenzi.png').convert_alpha()
lose=pygame.image.load(r'D:\lose.png').convert_alpha()
zhadan_x=0
zhadan_y=277
zhadan_Vy=0
zhadan_Vx=0
FPS = 10
fashe = True
while fashe:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            zhadan_Vx=x/100
            zhadan_Vy=(zhadan_y-y)/10
        zhadan_x=zhadan_x+zhadan_Vx
        zhadan_y=zhadan_y-zhadan_Vy
        if zhadan_y>=508 or zhadan_x>=960:
            zhadan_x=0
            zhadan_y=277
            zhadan_Vx=0
            zhadan_Vy=0
        if zhadan_y>=228 and zhadan_x>=780:
            screen.blit(wenzi, (200,100))       
            pygame.display.update()
            time.sleep(5)
            zhadan_x=0
            zhadan_y=277
            zhadan_Vx=0
            zhadan_Vy=0
        if zhadan_y>=228 and zhadan_x>=350 and zhadan_x<=550:
            screen.blit(lose, (400,100)) 
            pygame.display.update()
            time.sleep(5)
            zhadan_x=0
            zhadan_y=277
            zhadan_Vx=0
            zhadan_Vy=0
            
        screen.blit(background, (0,0))
        screen.blit(lang, (0,307))
        screen.blit(yang, (800,307))
        screen.blit(feiyangyang, (400,307))
        screen.blit(zhadan,(zhadan_x,zhadan_y))
        pygame.display.update()
        pygame.time.Clock().tick(FPS)