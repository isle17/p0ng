from turtle import Turtle
import random

RANDOM_ANGLE = random.randint(0, 361)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(0)
        self.penup()
        self.color("red")
        self.shape("circle")

    def move(self):
        self.forward(10)

    def deflect_q1(self):
        self.setheading(random.randint(280, 340))

    def deflect_q2(self):
        self.setheading(random.randint(280, 345))

    def deflect_q3(self):
        """If the ball is in quadrant 3 of our coordinate system below the line x=-600
            and touches the line y = -390"""
        self.setheading(random.randint(90, 136))

    def deflect_q4(self):
        self.setheading(random.randint(10, 80))

    def deflect_off_paddle_one(self):
        self.setheading(random.randint(110, 260))

    def deflect_off_paddle_two(self):
        self.setheading(random.randint(0, 90))
