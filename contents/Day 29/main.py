from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
#---------------------------PASSWORD GENERATOR-------------------#
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)

#-------------------------------SAVE PASSWORD-----------------------------#
def save():
    website =website_entry.get()
    email=email_entry.get()
    password= pass_entry.get()
    
    if len(website) == 0 or len(password) == 0 :
        messagebox.showinfo(title="Oops", message="Please do not leave the fields empty!")
    else:
    #message box
        is_ok = messagebox.askokcancel(title="Information provided", message=f"These are the details entered: \nEmail: {email} \nPassword: {password}"
                            f"\nWebsite: {website}. \nIs it ok to save it?")
        
        if is_ok:
            with open("100-days-of-coding--Python-\contents\Day 29\data.txt", mode='a') as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0,END)
                pass_entry.delete(0,END)
        
        

#-------------------------------UI SETUP------------------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

pass_image = PhotoImage(file=r"100-days-of-coding--Python-\contents\Day 29\logo.png")
canvas = Canvas(width=200, height=200 )
canvas.create_image(100,100, image=pass_image)
canvas.grid(row=0, column=1)

#------------Labels 
#Labels
website_label = Label(text="Website:", font=("Arial", 10))
website_label.grid(column=0, row=1)

username_label = Label(text="Email/ Username:", font=("Arial", 10))
username_label.grid(column=0, row=2)

pass_label = Label(text="Password:", font=("Arial", 10))
pass_label.grid(column=0, row=3)



#-----------Entries
website_entry = Entry(width=54)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=54)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "nneeeelllaa@gmail.com")

pass_entry = Entry(width=35)
pass_entry.grid(column=1, row=3)


#-----------Buttons

#calls action() when pressed
add_button = Button(text="Add", command=save, width=46)
add_button.grid(column=1, row=4, columnspan=2)

#calls action() when pressed
generate_button = Button(text="Generate Password:", command=generate, justify="left")
generate_button.grid(column=2, row=3)

window.mainloop()