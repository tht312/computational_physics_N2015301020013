import pygame
from sys import exit
pygame.init()
screen=pygame.display.set_mode((650,377),0,32)
pygame.display.set_caption("Hello, World!")
background = pygame.image.load(r'D:\back.jpg').convert()
shell=pygame.image.load(r'D:\bird.png').convert_alpha()
body=pygame.image.load(r'D:\body.png').convert_alpha()
shell_x=0
shell_y=277
shell_Vy=-13
FPS = 10
while True:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    shell_x=shell_x+20
    shell_Vy=shell_Vy+1
    shell_y=shell_y+shell_Vy
    if shell_y>=377:
        shell_x=0
        shell_y=277
        shell_Vy=-13
    screen.blit(background, (0,0))
    screen.blit(body, (0,307))
    screen.blit(shell,(shell_x,shell_y))
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
