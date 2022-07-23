from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT_GAME_OVER = ("Courier", 34, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.level}",
                   align="left",
                   font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",
                   align="center",
                   font=FONT_GAME_OVER)
