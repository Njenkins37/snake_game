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
    scoreboard.hideturtle()


    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.add_segment()
            scoreboard.add_score()
            scoreboard.clear()
        scoreboard.update_scoreboard()
        if round(snake.head.xcor()) >= 300 or round(snake.head.xcor()) <= (-300):
            snake.reset()
            scoreboard.reset()
        if round(snake.head.ycor()) >= 300 or round(snake.head.ycor()) <= (-300):
            snake.reset()
            scoreboard.reset()



    screen.exitonclick()