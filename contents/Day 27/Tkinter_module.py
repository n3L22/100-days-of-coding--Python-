import tkinter

window = tkinter.Tk()
window.title("My First GUI Program ")
#to scale the window 
window.minsize(width=500, height=300)

#label but not enough like this
my_label= tkinter.Label(text="Label test", font=("Arial", 24))

#should specify the properties of it in order to show
my_label.pack(side = "left") # this will put it in center top

#usually we have **arg ang **kwarg (key word arguments) to put inside methods for example
#a kwarg:
''' key word argument are when you actually call them in methods write(text="what do you write)'''

#an arg:
'''when a method is arg it means that you only have to put that others will be default '''



window.mainloop()

#to make unlimited number of arguments we can simply use *args
def add(*args):
    for n in args:
        print(n)