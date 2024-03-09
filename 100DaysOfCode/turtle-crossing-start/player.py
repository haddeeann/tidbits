from turtle import Turtle
STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.goto(STARTING_POSITION)
        self.color('green')
        self.left(90)
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        
    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def track_level(self, road_height):
        if self.ycor() > road_height + 20:
            self.goto(STARTING_POSITION)
            return True

    def reset_position(self):
        self.goto(STARTING_POSITION)
        
