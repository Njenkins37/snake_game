from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width= 600, height= 600)
    screen.bgcolor("Black")
    screen.title("Snake Game")
    snake = Snake()
    screen.tracer(0)
    screen.listen()
    screen.onkey(snake.move_left, "Left")
    screen.onkey(snake.move_right, 'Right')
    screen.onkey(snake.move_up, 'Up')
    screen.onkey(snake.move_down, 'Down')


    game_is_on = True
    food = Food()
    scoreboard = Scoreboard()

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        snake.eat_food(food, scoreboard)
        game_is_on = snake.game_over()

    screen.exitonclick()