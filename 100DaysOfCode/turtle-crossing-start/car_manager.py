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
        self.make_batch()

    def batch_manager(self):
        self.move()

    def make_batch(self):
        for car_num in range(6):
            self.make_car(car_num)

    def make_car(self, car_num):
        color_index = car_num
        car = Turtle()
        car.color(COLORS[color_index])
        car.shape('square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        car.goto(x, y)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(10)

