# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x1 = 320+math.cos(angle + 0.628 * 0)*150-robot.get_width()/2
    y1 = 240+math.sin(angle + 0.628 * 0)*150-robot.get_height()/2

    x2 = 320+math.cos(angle + 0.628 * 1)*150-robot.get_width() /2
    y2 = 240+math.sin(angle + 0.628 * 1)*150-robot.get_height()/2

    x3 = 320+math.cos(angle + 0.628 * 2)*150-robot.get_width() /2
    y3 = 240+math.sin(angle + 0.628 * 2)*150-robot.get_height()/2

    x4 = 320+math.cos(angle + 0.628 * 3)*150-robot.get_width() /2
    y4 = 240+math.sin(angle + 0.628 * 3)*150-robot.get_height()/2

    x5 = 320+math.cos(angle + 0.628 * 4)*150-robot.get_width() /2
    y5 = 240+math.sin(angle + 0.628 * 4)*150-robot.get_height()/2

    x6 = 320+math.cos(angle + 0.628 * 5)*150-robot.get_width() /2
    y6 = 240+math.sin(angle + 0.628 * 5)*150-robot.get_height()/2

    x7 = 320+math.cos(angle + 0.628 * 6)*150-robot.get_width() /2
    y7 = 240+math.sin(angle + 0.628 * 6)*150-robot.get_height()/2

    x8 = 320+math.cos(angle + 0.628 * 7)*150-robot.get_width() /2
    y8 = 240+math.sin(angle + 0.628 * 7)*150-robot.get_height()/2

    x9 = 320+math.cos(angle + 0.628 * 8)*150-robot.get_width() /2
    y9 = 240+math.sin(angle + 0.628 * 8)*150-robot.get_height()/2

    x10= 320+math.cos(angle + 0.628 * 9)*150-robot.get_width() /2
    y10= 240+math.sin(angle + 0.628 * 9)*150-robot.get_height()/2

    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    window.blit(robot, (x3, y3))
    window.blit(robot, (x4, y4))
    window.blit(robot, (x5, y5))
    window.blit(robot, (x6, y6))
    window.blit(robot, (x7, y7))
    window.blit(robot, (x8, y8))
    window.blit(robot, (x9, y9))
    window.blit(robot, (x10, y10))

    pygame.display.flip()

    angle += 0.01
    clock.tick(60)



# Answers!!!
# import pygame
# import math
 
# pygame.init()
# width, height = 640, 480
# screen = pygame.display.set_mode((width, height))
 
# robot = pygame.image.load("robot.png")
 
# angle = 0
# radius = 150
# number = 10
# clock = pygame.time.Clock()
 
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
 
#     screen.fill((0, 0, 0))
#     for i in range(number):
#         x = width/2+math.cos(angle+2*math.pi*i/number)*radius-robot.get_width()/2
#         y = height/2+math.sin(angle+2*math.pi*i/number)*radius-robot.get_height()/2
#         screen.blit(robot, (x, y))
#     pygame.display.flip()
 
#     angle += 0.01
#     clock.tick(60)