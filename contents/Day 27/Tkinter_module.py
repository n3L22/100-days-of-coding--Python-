import tkinter

window = tkinter.Tk()
window.title("My First GUI Program ")
#to scale the window 
window.minsize(width=500, height=300)

#label but not enough like this
my_label= tkinter.Label(text="Label test", font=("Arial", 24))

#to simply create more labels
my_label["text"] = "Newww text"

#should specify the properties of it in order to show
my_label.pack() # this will put it in center top

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    
#we can also do buttons in tkinter
button = tkinter.Button(text="click me", command=button_clicked)
button.pack()

#Entry components 
input = tkinter.Entry(width=10)
input.pack()

    

window.mainloop()
