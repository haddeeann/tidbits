from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"score {self.score}", align='center', font=('Arial', 24, 'normal'))

    def make_score(self):
        self.clear()
        self.score += 1
        self.write(f"score {self.score}", align='center', font=('Arial', 24, 'normal'))

