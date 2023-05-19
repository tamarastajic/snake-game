from turtle import Turtle


# ~~~~~~~~~~~~~~~~~~~~~~ Score Class ~~~~~~~~~~~~~~~~~~~~~~
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.write_score()

    def write_score(self):
        """A method that writes the current score and high score if available."""
        self.clear()
        if self.high_score != 0:
            self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))
        else:
            self.write(arg=f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def reset_score(self):
        """A method that resets the current score."""
        if self.score > self.high_score:
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.write_score()

