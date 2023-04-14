from os import scandir
from select import select
from pygame.locals import *
import sys
import pygame
import random
pygame.init()

BLACK = (0,0,0)
RED = (255,0,0)
LINE_COLOR = (50,50,50)
GREEN = (0,255,0)
HEIGHT = 400
WIDTH = 400
MAX_LEVEL = 2
SCORE = 0
font = pygame.font.SysFont("comicsansms", 35)
game_over = font.render("Game Over", True, BLACK)

# text = font.render(SCORE, True, (0, 128, 0))
CELL_WIDTH = 20
BLOCK_SIZE = 20

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Wall:
    def __init__(self, level):
        self.body = []
        f = open("level{}.txt".format(level), "r")

        for y in range(0, HEIGHT // BLOCK_SIZE + 1):
            for x in range(0, WIDTH // BLOCK_SIZE + 1):
                if f.readline(1) == "#":
                    self.body.append(Point(x,y))

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (226,135,67), rect)

class Food:
    def __init__(self):
        self.location = Point(4,10)
    def draw(self):
        point = self.location
        rect = pygame.Rect(CELL_WIDTH * point.x, CELL_WIDTH * point.y, CELL_WIDTH, CELL_WIDTH)
        pygame.draw.rect(SCREEN, (0,255,0), rect)



class Snake:
    def __init__(self):
        self.body = [Point(10,11)]
        self.dx = 0
        self.dy = 0
        self.level = 1

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if self.body[0].x * CELL_WIDTH > WIDTH:
            self.body[0].x = 0
        
        if self.body[0].y * CELL_WIDTH > HEIGHT:
            self.body[0].y = 0

        if self.body[0].x * CELL_WIDTH < 0:
            self.body[0].x = WIDTH / CELL_WIDTH

        if self.body[0].y * CELL_WIDTH < 0:
            self.body[0].x = HEIGHT / CELL_WIDTH
    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(CELL_WIDTH * point.x, CELL_WIDTH * point.y, CELL_WIDTH, CELL_WIDTH)
        pygame.draw.rect(SCREEN, (255,0,0), rect)

        for point in self.body[1:]:
            rect = pygame.Rect(CELL_WIDTH * point.x, CELL_WIDTH * point.y, CELL_WIDTH, CELL_WIDTH)
            pygame.draw.rect(SCREEN, (0,255,0), rect)

    def check_collision(self,food):
        global SCORE
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                self.body.append(Point(food.location.x, food.location.y))
                SCORE += 1
    def check_collision_wall(self,food):
        if self.body[0] == self.body:
            SCREEN.fill(RED)
            SCREEN.blit(game_over, (30,250))



        

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    snake = Snake()
    food = Food()
    wall = Wall(snake.level)


    while True:
        pygame.init()
        drawGrid()
        drawSnake()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        

        
        

        # SCREEN.blit(scores, (360,40))


        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                    snake.dx = -1
                    snake.dy = 0
            if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -1
            if event.key == pygame.K_DOWN:
                    snake.dx = 0 
                    snake.dy = 1


        snake.move()
        snake.check_collision(food)

        if len(snake.body) > 4 and len(snake.body) % 2 == 1:
            new_level = (snake.level + 1) % MAX_LEVEL
            snake = Snake()
            snake.level = new_level
            wall = Wall(snake.level)


        SCREEN.fill(BLACK)


        snake.draw()
        food.draw()
        wall.draw()
        drawGrid()
        """add scores"""
        scores = font.render(str(SCORE), True, (0,255,0))
        SCREEN.blit(scores,(350,0))
        pygame.display.update()
        CLOCK.tick(5)


def drawGrid():
    for x in range (0,WIDTH, CELL_WIDTH):
        for y in range (0, HEIGHT, CELL_WIDTH):
            rect = pygame.Rect(x,y, CELL_WIDTH,CELL_WIDTH)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)
            

def drawSnake():
    snake = [(0,0), (1,0), (2,0)]
    #head
    x,y = snake[0]
    rect = pygame.Rect(CELL_WIDTH * x, CELL_WIDTH * y, CELL_WIDTH, CELL_WIDTH)
    pygame.draw.rect(SCREEN, RED, rect)

    for x,y in snake[1:]:
        rect = pygame.Rect(CELL_WIDTH * x, CELL_WIDTH * y, CELL_WIDTH, CELL_WIDTH)
        pygame.draw.rect(SCREEN, GREEN, rect)

main()
