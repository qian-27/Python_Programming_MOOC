# WRITE YOUR SOLUTION HERE:
import pygame
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

pygame.init()
pygame.display.set_caption(current_time)
display = pygame.display.set_mode((640, 480))
display.fill((0, 0, 0))

pygame.draw.circle(display, (255, 0, 0), (320, 240), 200)
pygame.draw.circle(display, (0, 0, 0), (320, 240), 195)
pygame.draw.circle(display, (255, 0, 0), (320, 240), 10)
pygame.draw.line(display, (0, 0, 255), (320, 240), (200, 160), 5)
pygame.draw.line(display, (0, 0, 255), (320, 240), (300, 160), 3)
pygame.draw.line(display, (0, 0, 255), (320, 240), (400, 160), 1)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()