# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x1 = 0
y1 = 50
velocity1 = 1

x2 = 0
y2 = 150
velocity2 = 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()
    
    x1 += velocity1
    if velocity1 > 0 and x1+robot.get_width() >= 640:
        velocity1 = -velocity1
    if velocity1 < 0 and x1 <= 0:
        velocity1 = -velocity1

    x2 += velocity2
    if velocity2 > 0 and x2+robot.get_width() >= 640:
        velocity2 = -velocity2
    if velocity2 < 0 and x2 <= 0:
        velocity2 = -velocity2

    clock.tick(60)


# Answers!!!
# import pygame
 
# pygame.init()
# width, height = 640, 480
# screen = pygame.display.set_mode((width, height))
 
# robot = pygame.image.load("robot.png")
 
# x1 = 0
# x2 = 0
# speed1 = 1
# speed2 = 2
 
# clock = pygame.time.Clock()
 
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
 
#     x1 += speed1
#     if x1 == 0 or x1+robot.get_width() == width:
#         speed1 = -speed1
#     x2 += speed2
#     if x2 == 0 or x2+robot.get_width() == width:
#         speed2 = -speed2
 
#     screen.fill((0, 0, 0))
#     screen.blit(robot, (x1, 50))
#     screen.blit(robot, (x2, 200))
#     pygame.display.flip()
 
#     clock.tick(60)