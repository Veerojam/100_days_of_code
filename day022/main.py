from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()


screen.listen()

""" Move the right paddle """
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

""" Move the left paddle """
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move_ball()
    # Detect collision with paddle:
    if ball.distance(right_paddle) < 10 or ball.distance(left_paddle) < 10:
        ball.collision_w_paddle()
    # Detect collision with wall:
    if ball.xcor() > 780 or ball.xcor() < -780 or ball.ycor() > 580 or ball.ycor() < -580:
        ball.collision_w_wall()


screen.exitonclick()