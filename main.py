from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



#default turtle shape = 20*20
#Create a screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('PONG')
screen.tracer(0)

#create a paddle

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, key='Up')
screen.onkey(r_paddle.go_down, key='Down')
screen.onkey(l_paddle.go_up, key='w')
screen.onkey(l_paddle.go_down, key='s')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with the wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()
        ball.speed(5)

    #detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()



    #detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()























screen.exitonclick()
