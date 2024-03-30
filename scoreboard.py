from turtle import Turtle, Screen
from snake import Snake


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        x = 0
        y = 250
        self.goto(x, y)
        self.score = 0



    def add_score(self):
        self.score += 1