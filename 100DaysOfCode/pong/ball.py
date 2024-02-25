from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.goto(0,0)
        self.setheading(170)

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
        self.forward(20)
        if int(self.xcor()) >= right_edge:
            if self.heading() == RIGHT:
                # before heading RIGHT 0
                # after heading LEFT 180
                self.setheading(LEFT)
            else:
                heading = int(self.heading())
                print(heading)
                if heading < UP:
                    self.setheading(heading+90)
                elif heading > DOWN:
                    self.setheading(heading+180)

        elif int(self.xcor()) <= left_edge:
            if self.heading() == LEFT:
                # before heading LEFT 180
                # after heading RIGHT 0
                self.setheading(RIGHT)
            else:
                heading = int(self.heading())
                if heading < LEFT:
                    self.setheading(heading-90)
                elif heading > LEFT:
                    self.setheading(heading+90)

        elif int(self.ycor()) >= up_edge:
            if self.heading() == UP:
                # before heading UP 90
                # after heading DOWN 270
                self.setheading(DOWN)
            else:
                heading = int(self.heading())
                if heading < UP:
                    self.setheading(360-heading)
                elif heading > UP:
                    self.setheading(90+heading)
        elif int(self.ycor()) <= bottom_edge:
            if self.heading() == DOWN:
                # before heading DOWN 270
                # after heading UP 90
                self.setheading(UP)
            else:
                heading = int(self.heading())
                if heading > DOWN:
                    self.setheading(360-heading)
                elif heading < DOWN:
                    self.setheading(heading-90)
