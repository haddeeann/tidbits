from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
WIDTH = 1000
HEIGHT = 600
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right = Paddle(425, 0)
left = Paddle(-425, 0)

ball = Ball(WIDTH, HEIGHT)

screen.listen()
screen.onkey(right.go_up, 'Up')
screen.onkey(right.go_down, 'Down')

screen.onkey(left.go_up, 's')
screen.onkey(left.go_down, 'x')

game_on = True
while game_on:
    screen.update()
    ball.move()

screen.exitonclick()
