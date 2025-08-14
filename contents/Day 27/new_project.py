from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=100, height=100, )
window.config(padx=50, pady=20)

#Labels
label_miles = Label(text="Miles", font="Arial, 16")
label_miles.grid(column=2, row=0)

text = Label(text="is equal to", font="Arial, 16")
text.grid(column=0, row=1)

label_km = Label(text="Km", font="Arial, 16")
label_km.grid(column=2,row=1)

#Buttons
def action():
    miles = float(text1.get())
    km = miles * 1.60934
    miles_to_km = Label(text=km, font="Arial, 12")
    miles_to_km.grid(column=1, row=1)


#calls action() when pressed calculate
button = Button(text="Calculate", command=action)
button.grid(column=1,row=2)

text1 = Entry(width=10)
text1.grid(column=1,row=0)


window.mainloop()