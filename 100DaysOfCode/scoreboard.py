from turtle import Turtle
ALIGN = 'center'
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"score {self.score}", align=ALIGN, font=FONT)

    def make_score(self):
        self.clear()
        self.score += 1
        self.write(f"score {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color('white')
        self.write(f"GAME OVER", align=ALIGN, font=FONT)

