from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
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
    
    new_data = {
        website:{
            "Email":email,
            "Password":password
    }}
    
    
    if len(website) == 0 or len(password) == 0 :
        messagebox.showinfo(title="Oops", message="Please do not leave the fields empty!")
    else:
    #message box
        messagebox.askokcancel(title="Information provided", message=f"These are the details entered: \nEmail: {email} \nPassword: {password}"
                            f"\n\nIs it ok to save it?")
        
        try:
            with open("100-days-of-coding--Python-\contents\Day 29\data.json", mode='r') as data_file:
                #to read a json file
                data = json.load(data_file)
        
        except FileNotFoundError:
            with open("100-days-of-coding--Python-\contents\Day 29\data.json", mode='w') as data_file:
                #(what do you want to write, where do you want to dump it)
                json.dump(new_data, data_file, indent=4)
                
        #else only get triggered if only thr try block succeded
        else:
            #updating the new data
            data.update(new_data)
            #save new data
            with open("100-days-of-coding--Python-\contents\Day 29\data.json", mode='w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            pass_entry.delete(0,END)
        
#------------------------------SEARCH FOR WEBSITE-----------------------------#
def search():
    website =website_entry.get()
    try:
        with open("100-days-of-coding--Python-\contents\Day 29\data.json", mode='r') as data_file:
                    #to read a json file
                    data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
                    
    else:                    
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]["Email"]} \n Password: {data[website]["Password"]}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist!!")


    
        
        
        

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
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=54)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "nneeeelllaa@gmail.com")

pass_entry = Entry(width=35)
pass_entry.grid(column=1, row=3)


#-----------Buttons

#calls add() when pressed
add_button = Button(text="Add", command=save, width=46)
add_button.grid(column=1, row=4, columnspan=2)

#calls generate() when pressed
generate_button = Button(text="Generate Password:", command=generate, justify="left")
generate_button.grid(column=2, row=3)

#calls generate() when pressed
search_button = Button(text="Search:", command=search, width=15)
search_button.grid(column=2, row=1)


window.mainloop()