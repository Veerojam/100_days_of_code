from turtle import Turtle
import random

BALL_COLOR = "blue"

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(BALL_COLOR)
        self.penup()
        self.y_step_size = 10
        self.x_step_size = 10

    def change_x_direction(self):
        self.x_step_size *= -1

    def change_y_direction(self):
        self.y_step_size *= -1

    def move(self):
        self.goto(self.xcor() + self.x_step_size, self.ycor() + self.y_step_size)

    def collision_w_paddle(self, paddle):
        # if self.ycor() > paddle.paddle.ycor() - 50 and self.ycor() < paddle.paddle.ycor() + 50 and self.xcor() > paddle.paddle.xcor() - 15 and self.xcor() < paddle.paddle.xcor() + 15:
        #     self.change_x_direction()
        if self.distance(paddle.paddle) < 55 and (self.xcor() > 320 or self.xcor() < -320):
            self.change_x_direction()

    def miss_paddle(self):
        pass

    def collision_w_wall(self):
        if self.ycor() < -280 or self.ycor() > 280:
            self.change_y_direction()



#   GET AN UDNERSTANDING OF HOW CURRENT COLLISION WITH PADDLE WORKS