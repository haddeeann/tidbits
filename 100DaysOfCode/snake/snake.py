import turtle


class Snake:
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = turtle.Turtle()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.speed(1)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

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
