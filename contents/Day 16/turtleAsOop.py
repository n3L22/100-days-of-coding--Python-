#module        #import class
from turtle import Turtle, Screen

#object       #class
mitorto = Turtle()

#object   #attribute
mitorto.shape("turtle")
mitorto.color("brown1")
mitorto.forward(100)
print(mitorto)


my_screen = Screen()

#       object   #attribute
print(my_screen.canvheight)


#object       #method
my_screen.exitonclick()

#use PyPI to search for packages on python