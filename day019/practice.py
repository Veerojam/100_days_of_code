import turtle as t

screen = t.Screen()
screen.listen()
screen.setup(width=500, height=400)

#user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
#print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
for color in colors:
    print(color)

for turtle_index in range(0, 6):
    tim = t.Turtle()
    tim.shape("turtle")
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])
    tim = t.Turtle()

# now give each one a different color



screen.exitonclick()