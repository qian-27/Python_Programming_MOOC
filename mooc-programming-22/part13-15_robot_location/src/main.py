# WRITE YOUR SOLUTION HERE:
import random
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")


robot_x = int(round(random.random() * (640 - robot.get_width()), 0))
robot_y = int(round(random.random() * (480 - robot.get_height()), 0))
target_x = 0
target_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            target_x = event.pos[0]
            target_y = event.pos[1]

        if event.type == pygame.QUIT:
            exit(0)
    
    if target_x >= robot_x and target_x <= robot_x + robot.get_width() and target_y >= robot_y and target_y <= robot_y + robot.get_height():
         while True:
            random_x = int(round(random.random() * (640 - robot.get_width()), 0))
            random_y = int(round(random.random() * (480 - robot.get_height()), 0))
            if random_x != robot_x or random_y != robot_y:
               break

         # if random_x != robot_x or random_y != robot_y:
         robot_x = random_x
         robot_y = random_y

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)




# Answers!!!
# import pygame
# from random import randint
 
# pygame.init()
# width, height = 640, 480
# screen = pygame.display.set_mode((width, height))
 
# robot = pygame.image.load("robot.png")
 
# x = randint(0, width-robot.get_width())
# y = randint(0, height-robot.get_height())
 
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_x = event.pos[0]
#             mouse_y = event.pos[1]
 
#             hit_x = mouse_x >= x and mouse_x <= x+robot.get_width()
#             hit_y = mouse_y >= y and mouse_y <= y+robot.get_height()
 
#             if hit_x and hit_y:
#                 x = randint(0, width-robot.get_width())
#                 y = randint(0, height-robot.get_height())
 
#         if event.type == pygame.QUIT:
#             exit()
 
#         screen.fill((0, 0, 0))
#         screen.blit(robot, (x, y))
#         pygame.display.flip()