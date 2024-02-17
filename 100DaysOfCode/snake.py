import turtle


class Snake:
    def __init__(self):
        self.segments = []
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_positions:
            square = self.draw_square(position)
            self.segments.append(square)

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
        self.segments[0].forward(20)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def right(self):
        self.segments[0].setheading(0)

    def left(self):
        self.segments[0].setheading(180)
