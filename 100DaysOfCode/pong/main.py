from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkey(paddle.go_up, 'Up')
screen.onkey(paddle.go_down, 'Down')

game_on = True
while game_on:
    screen.update()

screen.exitonclick()
