#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

#v1
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def goal():
    while not at_goal():
        if front_is_clear():
            move()
        else:
            hurdle()

def hurdle():
    turn_left()
    while not right_is_clear():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_right() #ta ei tohi prst seda teha
        move()
        turn_right()
        goal()

goal()


#v2:


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        hurdle()



    





