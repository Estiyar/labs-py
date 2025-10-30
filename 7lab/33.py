import pygame
import sys


pygame.init()


width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('КРУГ')


white = (255, 255, 255)
red = (255, 0, 0)


pos = [width // 2, height // 2]
radius = 25


speed = 20

Done = True
while Done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pos[0] = max(pos[0] - speed, radius)
            if event.key == pygame.K_RIGHT:
                pos[0] = min(pos[0] + speed, width - radius)
            if event.key == pygame.K_UP:
                pos[1] = max(pos[1] - speed, radius)
            if event.key == pygame.K_DOWN:
                pos[1] = min(pos[1] + speed, height - radius)
    

    screen.fill('black')
    pygame.draw.circle(screen, red, pos, radius)
    

    pygame.display.flip()

pygame.quit()