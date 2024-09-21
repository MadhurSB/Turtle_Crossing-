from turtle import Turtle

FONT = ("Calibri", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()
        self.color("white")

    def update_scoreboard(self):
        self.clear()
        self.color("white")
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_Level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def reset_score(self):
        self.level = 1
        self.update_scoreboard()  # Resets the display
