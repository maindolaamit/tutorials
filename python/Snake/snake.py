import pygame
import random


class Box:
    def __init__(self, start, dir_x=1, dir_y=0, color=(255, 0, 0)):
        """ Function to Initialize a Box """
        self.color = color
        self.direction_x = dir_x
        self.direction_y = dir_y
        self.pos = start

    def move(self, dir_x, dir_y):
        """ Function to move the Box in a given Direction """
        self.direction_x = dir_x
        self.direction_y = dir_y
        # Change the Direction by adding to it
        self.pos = (self.pos[0] + dir_x, self.pos[1] + dir_y)

    def draw(self, surface, eyes=False):
        global width, rows
        size = width // rows
        x = self.pos[0]
        y = self.pos[1]
        pygame.draw.rect(surface, self.color, (size * x + 1, size * y + 1, size, size))
        if eyes:
            center = size // 2
            radius = 3
            pygame.draw.circle(surface, (0, 100, 0), (size * x + center + radius, size * y + center - radius), radius)
            pygame.draw.circle(surface, (0, 100, 0), (size * x + center + radius, size * y + center + radius), radius)


class Snake():
    body = []  # A snake is composed of different boxes
    turns = {}

    def __init__(self, color, pos):
        self.color = color  # Give color to the Snake
        self.head = Box(start=pos, color=color)  # Create a Head and to the Body
        self.body.append(self.head)
        # Variable to store Directions either in X or Y Directions to capture snake Movement
        self.direction_x = 1
        self.direction_y = 0

    def reset(self):
        """ Metdho to Reset the snake """
        self.head = Box((0, 0))
        self.body.append(self.head)
        # Variable to store Directions either in X or Y Directions to capture snake Movement
        self.direction_x = 1
        self.direction_y = 0

    def move(self):
        # Quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            """ Method to move the snake """
            keys = pygame.key.get_pressed()  # Get the Pressed Key

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.direction_x = -1
                    self.direction_y = 0
                elif keys[pygame.K_RIGHT]:
                    self.direction_x = 1
                    self.direction_y = 0
                elif keys[pygame.K_UP]:
                    self.direction_x = 0
                    self.direction_y = -1
                elif keys[pygame.K_DOWN]:
                    self.direction_x = 0
                    self.direction_y = 1
                elif keys[pygame.QUIt]:
                    print("Exiting game...")
                    pygame.quit();

                self.turns[self.head.pos[:]] = [self.direction_x, self.direction_y]
                # print(self.turns)

        # Move all the boxes in the body
        for i, box in enumerate(self.body):
            pos = box.pos[:]
            if pos in self.turns:
                turn = self.turns[pos]
                box.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(pos)
            else:
                if box.direction_x == -1 and box.pos[0] <= 0:
                    box.pos = (rows - 1, box.pos[1])
                elif box.direction_x == 1 and box.pos[0] >= rows - 1:
                    box.pos = (0, box.pos[1])
                elif box.direction_y == 1 and box.pos[1] >= rows - 1:
                    box.pos = (box.pos[0], 0)
                elif box.direction_y == -1 and box.pos[1] <= 0:
                    box.pos = (box.pos[0], rows - 1)
                else:
                    box.move(box.direction_x, box.direction_y)

    def add_box(self):
        """ Add a box to the Snake body """
        tail = self.body[-1]
        dx_tail = tail.direction_x
        dy_tail = tail.direction_y

        # Take directions of the Tail and append to it
        if dx_tail == 1 and dy_tail == 0:  # Moving to Right
            self.body.append(Box((tail.pos[0] - 1, tail.pos[1]), dx_tail, dy_tail, self.color))
        elif dx_tail == -1 and dy_tail == 0:  # Moving to Left
            self.body.append(Box((tail.pos[0] + 1, tail.pos[1]), dx_tail, dy_tail, self.color))
        elif dx_tail == 0 and dy_tail == 1:  # Moving to Up
            self.body.append(Box((tail.pos[0], tail.pos[1] - 1), dx_tail, dy_tail, self.color))
        elif dx_tail == 0 and dy_tail == -1:  # Moving to Down
            self.body.append(Box((tail.pos[0], tail.pos[1] + 1), dx_tail, dy_tail, self.color))

    def draw(self, surface):
        """ Method to draw the Snake"""
        for i, box in enumerate(self.body):
            if i == 0:
                box.draw(surface, eyes=True)
            else:
                box.draw(surface)


def get_snack(color):
    """ Get a Random snack in the Board """
    global snake

    while True:
        x = random.randint(0, rows)
        y = random.randint(0, rows)
        # Check if Box is in the Snake Body
        print("Snack position ({},{})".format(x, y))
        for box in snake.body:
            print(box.pos)

        if len(list(filter(lambda box: box.pos == (x, y), snake.body))) == 0:
            return Box(start=(x, y), color=color)


def draw_grid(width, rows, surface):
    """ Method to Draw the Grids on Board """
    size = width // rows
    x, y = 0, 0
    for i in range(rows):
        x = x + size
        y = y + size
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))


def draw_board(surface):
    """ Method to draw game Board """
    surface.fill((0, 0, 0,))  # Fill window with black
    global width, rows
    draw_grid(width, rows, surface)
    snack.draw(surface)
    snake.draw(surface)
    pygame.display.update()


def main():
    global rows, width, snack, snake
    rows, width = 20, 500
    win = pygame.display.set_mode((width, width))

    # Create Snake
    snake_color = (255, 0, 0)
    snake = Snake(color=snake_color, pos=(0, 0))

    # Create Snack
    snack_color = (0, 255, 0)
    snack = get_snack(snack_color)

    # Create a clock
    clock = pygame.time.Clock()

    # Loop in the game for Instructions
    flag = True
    while flag:
        pygame.time.delay(50)  # Delay the Window
        clock.tick(10)
        snake.move()
        # Check if Head meets Snack
        if snake.body[0].pos == snack.pos:
            snake.add_box()
            snack = get_snack(snack_color)

        # Game Over if Snake ate himself
        # filter(lambda box: box.pos = snake.body[0].start, snake.body)


        draw_board(win)
        # flag = False


main()
