from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]       # keep track of the “head”

    def create_snake(self):
        x_pos = 0
        for _ in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(x_pos, 0)
            self.segments.append(segment)
            x_pos -= MOVE_DISTANCE

    def move(self):
        # move each segment to the position of the one ahead of it
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        # finally move the head forward
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
