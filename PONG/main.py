from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()

screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

l_paddle = Paddle(-340, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detecting collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    else:
        pass
    # detecting collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 45 and ball.xcor() > -350:
        ball.bounce_x()

    # detect r_paddle misses
    if ball.xcor() > 380:
        score.l_point()
        ball.reset_position()
    # detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()
