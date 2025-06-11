# import colorgram

# # Extract 10 colors from an image
# colors = colorgram.extract('contents/Day 18/colorsofpainting.png', 30)
# rgb_colors = []

# for i in range(30):
#     color = colors[i].rgb
#     # RGB has only 3 components: red, green, blue
#     rgb_tuple = (color.r, color.g, color.b)
#     rgb_colors.append(rgb_tuple)

# print(rgb_colors)

color_list = [ (234, 230, 232), (224, 232, 227), (207, 161, 83), (54, 89, 131), (146, 91, 39), (139, 26, 48), (222, 206, 109), (132, 177, 202), (157, 46, 84), (46, 55, 103), (169, 160, 39), (128, 189, 143), (83, 20, 44), (37, 42, 68), (186, 94, 106), (185, 140, 171), (84, 124, 181), (59, 39, 30), (87, 157, 91), (78, 153, 165), (193, 78, 73), (161, 202, 220), (45, 74, 77), (80, 74, 43), (57, 131, 125), (216, 178, 188), (168, 207, 168), (219, 181, 169)]


import turtle
import random

# Set up screen and color mode
screen = turtle.Screen()
screen.colormode(255)

# Create turtle
arrow = turtle.Turtle()
arrow.shape('arrow')  
dots = 100 

# Starting position
x = -230
y = -225
arrow.hideturtle()
arrow.penup()  # Keep pen up for positioning
arrow.goto(x, y)
# Create a 10x10 grid of circles
for count in range(1, dots):
        # Choose random color and draw circle
        random_col = random.choice(color_list)
        arrow.dot(20,random_col)
        
        arrow.forward(50)
        
        if count % 10 == 0:
            y+=50
            arrow.goto(x, y)

screen.exitonclick()