from turtle import Turtle
import random

RANDOM_ANGLE = random.randint(0, 361)
ball_speed = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(random.randint(0, 361))
        self.speed(ball_speed)
        self.penup()
        self.color("yellow")
        self.shape("circle")

    def move(self):
        self.forward(10)

    # def deflect_q1(self):
    #     self.setheading(random.randint(280, 340))
    #
    # def deflect_q2(self):
    #     self.setheading(random.randint(190, 250))
    #
    # def deflect_q3(self):
    #     """If the ball is in quadrant 3 of our coordinate system below the line x=-600
    #         and touches the line y = -390"""
    #     self.setheading(random.randint(135, 150))
    #
    # def deflect_q4(self):
    #     self.setheading(random.randint(10, 80))
    # TODO 1 Need to fix the angle issues
    def deflect_off_paddle_one(self):
        reflected_angle = (180 - self.heading()) - 10
        self.setheading(reflected_angle)

    def deflect_off_paddle_two(self):
        reflected_angle = (180 - self.heading()) - 10
        self.setheading(reflected_angle)

    def ball_reset_left(self):
        self.speed(ball_speed)
        self.goto(0, 0)
        # self.setheading(random.randint(280, 405))
        self.setheading(160)

    def ball_reset_right(self):
        self.speed(ball_speed)
        self.goto(0, 0)
        # self.setheading(random.randint(120, 230))
        self.setheading(45)
