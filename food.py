from turtle import Turtle
from snake import Snake
import random
ARRAY = []
for num in range(-280, 300, 20):
    ARRAY.append(num)
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.speed('fastest')

        test_int_x = random.randint(-280, 280)
        test_int_y = random.randint(-280, 280)
        self.goto(test_int_x, test_int_y)
        self.refresh()

        # array_pos_x = random.randint(0, 28)
        # array_pos_y = random.randint(0, 28)
        # self.x = ARRAY[array_pos_x]
        # self.y = ARRAY[array_pos_y]
        # self.t = Turtle('circle')
        # self.t.color('blue')
        # self.t.penup()
        # self.t.setx(self.x)
        # self.t.sety(self.y)


    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


