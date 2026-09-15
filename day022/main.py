from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

""" Move the right paddle """
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

""" Move the left paddle """
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    ball.collision_w_paddle(left_paddle)
    ball.collision_w_paddle(right_paddle)

        
    ball.collision_w_wall()
    if ball.miss_left_paddle():
        scoreboard.increase_r_score()

    if ball.miss_right_paddle():
        scoreboard.increase_l_score()

        
    


screen.exitonclick()

