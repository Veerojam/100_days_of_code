
#import turtle
#timmy = turtle.Turtle()

### Simplified version of the above >

from turtle import Turtle, Screen
timmy = Turtle()
tommy = Turtle()

my_screen = Screen()
my_screen.setworldcoordinates(-1000, -1000, 1000, 1000)

timmy.shape("turtle")
timmy.color("red", "green")

tommy.shape("turtle")
tommy.color("green", "yellow")

timmy.speed(1)


for i in range(64):
    timmy.forward(50)
    timmy.right(6.625)
    tommy.backward(50)
    tommy.left(6.625)

    

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(30)


my_screen.exitonclick()





