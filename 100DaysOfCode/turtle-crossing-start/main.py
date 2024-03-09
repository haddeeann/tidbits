import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
game_on = True
road = Turtle()
road.color("lightgray")
road_height = 225
rectCors = (
    (-road_height,300), # bottom right
    (road_height,300), #  top right
    (road_height,-300), # top left
    (-road_height,-300) # bottom left
)
bob = CarManager(road_height)
play = Player()

screen.register_shape('rectangle',rectCors)
road.shape('rectangle')

screen.listen()
screen.onkey(play.go_up, "Up")
screen.onkey(play.go_down, "Down")
screen.onkey(play.go_right, "Right")
screen.onkey(play.go_left, "Left")

while game_on:
    time.sleep(0.1)
    level = play.track_level(road_height)
    screen.update()
    game_status = bob.batch_manager(play)
    if game_status == 'game_over':
        game_on = False

screen.exitonclick()


