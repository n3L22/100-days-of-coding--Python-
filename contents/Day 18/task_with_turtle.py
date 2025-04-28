from turtle import Turtle, Screen


#tkinter is what turtle is relying on 

timmy = Turtle()

timmy.shape("square")
timmy.color("bisque4")

#challenge 1 - draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)


#challenge 2 - draw a dashed line 
# for _ in range(6):
#     timmy.pendown()
#     timmy.forward(20)
#     timmy.penup()
#     timmy.forward(20)

#challenge 3 draw 10 shapes inside each other
from random import random, choice

# timmy.teleport(50,100)
# sides = 3
# while sides <=10:
#     rgb = random(),random(),random()
#     timmy.color(rgb)
#     for _ in range(sides):
#         timmy.right(360/sides)
#         timmy.forward(100)
#     sides +=1
    
#challenge 4 Draw a random walk 
# timmy.pensize(10)
# timmy.speed(0) #0 or "fastest"
# angle = [0,90,180,270]
# for _ in range(100):
#     timmy.setheading(choice(angle))
#     rgb = random(),random(),random()
#     timmy.color(rgb)
#     timmy.forward(20)
    

#challenge 5 Draw a spirograph 
# timmy.speed(0)
# for _ in range (36):
#     rgb = random(),random(),random()
#     timmy.color(rgb)
#     timmy.circle(50)
#     timmy.right(10)
    


screen = Screen()
screen.exitonclick()