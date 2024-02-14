import turtle


def draw_square(movement, color):
    snake = turtle.Turtle()
    if movement:
        snake.up()
        snake.backward(movement)
        snake.down()
    snake.color(color)
    snake.shape("square")


def draw_snake():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")  # Set the background color here
    screen.title("Snake Game")
    colors = ["red", "white", "blue"]
    for x in range(3):
        movement = x * 20
        draw_square(movement, colors[x])

    # Create the turtle and set its attributes
    screen.exitonclick()


draw_snake()
