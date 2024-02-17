import turtle


class Snake:
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self):
        self.segments = []
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_positions:
            square = self.draw_square(position)
            self.segments.append(square)
        self.head = self.segments[0]

    def draw_square(self, position):
        square = turtle.Turtle()
        square.penup()
        square.goto(position)
        square.color("white")
        square.shape("square")
        return square

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].speed(1)
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)

    def down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)

    def left(self):
        if self.head.heading() != self.RIGHT:
            self.segments[0].setheading(self.LEFT)
