# WRITE YOUR SOLUTION HERE:
import random
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")



# min_x = 0
max_x = 640 - robot.get_width()
# min_y = 0 - robot.get_height()
# max_y = 480 - robot.get_height()

x_list = []
for i in range(100):
  x = int(round(random.random() * max_x, 0))
  x_list.append(x)
y = -83
velocity = 1

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
 
    # for i in range(2):
    #   x = int(round(random.random() * max_x, 0))
    #   y = 0 - robot.get_height()
    #   window.blit(robot, (x, y))

    window.blit(robot, (x, y))

    if y+robot.get_height() < 480:
      y += velocity
    elif y+robot.get_height() == 480:
      if x > -robot.get_width() and x < 320:
        x -= velocity
      elif x >= 320 and x < 640 + robot.get_width():
        x += velocity
  
    pygame.display.flip()

    clock.tick(60)







# pygame.init()
# window = pygame.display.set_mode((640, 480))

# robot = pygame.image.load("robot.png")

# # def location():
# #   max_x = 640 - robot.get_width()
# #   x = int(round(random.random() * max_x, 0))
  
# #   return x

# # x = location()
# max_x = 640 - robot.get_width()
# y = -83
# velocity = 1
# clock = pygame.time.Clock()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()

#     window.fill((0, 0, 0))

#     for i in range(10):
#       x = int(round(random.random() * max_x, 0))
#       window.blit(robot, (x, y))
#       pygame.display.flip()
  
#       if y+robot.get_height() < 480:
#         y += velocity
#       elif y+robot.get_height() == 480:
#         if x > -robot.get_width() and x < 320:
#           x -= velocity
#         elif x >= 320 and x < 640 + robot.get_width():
#           x += velocity
  
#     clock.tick(60)