import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
game_on = True
bob = CarManager()
while game_on:
    time.sleep(0.1)
    screen.update()
    bob.move()

