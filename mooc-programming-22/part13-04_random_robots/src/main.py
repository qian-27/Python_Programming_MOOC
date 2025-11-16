# WRITE YOUR SOLUTION HERE:
import random
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
width = robot.get_width()
height = robot.get_height()

max_width = 640-width
max_hight = 480-height
for i in range(1000):
   x = int(round(random.random() * max_width, 0))
   y = int(round(random.random() * max_hight, 0))
   window.blit(robot, (x, y))


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
