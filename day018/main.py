# import colorgram

# color_list = []

# def get_rgb_values(n_of_colors):
#     colors = colorgram.extract("painting.jpg", n_of_colors)
#     for color in colors:
#         color_list.append(tuple(color.rgb))
#     print(color_list)


# get_rgb_values(30)

import random
import turtle as t


color_list = [(198, 12, 32), (250, 238, 16), (39, 76, 190), (239, 227, 5), (38, 217, 69), (230, 158, 44), (28, 39, 157), (215, 75, 13), (202, 14, 11), (15, 154, 15), (243, 34, 165), (231, 16, 124), (71, 9, 31), (60, 15, 8), (225, 141, 211), (10, 97, 62), (47, 214, 232), (217, 161, 9), (19, 19, 44), (11, 227, 239), (237, 156, 220), (85, 73, 210), (76, 212, 161), (85, 233, 197), (58, 233, 243), (4, 67, 42)]

# 10 x 10 canvas
# each dot 20 in size and spaced apart 50
t.colormode(255)
tim = t.Turtle()
tim.speed(3)


# def turn_tim(nr_of_dots_in_row, turns):
#     turns += 1
#     if turns < nr_of_dots_in_row:
#         tim.setheading(90)
#         tim.fd(50)
#         if turns % 2 != 0:
#             tim.setheading(180)
#             tim.fd(50)
#         else:
#             tim.setheading(0)
#             tim.fd(50)
#         make_dots(nr_of_dots_in_row, turns)        
#     else:
#         return

# def make_dots(nr_of_dots_in_row, turns = 0):
#     for nr in range(nr_of_dots_in_row):
#         tim.penup()
#         tim.dot(20, random.choice(color_list))
#         tim.fd(50)
#     turn_tim(nr_of_dots_in_row, turns)

def make_dots(n_dots, dot_size = 20, fd_len = 50):
        row = 0
        while True:
            for n_dot_in_line in range(n_dots):
                tim.penup()
                tim.dot(dot_size, random.choice(color_list))
                if n_dot_in_line != n_dots - 1:
                    tim.fd(fd_len)    

            if row == n_dots - 1:
                break    

            tim.setheading(90)
            tim.fd(fd_len)
            row += 1

            if row % 2 != 0:
                tim.setheading(180)     
            else:
                tim.setheading(0)
            tim.dot(dot_size, random.choice(color_list))
            
make_dots(5, 10, 100)



screen = t.Screen()
screen.exitonclick()