from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia 3310 - Snake Game")

x_pos = 0
for _ in range(0, 3):
    segment_1 = Turtle("square")
    segment_1.penup()
    segment_1.color("white")
    segment_1.goto(x_pos,0)
    x_pos-=20





screen.exitonclick()