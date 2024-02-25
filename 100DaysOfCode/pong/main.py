from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right = Paddle(425, 0)
left = Paddle(-425, 0)

screen.listen()
screen.onkey(right.go_up, 'Up')
screen.onkey(right.go_down, 'Down')

screen.onkey(left.go_up, 's')
screen.onkey(left.go_down, 'x')

game_on = True
while game_on:
    screen.update()

screen.exitonclick()
