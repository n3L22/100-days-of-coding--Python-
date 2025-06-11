from turtle import Turtle, Screen
import random
#each instance, diff attribute, diff methods --> state
#tommy = Turtle()
#nela =Turtle()

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Who do you think is winning? Enter a color:")
colors = ["red", "orange","yellow", "green","blue","purple"]
y_position=[-70,-40,-10,20,50,80]
all_turtles = []
is_race_on = False
#to go to front 

for turtle_index in range(0,6): #from 0 to 5
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -230,y=y_position[turtle_index])
    all_turtles.append(new_turtle)
    
if user_bet:
    is_race_on = True
    
while is_race_on:
    #since the trutle is 40 by 40 in size when it reach the end it should be not 250 but: 250 -(40/2)=230
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color= turtle.pencolor() #because color returns both pencolor and fill color
            if winning_color == user_bet:
                print(f"You've won!! The { winning_color} turtle is the winner!")
            else:
                print(f"Nooope!!! The { winning_color} turtle is the winner!")
            break
        turtle.forward(random.randint(0,10))
    
    
    
    
screen.exitonclick()