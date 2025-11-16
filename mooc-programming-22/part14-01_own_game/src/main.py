# Complete your game here
import pygame
import random

class CollectingCoins:
    def __init__(self):
        # initial
        pygame.init()

        self.screen_width = 640
        self.screen_height = 480
        self.background_color = (192, 192, 192)
        self.score = 0
        self.game_state = "running"

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Collecting Coins")
        self.clock = pygame.time.Clock()

        # Door image
        self.door = pygame.image.load("door.png")
        self.door_x = 596
        self.door_y = 416

        # Create random coins
        self.coin = pygame.image.load("coin.png")
        random_max_width = self.screen_width - self.coin.get_width()
        random_max_hight = self.screen_height - self.coin.get_height()
        self.coin_list = []
        for i in range(10):
            coin_x = random.randint(0, random_max_width)
            coin_y = random.randint(0, random_max_hight)
            self.coin_list.append(pygame.Rect(coin_x, coin_y, 40, 40))
        
        # Create robot
        self.robot = pygame.image.load("robot.png")
        self.robot_x = 0
        self.robot_y = 0
        self.target_x = 0
        self.target_y = 0
        self.robot_speed = 4

        # Create monster
        self.monster = pygame.image.load("monster.png")
        monster_max_width = self.screen_width - self.monster.get_width()
        monster_max_hight = self.screen_height - self.monster.get_height()
        self.monster_x = random.randint(400, monster_max_width)
        self.monster_y = random.randint(300, monster_max_hight)
        self.monster_speed = 1

        self.main_loop()



    def main_loop(self):
        while True:
            self.check_events()
            self.load_image()
            self.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEMOTION:
                self.target_x = event.pos[0] - self.robot.get_width() / 2
                self.target_y = event.pos[1] - self.robot.get_height() / 2   


# function for text
    def draw_text(self, size:int, t: str, x: int, y: int):
        self.font = pygame.font.SysFont("Arial", size)
        text = self.font.render(t, True, (0, 0, 0))
        self.screen.blit(text, (x, y))

# function for loading image
    def load_image(self):
        # draw background
        self.screen.fill(self.background_color)

        # draw random coins
        for c in self.coin_list:
            self.screen.blit(self.coin, c)

        # draw escape_door
        self.screen.blit(self.door, (self.door_x, self.door_y))

        # draw robot
        self.screen.blit(self.robot, (self.robot_x, self.robot_y))
        # Robot movement
        if self.robot_x > self.target_x:
            self.robot_x -= self.robot_speed
        if self.robot_x < self.target_x:
            self.robot_x += self.robot_speed
        if self.robot_y > self.target_y:
            self.robot_y -= self.robot_speed
        if self.robot_y < self.target_y:
            self.robot_y += self.robot_speed

        # range limits of robot
        self.robot_x = max(self.robot_x, 0)
        self.robot_x = min(self.robot_x, self.screen_width - self.robot.get_width())
        self.robot_y = max(self.robot_y, 30)
        self.robot_y = min(self.robot_y, self.screen_height - self.robot.get_height())

        # draw monster
        self.screen.blit(self.monster, (self.monster_x, self.monster_y))
        # Monster movement
        if self.monster_x > self.robot_x:
            self.monster_x -= self.monster_speed
        if self.monster_x < self.robot_x:
            self.monster_x += self.monster_speed
        if self.monster_y > self.robot_y:
            self.monster_y -= self.monster_speed
        if self.monster_y < self.robot_y:
            self.monster_y += self.monster_speed

        # show_score
        self.draw_text(24, f"Score: {self.score}", 0, 0)
        self.draw_text(16, f"Robot follow the mouse direction. Please stay away from monster.", 170, 5)
        if self.game_state == "win":
            self.draw_text(24, f"Escape succeed! Score: {self.score}", 170, 240)
        if self.game_state == "lose":
            self.draw_text(24, f"Caught by monster! Game over!", 150, 240)

        pygame.display.flip()
        self.clock.tick(60)



# function for updating
    def update(self):
    # collected coins
        the_player = pygame.Rect(self.robot_x, self.robot_y, 50, 86)
        for c in self.coin_list:
            if c.colliderect(the_player):
                self.coin_list.remove(c)
                self.score += 10

    # escape succeed
        the_door = pygame.Rect(self.door_x, self.door_y, 50, 70)
        if the_player.colliderect(the_door):
            self.monster_speed = 0
            self.robot_speed = 0
            self.game_state = "win"

    # caught by monster
        the_monster = pygame.Rect(self.monster_x, self.monster_y, 30, 30)
        if the_player.colliderect(the_monster):
            self.robot_speed = 0
            self.game_state = "lose"


if __name__ == "__main__":
    CollectingCoins()


# The robot follows the mouse's direction with +4 speed.
# The monster hunts the robot with +1 speed.
# Game will be ended immediately when robot touches the monster or blue door.
# Each coin is worth 10 points, maximum points of this game is 100.






# # Complete your game here
# import pygame
# import random


# def draw_text(t: str, x: int, y: int):
#     text = font.render(t, True, (255, 0, 0))
#     screen.blit(text, (x, y))


# # constant variables
# screen_width = 640
# screen_height = 480
# screen_size = (screen_width, screen_height)
# background_color = (192, 192, 192)
# game_state = "running"


# # initial
# pygame.init()
# screen = pygame.display.set_mode(screen_size)
# pygame.display.set_caption("Collecting Coins")
# clock = pygame.time.Clock()
# font = pygame.font.SysFont("Arial", 24)


# # Create random coins
# coin = pygame.image.load("coin.png")
# random_max_width = screen_width - coin.get_width()
# random_max_hight = screen_height - coin.get_height()
# coin_list = []
# for i in range(10):
#     coin_x = random.randint(0, random_max_width)
#     coin_y = random.randint(0, random_max_hight)
#     coin_list.append(pygame.Rect(coin_x, coin_y, 40, 40))

# # Escape door positions
# door = pygame.image.load("door.png")
# door_x = screen_width - 44
# door_y = screen_height - 64

# # Robot
# robot = pygame.image.load("robot.png")
# robot_x = 0
# robot_y = 0
# target_x = 0
# target_y = 0
# robot_speed = 4

# # Create monster
# monster = pygame.image.load("monster.png")
# monster_max_width = screen_width - monster.get_width()
# monster_max_hight = screen_height - monster.get_height()
# monster_x = random.randint(300, monster_max_width)
# monster_y = random.randint(300, monster_max_hight)
# monster_list = []
# monster_list.append(pygame.Rect(monster_x, monster_y, 40, 40))
# monster_speed = 1

# # score
# score = 0


# while True:
#     # game loop

#     # input
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit(0)

#         if event.type == pygame.MOUSEMOTION:
#             target_x = event.pos[0] - robot.get_width() / 2
#             target_y = event.pos[1] - robot.get_height() / 2

#    # draw background
#     screen.fill(background_color)

#    # draw random coins
#     for c in coin_list:
#         screen.blit(coin, c)

#    # draw escape_door
#     screen.blit(door, (door_x, door_y))

#    # draw robot
#     screen.blit(robot, (robot_x, robot_y))
#    # Robot movement
#     if robot_x > target_x:
#         robot_x -= robot_speed
#     if robot_x < target_x:
#         robot_x += robot_speed
#     if robot_y > target_y:
#         robot_y -= robot_speed
#     if robot_y < target_y:
#         robot_y += robot_speed

#     robot_x = max(robot_x, 0)
#     robot_x = min(robot_x, screen_width - robot.get_width())
#     robot_y = max(robot_y, 30)
#     robot_y = min(robot_y, screen_height - robot.get_height())

#    # draw monster
#     screen.blit(monster, (monster_x, monster_y))
#    # Monster movement
#     if monster_x > robot_x:
#         monster_x -= monster_speed
#     if monster_x < robot_x:
#         monster_x += monster_speed
#     if monster_y > robot_y:
#         monster_y -= monster_speed
#     if monster_y < robot_y:
#         monster_y += monster_speed

#    # collected coins
#     the_player = pygame.Rect(robot_x, robot_y, 50, 86)
#     for c in coin_list:
#         if c.colliderect(the_player):
#             coin_list.remove(c)
#             score += 10

#    # escape succeed
#     the_door = pygame.Rect(door_x, door_y, 50, 70)
#     if the_player.colliderect(the_door):
#         monster_speed = 0
#         robot_speed = 0
#         game_state = "win"
#         # draw_text(f"Escape succeed! Score: {score}", 170,240)

#    # caught by monster
#     the_monster = pygame.Rect(monster_x, monster_y, 30, 30)
#     if the_player.colliderect(the_monster):
#         robot_speed = 0
#         game_state = "lose"
#         # draw_text(f"Caught by monster! Game over!", 150, 240)

#    #  Show score
#     draw_text(f"Score: {score}", 0, 0)

#     if game_state == "win":
#         draw_text(f"Escape succeed! Score: {score}", 170, 240)
#     if game_state == "lose":
#         draw_text(f"Caught by monster! Game over!", 150, 240)

#     pygame.display.flip()

#     clock.tick(60)