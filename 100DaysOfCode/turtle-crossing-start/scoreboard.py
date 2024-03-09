from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.score = f"Level: {self.level}"
        self.write(self.score, font=FONT)

    def level_up(self):
        print('level up')
        self.level += 1
        self.update_scoreboard()
