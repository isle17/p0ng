import random
from turtle import Screen
import time
from paddle import Paddle
from paddle_two import PaddleTwo
from ball import Ball
from p0ngscoreboard import Scoreboard
from walls import Walls

screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.title("p0ng")
screen.tracer(0)
scoreboard = Scoreboard()
walls = Walls()
walls.draw_net()

paddle1 = Paddle()
paddle2 = PaddleTwo()
ball = Ball()

screen.onkeypress(paddle1.move_up, key="Up")
screen.onkeypress(paddle1.move_down, key="Down")
screen.onkeypress(paddle2.move_up, key="w")
screen.onkeypress(paddle2.move_down, key="s")
screen.listen()

ball_in_play = True
while ball_in_play:
    screen.update()
    time.sleep(0.01)

    if 90 < ball.heading() < 270:
        if ball.ycor() > 290:
            reflected_angle = abs(ball.heading() - 360)
            # draw_angle.write(ball.heading())
            print(reflected_angle)
            ball.setheading(reflected_angle)
        elif ball.ycor() < -270:
            # testing new method
            # ball.setheading(135)
            reflected_angle = abs(ball.heading() - 360)
            # reflected_angle = 1
            ball.setheading(reflected_angle)
    elif 270 <= ball.heading() <= 360 or 0 <= ball.heading() <= 90:
        if ball.ycor() > 290:
            # ball.setheading(315)
            reflected_angle = abs(ball.heading() - 360)
            ball.setheading(reflected_angle)
        elif ball.ycor() < -270:
            # ball.setheading(45)
            reflected_angle = abs(ball.heading() - 360)
            ball.setheading(reflected_angle)
    for segment in paddle1.paddle:
        if ball.distance(segment) < 23:
            ball.deflect_off_paddle_one()

    for segment2 in paddle2.paddle:
        if ball.distance(segment2) < 21:
            ball.deflect_off_paddle_two()

    if ball.xcor() > 610:
        scoreboard.update_score_player_two()
        ball.ball_reset_left()

    elif ball.xcor() < -610:
        scoreboard.update_score_player_one()
        ball.ball_reset_right()

    ball.move()

screen.exitonclick()
