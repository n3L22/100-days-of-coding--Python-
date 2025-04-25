from turtle import Turtle, Screen


#tkinter is what turtle is relying on 

timmy = Turtle()

timmy.shape("square")
timmy.color("bisque4")

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)



screen = Screen()
screen.exitonclick()

#    1- in order to import a module 

#keywords   #module 
#import      turtle 

#in order to use it 
#give a name     # call module.classname
#tim = turtle.Turtle()


#      2- another way to use it is to: 
#keyword  #module name   #keyword   #thing in module 
#from     turtle         import      Turtle

#to use this method:
#give a name     # call classname
#tim    =          Turtle()

#    3 - if you want to import everything from module:
#from turtle import *


#    4 - you can import as - to represent the whole turtle 
#import turtle as t

#give a name     # call module as said.classname
#tim = t.Turtle()