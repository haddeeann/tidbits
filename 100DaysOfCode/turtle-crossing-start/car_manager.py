from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLORS[0])
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        y = random.randint(-225, 225)
        self.goto(400, y)

    def move(self):
        new_x = self.xcor() - MOVE_INCREMENT
        new_y = self.ycor()
        self.goto(new_x, new_y)

