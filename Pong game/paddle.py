from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x):
      super().__init__()
      self.shape('square')
      self.shapesize(stretch_len=1, stretch_wid=5)
      self.color('white')
      self.penup()
      self.goto(x)



    def up(self):
        self.penup()
        self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        self.penup()
        self.goto(self.xcor(), self.ycor()-20)


