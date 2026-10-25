from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score_l = 0
        self.score_r = 0
        self.color('white')
        self.update()

    def update(self):
        self.goto(-100, 250)
        self.write(self.score_l, align='center', font=('Courier', 50, 'normal'))
        self.goto(100, 250)
        self.write(self.score_r, align='center', font=('Courier', 50, 'normal'))
        self.hideturtle()



    def points_scored_l(self):
        self.score_l += 1
        self.clear()
        self.update()

    def points_scored_r(self):
        self.score_r += 1
        self.clear()
        self.update()



