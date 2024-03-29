from turtle import Turtle
FONT = ("Courier", 24, "normal")
SMALL_FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.color('blue')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 250)
        self.score = f"Level: {self.level}"
        self.write(self.score, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(-150, 0)
        self.color('red')
        self.score = f"GAME OVER! LEVEL {self.level}"
        self.write(self.score, font=FONT)

        self.goto(-150, -30)
        self.color('white')
        self.score = f"To Start New Game, Press y"
        self.write(self.score, font=SMALL_FONT)

    def clear_game(self):
        self.level = 1
        self.setup()
        self.update_scoreboard()
