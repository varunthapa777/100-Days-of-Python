import turtle
from turtle import Turtle,register_shape

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

register_shape("turtle.gif")

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle.gif")
        self.penup()
        self.setheading(90)
        self.setpos(0, -280)

    def move_up(self):
        self.forward(10)

    def reset_turtle(self):
        self.setpos(0, -280)