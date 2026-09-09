from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
         super().__init__()
         self.penup()
         self.hideturtle()
         self.goto(0, 275)
         self.color("white")
         self.score = 0
         self.update_score()

    def update_score(self):
         self.write(f"Score: {self.score}", False, align="center", font=('Arial', 14, 'normal'))

    def increase_score(self):
         self.score += 1
         self.clear()
         self.update_score()

    def game_over(self):
         self.goto(0, 0)
         self.write(f"GAME OVER", False, align="center", font=('Arial', 14, 'normal'))