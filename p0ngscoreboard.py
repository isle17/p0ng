from turtle import Turtle
import random


POSITION = (-50, 250)
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_player_one = 0
        self.score_player_two = 0
        self.goto(POSITION)
        self.pencolor("red")
        self.write(f"{self.score_player_two}     {self.score_player_one}", font=FONT)

        self.hideturtle()
        # self.clear()

    def update_score_player_one(self):
        self.score_player_one += 1
        self.clear()
        self.goto(POSITION)
        self.write(f"{self.score_player_two}    {self.score_player_one}", font=FONT)

    def update_score_player_two(self):
        self.score_player_two += 1
        self.clear()
        self.goto(POSITION)
        self.write(f"{self.score_player_two}    {self.score_player_one}", font=FONT)

    def game_over(self):
        self.goto(-50, 0)
        self.write("Game Over", font=("Arial", 14, "normal"))

    def draw_walls(self):
        coordinates = [(-700, 290), (700, 290), (-700, -290), (700, -290)]
        for i in range(0, 3, 2):
            self.penup()
            self.pencolor("white")
            self.goto(coordinates[i])
            self.pendown()
            self.goto(coordinates[i+1])
        self.penup()

