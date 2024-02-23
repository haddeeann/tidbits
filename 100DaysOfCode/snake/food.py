from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.color('blue')
        self.speed('fastest')
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)