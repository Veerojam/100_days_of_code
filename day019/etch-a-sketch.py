import turtle as t

tim = t.Turtle()
screen = t.Screen()
screen.listen()


def move_fwd():
    tim.fd(10)

def move_bwd():
    tim.bk(10)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear_screen():
    tim.reset()


screen.onkey(key="w", fun=move_fwd)
screen.onkey(key="s", fun=move_bwd)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
 
# W = fwd
# S backwrd
# A counter-clockwise
# D clockwise
# C clear drawing