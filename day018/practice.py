import turtle as t
import random


timmy = t.Turtle()
timmy.shape("turtle")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "black", "gray"]
t.colormode(255)
timmy.speed(0)

""" Spirograph """

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

# for heading in range(1, 360, 5):
#         timmy.setheading(heading)
#         timmy.color(random_color())
#         timmy.circle(80)

def draw_spirograph(size_of_gap):
      for _ in range(360 // size_of_gap):
            timmy.color(random_color())
            timmy.circle(80)
            timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(7)


""" Random Walk """
### My code:

# def random_walk():
#     while True:
#         timmy.pensize(10)
#         move = random.choice([timmy.forward, timmy.backward])
#         turn = random.choice([timmy.left, timmy.right])
#         timmy.pencolor(random.choice(colors))
#         move(50)
#         turn(90)
# random_walk()

### Author's code:

# directions = [0, 90, 180, 270]
# timmy.pensize(15)
# for _ in range(500):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb = (r, g, b)
#     return rgb



""" Draws shapes """

# def draw_shape(sides):
#     angle = 360/sides
#     timmy.pencolor(random.choice(colors))
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)


# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n)










screen = t.Screen()
screen.exitonclick()