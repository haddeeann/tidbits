import turtle
import time
from snake import Snake


def draw_snake():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")  # Set the background color here
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    game = True
    while game:
        screen.update()
        time.sleep(.1)
        snake.move()

    # Create the turtle and set its attributes
    screen.exitonclick()


draw_snake()
