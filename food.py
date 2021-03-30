from turtle import Turtle
import random as rand
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('green')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x = rand.randint(-280, 280)
        y = rand.randint(-280, 280)
        self.goto(x, y)

