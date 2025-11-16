# WRITE YOUR SOLUTION HERE:
import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")

# Robot 1
x = 400
y = 200

to_right = False
to_left = False
to_up = False
to_down = False


# Robot 2
x2 = 100
y2 = 150

t_right = False
t_left = False
t_up = False
t_down = False
 
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
      # Robot 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False

      # Robot 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                t_left = True
            if event.key == pygame.K_d:
                t_right = True
            if event.key == pygame.K_w:
                t_up = True
            if event.key == pygame.K_s:
                t_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                t_left = False
            if event.key == pygame.K_d:
                t_right = False
            if event.key == pygame.K_w:
                t_up = False
            if event.key == pygame.K_s:
                t_down = False
 
        if event.type == pygame.QUIT:
            exit()
   
   # Robot 1
    if to_right:
        x += 2
    if to_left:
        x -= 2
    if to_up:
        y -= 2
    if to_down:
        y += 2

    x = max(x,0)
    x = min(x,width-robot.get_width())
    y = max(y,0)
    y = min(y,height-robot.get_height())


   # Robot 2
    if t_right:
        x2 += 2
    if t_left:
        x2 -= 2
    if t_up:
        y2 -= 2
    if t_down:
        y2 += 2

    x2 = max(x2,0)
    x2 = min(x2,width-robot.get_width())
    y2 = max(y2,0)
    y2 = min(y2,height-robot.get_height())


    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    screen.blit(robot, (x2, y2))
    pygame.display.flip()
 
    clock.tick(60)



# Answers!!!
# import pygame
 
# pygame.init()
# width, height = 640, 480
# screen = pygame.display.set_mode((width, height))
 
# robot = pygame.image.load("robot.png")
 
# # positions of robots
# positions = [[0, 0],
#           [width-robot.get_width(), height-robot.get_height()]]
 
# controls = []
# # key, which robot moves, horizontal movement, vertical movement
# controls.append((pygame.K_LEFT, 0, -2, 0))
# controls.append((pygame.K_RIGHT, 0, 2, 0))
# controls.append((pygame.K_UP, 0, 0, -2))
# controls.append((pygame.K_DOWN, 0, 0, 2))
# controls.append((pygame.K_a, 1, -2, 0))
# controls.append((pygame.K_d, 1, 2, 0))
# controls.append((pygame.K_w, 1, 0, -2))
# controls.append((pygame.K_s, 1, 0, 2))
 
# clock = pygame.time.Clock()
 
# key_pressed = {}
 
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             key_pressed[event.key] = True
 
#         if event.type == pygame.KEYUP:
#             del key_pressed[event.key]
 
#         if event.type == pygame.QUIT:
#             exit()
 
#     for key in controls:
#         if key[0] in key_pressed:
#             positions[key[1]][0] += key[2]
#             positions[key[1]][1] += key[3]
 
#     screen.fill((0, 0, 0))
#     for i in range(2):
#         screen.blit(robot, (positions[i][0], positions[i][1]))
#     pygame.display.flip()
 
#     clock.tick(60)