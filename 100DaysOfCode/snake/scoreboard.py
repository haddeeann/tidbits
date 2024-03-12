from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('highscore.txt', mode='r') as file:
            score = file.read()
            if score:
                self.high_score = int(score)
            else:
                self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} || High Score: {self.high_score}", align=ALIGN, font=FONT)

    def make_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            with open('highscore.txt', mode='w') as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color('white')
        self.write(f"GAME OVER", align=ALIGN, font=FONT)
