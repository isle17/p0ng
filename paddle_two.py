from turtle import Turtle

X = -600
COORDINATES_PADDLE_TWO = [(X, 40), (X, 20), (X, 0), (X, -20), (X, -40)]

COLOR = ["white", "green", "blue", "red", "yellow"]
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180


class PaddleTwo(Turtle):

    def __init__(self):
        self.paddle = []
        self.create_paddle_two()
        self.top = self.paddle[0]
        self.bottom = self.paddle[4]

    def create_paddle_two(self):
        for i in range(0, 5):
            segment = Turtle("square")
            segment.color(COLOR[i])
            segment.penup()
            segment.speed("fastest")
            segment.goto(COORDINATES_PADDLE_TWO[i])
            self.paddle.append(segment)

    def move_up(self):
        # Need to make the middle follow the top then the bottom follow the middle
        self.top.setheading(NORTH)
        for seg_num in range(len(self.paddle) - 1, 0, -1):
            new_x = self.paddle[seg_num - 1].xcor()
            new_y = self.paddle[seg_num - 1].ycor()
            self.paddle[seg_num].goto(new_x, new_y)
        self.top.forward(20)

    def move_down(self):
        self.bottom.setheading(270)
        for seg_num in range(0, len(self.paddle) - 1):
            new_x = self.paddle[seg_num + 1].xcor()
            new_y = self.paddle[seg_num + 1].ycor()
            self.paddle[seg_num].goto(new_x, new_y)
        self.bottom.forward(20)
