# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("ball.png")

x = 0
y = 0
x_speed = 1
y_speed = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    x += x_speed
    if x_speed > 0 and x+robot.get_width() >= 640:
        x_speed = -x_speed
    if x_speed < 0 and x <= 0:
        x_speed = -x_speed

    y += y_speed
    if y_speed > 0 and y+robot.get_height() >= 480:
        y_speed = -y_speed
    if y_speed < 0 and y <= 0:
        y_speed = -y_speed

    clock.tick(60)


# Answers!!!
# import pygame
# import math
 
# pygame.init()
# width, height = 640, 480
# screen = pygame.display.set_mode((width, height))
 
# ball = pygame.image.load("ball.png")
 
# x = 0
# y = 0
# ball_x = 2
# ball_y = 2
# clock = pygame.time.Clock()
 
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
 
#     x += ball_x
#     y += ball_y
 
#     if x == 0 or x+ball.get_width() == width:
#         ball_x = -ball_x
#     if y == 0 or y+ball.get_height() == height:
#         ball_y = -ball_y
 
#     screen.fill((0, 0, 0))
#     screen.blit(ball, (x, y))
#     pygame.display.flip()
 
#     clock.tick(60)