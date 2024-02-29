import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
WIDTH = 900
HEIGHT = 600
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right = Paddle((WIDTH / 2) - 75, 0)
left = Paddle(-((WIDTH / 2) - 75), 0)

ball = Ball(WIDTH, HEIGHT)

screen.listen()
screen.onkey(right.go_up, 'Up')
screen.onkey(right.go_down, 'Down')

screen.onkey(left.go_up, 's')
screen.onkey(left.go_down, 'x')

scoreboard = Scoreboard()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # paddle left and right
    if ball.distance(right) < 50 and ball.xcor() > 350:
        ball.x_bounce()

    if ball.distance(left) < 50 and ball.xcor() < -350:
        ball.x_bounce()

    # left wins point, end game restart
    if ball.xcor() > 430:
        ball.reset_position()
        ball.x_bounce()
        scoreboard.l_point()
    # right wins point, end game restart
    if ball.xcor() < -430:
        ball.reset_position()
        ball.x_bounce()
        scoreboard.r_point()

screen.exitonclick()
