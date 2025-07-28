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
            self.add_segment((x_pos, 0))
            x_pos -= MOVE_DISTANCE

    def add_segment(self, position):
        """Create a new snake segment at the given position."""
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        """Add a new segment to the snake at the last segment's position."""
        last_position = self.segments[-1].position()
        self.add_segment(last_position)

    def move(self):
        """Move each segment to follow the previous one, then move head forward."""
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
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
