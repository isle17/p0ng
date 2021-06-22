from turtle import Turtle


class Walls(Turtle):

    def __init__(self):
        super().__init__()
        self.draw_net()
        self.draw_walls()

    def draw_walls(self):
        coordinates = [(-700, 300), (700, 300), (-700, -280), (700, -280)]
        for i in range(0, 3, 2):
            self.penup()
            self.pencolor("white")
            self.goto(coordinates[i])
            self.pendown()
            self.goto(coordinates[i + 1])
        self.penup()

    def draw_net(self):
        self.goto(0, 290)
        self.setheading(270)
        self.pencolor("green")
        self.width(6)
        for i in range(0, 10):
            self.pendown()
            self.forward(50)
            self.penup()
            self.forward(50)
