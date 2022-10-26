from turtle import Turtle
from random import randint, choice


class Food(Turtle):
    def __init__(self):
        self.colors = ['purple', "rosybrown", "royalblue", "salmon", "seagreen", 'sienna', 'cornflowerblue', "violet"]
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(choice(self.colors))
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        pos = (randint(-290, 290), randint(-290, 290))
        self.goto(pos)
        self.color(choice(self.colors))
