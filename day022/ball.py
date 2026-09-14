from turtle import Turtle
import random

BALL_COLOR = "blue"

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(BALL_COLOR)
        self.penup()
        self.y_step_size = -15
        self.x_step_size = -10
        self.left_ball_has_bounced = False
        self.right_ball_has_bounced = False

    def move(self):
        self.goto(self.xcor() + self.x_step_size, self.ycor() + self.y_step_size)


    def collision_w_paddle(self, paddle):
        if self.distance(paddle.paddle) < 30 and paddle.ball_has_bounced == False:
            print("collision with paddle")
            self.y_step_size *= -1
            self.x_step_size *= -1
            paddle.ball_has_bounced = True
            if self.distance(paddle.paddle) > 30:
                paddle.ball_has_bounced = False


    def miss_paddle(self):
        pass

    def collision_w_wall(self):
        if self.ycor() < -280 or self.ycor() > 280:
            print("collision with wall")
            self.y_step_size *= -1
