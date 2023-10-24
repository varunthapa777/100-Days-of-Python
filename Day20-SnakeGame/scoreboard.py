from turtle import Turtle

STYLE = ("Gilroy", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.color("White")
        self.penup()
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.setpos(0, 260)
        self.write(f"Score: {self.score}        "
                   f"High Score: {self.high_score}", move=False, align="center", font=STYLE)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.store_high_score()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.setpos(0, 0)
    #     self.write("GAME OVER", move=False, align="center", font=("arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def store_high_score(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))

    def get_high_score(self):
        with open("highscore.txt") as file:
            self.high_score = int(file.read())