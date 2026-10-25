
from turtle import Turtle
STARTING_POSITIONS =[(0,0),(-20,0), (-40,0)]
UP = 90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.segments =[]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:

            turtle = Turtle(shape='square')
            turtle.color('white')
            turtle.penup()
            turtle.goto(position)
            self.segments.append(turtle)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x_cor = self.segments[seg_num - 1].xcor()
            new_y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x_cor, new_y_cor)

        self.head.forward(20)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def extend(self):
        new_segment = Turtle(shape = 'square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


