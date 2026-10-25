from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from pong_scoreboard import Scoreboard
screen = Screen()

screen.bgcolor('black')
screen.setup(width= 800, height = 600)
screen.tracer(0)

paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun= paddle_r.up, key='Up')
screen.onkey(fun= paddle_r.down, key='Down')
screen.onkey(fun = paddle_l.up, key ='w')
screen.onkey(fun = paddle_l.down, key ='s')
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 60 and ball.xcor() > 320 or ball.distance(paddle_l) <60 and ball.xcor() <-320:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.points_scored_l()

    if ball.xcor() < -380:

        ball.reset_position()
        scoreboard.points_scored_r()























screen.exitonclick()