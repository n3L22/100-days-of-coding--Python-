import turtle, pandas, time

screen = turtle.Screen()
screen.title("U.S. States Game")

data = pandas.read_csv(r"100-days-of-coding--Python-\contents\Day 25\50_states.csv")
image ="100-days-of-coding--Python-/contents/Day 25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()      
message_turtle = turtle.Turtle()
message_turtle.hideturtle()
message_turtle.penup()

correct_answer = []
while len(correct_answer) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answer)}/50 Guess the State", prompt="What's another state's name?").title()

    if answer_state in data["state"].values and answer_state not in correct_answer:
        correct_answer.append(answer_state)
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        t.penup()             
        t.goto(x,y)     
        t.write(answer_state)
    else:
        message_turtle.goto(0,0) 
        message_turtle.write("That's a duplicate!", align="center", font=("Arial", 16, "normal"))
        time.sleep(2)
        message_turtle.clear()

message_turtle.goto(0,0) 
message_turtle.write("YOU ARE SMART!!!!", align="center", font=("Arial", 16, "normal"))


#to get the exact coordinates 
# def get_mouse_click_coor(x, y):
#     print(x,y)
    
# turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()