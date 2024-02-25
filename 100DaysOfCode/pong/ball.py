from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.goto(0,0)
        self.setheading(180)

    def move(self):
        WIDTH = 1000
        HEIGHT = 600
        left_edge = -500
        right_edge = 500
        up_edge = 300
        bottom_edge = -300
        RIGHT = 0
        UP = 90
        LEFT = 180
        DOWN = 270
        self.forward(2)
        print(int(self.xcor()), int(self.ycor()))
        if int(self.xcor()) >= right_edge:
            self.setheading(LEFT)

        elif int(self.xcor()) <= left_edge:
            self.setheading(RIGHT)

        elif int(self.ycor()) >= up_edge:
            self.setheading(DOWN)

        elif int(self.ycor()) <= bottom_edge:
            self.setheading(UP)

