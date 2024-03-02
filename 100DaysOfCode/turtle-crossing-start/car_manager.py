from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.make()

    def make(self):
        car = Turtle()
        car.color(COLORS[0])
        car.shape('square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(10)

