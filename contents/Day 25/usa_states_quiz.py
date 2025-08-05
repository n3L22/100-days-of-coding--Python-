import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image ="100-days-of-coding--Python-/contents/Day 25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")




#to get the exact coordinates 
# def get_mouse_click_coor(x, y):
#     print(x,y)
    
# turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()