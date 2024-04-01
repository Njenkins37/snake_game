from turtle import Turtle, Screen
from snake import Snake

FONT = ('Courier', 24, 'normal')
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        x = 0
        y = 250
        self.goto(x, y)
        self.score = 0
        with open('high_score.txt', mode='r') as file:
            num = file.read()
            self.high_score = num

    def add_score(self):
        self.score += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align= ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align= 'center', font= ('courier', 24, 'normal'), move=False)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open('high_score.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

