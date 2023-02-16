from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("snake_score.txt") as data:
            self.high_score = int(data.read())

        self.color("red")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score : {self.score} High Score : {self.high_score}",
            True,
            align=ALIGNMENT,
            font=FONT,
        )

    def reset_score(self):

        if self.score > self.high_score:
            self.high_score = self.score

        with open("snake_score.txt", mode="w") as data:
            data.write(f"{self.high_score}")

        self.score = 0
        self.score_board()

    def increase_score(self):
        self.score += 1
        self.score_board()

    def score_board(self):
        self.goto(0, 270)
        self.clear()
        self.update_score()
