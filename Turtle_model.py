from turtle import *
from random import *


class TurtleMod(Turtle):

    def __init__(self, x, y, color):
        super().__init__(shape="turtle")
        self.penup()
        self.goto(x, y)
        self.color(color)
        self.name = color
        self.points = 0

    def move_forwards(self):
        x = randint(0, 10)
        self.forward(x)
        self.points += x
        if self.points >= 480:
            return True
