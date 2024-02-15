import turtle
import time

def draw_square(position):
    square = turtle.Turtle()
    square.penup()
    square.goto(position)
    square.color("white")
    square.shape("square")
    return square


def draw_snake():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")  # Set the background color here
    screen.title("Snake Game")
    screen.tracer(0)

    segments = []
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    for position in starting_positions:
        square = draw_square(position)
        segments.append(square)

    game = True
    while game:
        screen.update()
        time.sleep(.1)
        for seg in range(len(segments) - 1, 0, -1):
            new_x = segments[seg - 1].xcor()
            new_y = segments[seg - 1].ycor()
            segments[seg].goto(new_x, new_y)
        segments[0].forward(20)
        segments[0].left(90)

    # Create the turtle and set its attributes
    screen.exitonclick()


draw_snake()
