from turtle import Turtle
import random
import time


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.lanes = [-260, -200, -140, -80, -20, 40, 100, 160, 220, 280]


    def create_cars(self):
        if random.randint(1, 5) == 1:
            self.car = Turtle("square")
            self.car.penup()
            self.car.color(random.choice(COLORS))
            self.car.shapesize(stretch_wid=1, stretch_len=2)
            self.car.setheading(180)
            random_y = random.choice(self.lanes)
            self.car.goto(310, random_y)
            self.all_cars.append(self.car)

    def move(self):
        for cars in self.all_cars:
            cars.fd(STARTING_MOVE_DISTANCE)        

#