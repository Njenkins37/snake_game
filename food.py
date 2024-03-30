from turtle import Turtle
from snake import Snake
import random
ARRAY = []
for num in range(-280, 300, 20):
    ARRAY.append(num)
class Food(Turtle):
    def __init__(self):
        super().__init__()
        array_pos_x = random.randint(0, 28)
        array_pos_y = random.randint(0, 28)
        self.x = ARRAY[array_pos_x]
        self.y = ARRAY[array_pos_y]
        self.t = Turtle('circle')
        self.t.color('blue')
        self.t.penup()
        self.t.setx(self.x)
        self.t.sety(self.y)


    def __delete__(self,):
        pass
    # def make_food(self):


    def change_food(self):
        array_pos_x = random.randint(0, 28)
        array_pos_y = random.randint(0, 28)
        self.x = ARRAY[array_pos_x]
        self.y = ARRAY[array_pos_y]
        self.t.setx(self.x)
        self.t.sety(self.y)


