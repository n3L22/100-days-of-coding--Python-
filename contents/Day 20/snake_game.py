from turtle import Screen, Turtle
#to see each of the updates with delay 
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia 3310 - Snake Game")
screen.tracer(0)
x_pos = 0
segments = []
for _ in range(0, 3):
    segment_1 = Turtle("square")
    segment_1.penup()
    segment_1.color("white")
    segment_1.goto(x_pos,0)
    x_pos-=20
    segments.append(segment_1)

#to freeze the whole body
screen.update()
game_is_on = True 

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    for seg in range(len(segments)-1, 0, -1):
    #explanation: will be that 3rd will go to 2nd and 2nd will go to 1st and will turn
        new_x = segments[seg-1].xcor() #second to last segment position
        new_y = segments[seg-1].ycor() #get hold of y
        segments[seg].goto(new_x, new_y) #3st 
        #telling the last segment to go to the position of 1 before segment 
    #get hold of 1st segment
    segments[0].forward(20)
    
    
    
        
    #the segments are not linked so we will need to change 
    # for seg in segments:
    #     seg.forward(20)
    #segments[0].left[90] -> cannot be done like this 
    
    



screen.exitonclick()