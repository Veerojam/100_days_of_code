from turtle import Turtle
import random

BALL_COLOR = "blue"

class Ball:

    def __init__(self):
        self.ball = Turtle("circle")
        self.ball.color(BALL_COLOR)
        self.ball.penup()
        random_y = random.randint(-280, 280)
        #random_heading = random.choice
        self.ball.setpos(0, random_y)
        

    def move_ball(self):
        self.ball.setheading(90)
        #self.ball.fd(1)
        # new_y = self.ball.ycor() - MOVE_DISTANCE
        # new_x = self.ball.xcor() - MOVE_DISTANCE
        # self.ball.goto(self.ball.xcor(), new_y)

    def collision_w_paddle(self):
        #if distance()
        pass

    def miss_paddle(self):
        pass

    def collision_w_wall(self):
        pass