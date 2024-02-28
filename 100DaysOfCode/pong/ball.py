from turtle import Turtle


class Ball(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.penup()
        self.color('white')
        self.shape('circle')
        self.goto(0,0)
        self.setheading(170)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_bounce()
        if self.xcor() > 430 or self.xcor() < -430:
            self.x_bounce()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1