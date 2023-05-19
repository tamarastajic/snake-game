from turtle import Turtle
import random


# ~~~~~~~~~~~~~~~~~~~~~~ Food Class ~~~~~~~~~~~~~~~~~~~~~~
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.move()

    def move(self):
        """A method that moves the food object to a new random location."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
