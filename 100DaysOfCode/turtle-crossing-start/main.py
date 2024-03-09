import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
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
scoreboard = Scoreboard()

screen.register_shape('rectangle',rectCors)
road.shape('rectangle')

screen.listen()
screen.onkey(play.go_up, "Up")
screen.onkey(play.go_down, "Down")
screen.onkey(play.go_right, "Right")
screen.onkey(play.go_left, "Left")

def start_game():
    game_on = True
    while game_on:
        time.sleep(0.1)
        level_up = play.track_level(road_height)
        if level_up:
            scoreboard.level_up()
        screen.update()
        game_status = bob.batch_manager(play, level_up)
        if game_status == 'game_over':
            game_on = False
            scoreboard.game_over()

start_game()

def restart_game():
    scoreboard.clear_game()
    play.reset_position()
    screen.update()
    start_game()

screen.onkey(restart_game, 'y')

screen.exitonclick()


