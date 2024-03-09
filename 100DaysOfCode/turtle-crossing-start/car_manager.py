from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self, road_height):
        super().__init__()
        self.car_lane = road_height - 10
        self.cars = []
        self.first_round = True
        top_y = 225
        bottom_y = -225

    def batch_manager(self, play):
        self.make_batch()
        self.remove_cars()
        collision = self.detect_collide(play)
        if not collision:
            self.move()
        else:
            return 'game_over'

    def detect_collide(self, play):
        for car in self.cars:
            x_distance = abs(car.xcor() - play.xcor())
            y_distance = abs(car.ycor() - play.ycor())
            if x_distance < 35 and y_distance < 28:
                return True

    def make_batch(self):
        random_chance = random.randint(1, 48)
        if random_chance == 1 or self.first_round:
            for car_num in range(6):
                self.make_car(car_num)
            self.first_round = False

    def remove_cars(self):
        for car in self.cars:
            if car.xcor() < -325:
                self.cars.remove(car)

    def make_car(self, car_num):
        color_index = car_num
        car = Turtle()
        car.color(COLORS[color_index])
        car.shape('square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        x = random.randint(400, 900)
        y = random.randint(-self.car_lane, self.car_lane)
        car.goto(x, y)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(MOVE_INCREMENT)

