# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
width = robot.get_width()
height = robot.get_height()

y = 0
z = 0
for i in range(10):
    x = 0
    for i in range(10):
        window.blit(robot, (50+x+z, 100+y))
        x += width/1.3
    z += 10
    y += height*0.25

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()