# import tkinter

# window = tkinter.Tk()
# window.title("My First GUI Program ")
# #to scale the window 
# window.minsize(width=500, height=300)

# #label but not enough like this
# my_label= tkinter.Label(text="Label test", font=("Arial", 24))

# #to simply create more labels
# my_label["text"] = "Newww text"

# #should specify the properties of it in order to show
# #my_label.pack() # this will put it in center top
# my_label.place(x=0,y=0) #x0 and y0  is at the top left 

# def button_clicked():
#     new_text = input.get()
#     my_label.config(text=new_text)
    
# #we can also do buttons in tkinter
# button = tkinter.Button(text="click me", command=button_clicked)
# button.pack()
# button.grid(column=0, row=0)

# #Entry components 
# input = tkinter.Entry(width=10)
# #input.pack()
# #remember if the first one is 0,0 for col and row thats when you can do bigger numbers
# input.grid(column=1, row=1)

# #to move or position stuff around we have pack(), place() and grid()
# #you cannot use grid and pack together
# window.mainloop()


#challenge 
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program ")
#to scale the window 
window.minsize(width=500, height=300)
#will do the layout add space around can do this in every block if you want
window.config(padx=20, pady=20)
#label but not enough like this
my_label= tkinter.Label(text="Label test", font=("Arial", 24))

#to simply create more labels
my_label["text"] = "Newww text"

#should specify the properties of it in order to show
#my_label.pack() # this will put it in center top
my_label.grid(column=0,row=0) #x0 and y0  is at the top left 

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    
#we can also do buttons in tkinter
button = tkinter.Button(text="click me", command=button_clicked)
button.grid(column=2, row=0)

#Entry components 
input = tkinter.Entry(width=10)
#input.pack()
#remember if the first one is 0,0 for col and row thats when you can do bigger numbers
input.grid(column=1, row=1)

#we can also do buttons in tkinter
button1 = tkinter.Button(text="new button", command=button_clicked)
button1.grid(column=3, row=2)
#to move or position stuff around we have pack(), place() and grid()
#you cannot use grid and pack together
window.mainloop()