from turtle import Turtle

MOVE_DISTANCE = 20
PADDLE_COLOR = "white"

class Paddle:

    def __init__(self, x_cor, y_cor):
        self.paddle = Turtle("square")
        self.paddle.color(PADDLE_COLOR)
        self.paddle.penup()
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.goto(x_cor, y_cor)
        self.ball_has_bounced = False

    def go_up(self):
        new_y = self.paddle.ycor() + MOVE_DISTANCE
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - MOVE_DISTANCE
        self.paddle.goto(self.paddle.xcor(), new_y)

