from turtle import Turtle, Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.turtle = None
        self.seg_list = []
        self.create_snake()
        self.head = self.seg_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.seg_list.append(new_segment)

    def move(self):
        for segment in range(len(self.seg_list)-1, 0, -1):
            new_x = self.seg_list[segment - 1].xcor()
            new_y = self.seg_list[segment - 1].ycor()
            self.seg_list[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def add_segment(self):
        x = self.seg_list[len(self.seg_list)-1].xcor()
        y = self.seg_list[len(self.seg_list)-1].xcor()
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(x, y)
        self.seg_list.append(new_segment)


    def game_over(self):
        if round(self.head.xcor()) >= 300 or round(self.head.xcor()) <= (-300):
            return False
        if round(self.head.ycor()) >= 300 or round(self.head.ycor()) <= (-300):
            return False
        return True



