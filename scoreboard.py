from turtle import Turtle, Screen
from snake import Snake

class Scoreboard:
    def __init__(self):
        self.score = 0

    def add_score(self):
        self.score += 1