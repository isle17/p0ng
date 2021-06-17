from turtle import Screen
import time
from paddle_one import PaddleOne
from paddle_two import PaddleTwo
from ball import Ball

screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.title("p0ng")
screen.listen()

paddle1 = PaddleOne()
paddle2 = PaddleTwo()
ball = Ball()

screen.onkey(paddle1.move_up, key="Up")
screen.onkey(paddle1.move_down, key="Down")

screen.onkey(paddle2.move_up, key="w")
screen.onkey(paddle2.move_down, key="s")


# TODO 1 Make it so when the ball connects with the paddle the ball deflects
# TODO 2 Make is so when the ball goes past the goal line the appropriate player scores


ball_in_play = True
while ball_in_play:
    screen.update()
    time.sleep(0.1)

    if 90 < ball.heading() < 270:
        if ball.ycor() > 290 and ball.xcor() < 0:
            ball.deflect_q2()
        elif ball.ycor() < -290 and ball.xcor() < 0:
            ball.deflect_q3()
    elif ball.heading() < 90 or ball.heading() > 270:
        if ball.ycor() > 290 and ball.xcor() > 0:
            ball.deflect_q1()
        elif ball.ycor() < -290 and ball.xcor() > 0:
            ball.deflect_q4()

    for segment in paddle1.paddle:
        if ball.distance(segment) < 21:
            ball.deflect_off_paddle_one()

    for segment2 in paddle2.paddle:
        if ball.distance(segment2) < 21:
            ball.deflect_off_paddle_two()

    ball.move()



screen.exitonclick()
