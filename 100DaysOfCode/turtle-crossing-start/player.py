from turtle import Turtle
STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        player = Turtle()
        player.penup()
        player.shape('turtle')
        player.goto(STARTING_POSITION)
        player.color('green')
        player.left(90)
        player.shapesize(stretch_wid=1.5, stretch_len=1.5)
