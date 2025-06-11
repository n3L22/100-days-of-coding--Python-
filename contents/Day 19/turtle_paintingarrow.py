# #HIGHER ORDER FUNCTIONS
# #a function that can work with other functions 
# #for example 
# def divide(n1,n2):
#     return n1/n2
# def subtract(n1/n2):
#     return n1-n2

# #higher order function can be like this 
# def calculator(n1, n2, func):
#     return func(n1, n2)

# #when call it 
# result = calculator(2,3,divide)
# print(result)

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.backward(10)
    
def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clearscreen():
    tim.reset()
    
#use listen to use function as inputs 
screen.listen()

#      when pressing space trigger the function move without parenthesis
screen.onkey(key='w', fun=move_forwards)
#or you can do it with positional arguments like below
#screen.onkey(move_backwards,'s')
#or keep doing with key arguments 
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clearscreen)

screen.exitonclick()


