from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # Set the background color here
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game = True
while game:
    screen.update()
    time.sleep(.2)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 30:
        food.refresh()
        snake.extend()
        board.make_score()
    edge = 290
    if snake.head.xcor() > edge or snake.head.ycor() > edge or snake.head.xcor() < -edge or snake.head.ycor() < -edge:
        board.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            board.reset()
            snake.reset()

# Create the turtle and set its attributes
screen.exitonclick()
