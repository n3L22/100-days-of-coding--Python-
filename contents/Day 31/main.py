from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
dict_data = {}
try:
    data = pandas.read_csv(r"100-days-of-coding--Python-\contents\Day 31\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(r"100-days-of-coding--Python-\contents\Day 31\data\spanish-english_data - Sheet1.csv")
    dict_data = original_data.to_dict(orient="records")
else:
    #records will make it as a dict inside a list 
    dict_data = data.to_dict(orient="records")


#-----------------------BUTTONS FUNCTIONALITY-----------------#
def click():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict_data)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(canvas_image, image=card_f_img)
    flip_timer = window.after(3000, func=changes_after)
    
def right_click():
    dict_data.remove(current_card)
    data = pandas.DataFrame(dict_data)
    data.to_csv(r"100-days-of-coding--Python-\contents\Day 31\data\words_to_learn.csv", index=False)
    click()
    
    
#-----------------------FLIP THE CARDS------------#

def changes_after():
    canvas.itemconfig(canvas_image, image=card_b_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

#----------------------UI SETUP-------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=changes_after)

canvas = Canvas(width=800, height=526)
card_f_img=PhotoImage(file=r"100-days-of-coding--Python-\contents\Day 31\images\card_front.png")
card_b_img = PhotoImage(file=r"100-days-of-coding--Python-\contents\Day 31\images\card_back.png")
canvas_image= canvas.create_image(400,250, image=card_f_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word= canvas.create_text(400,263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)

wrong_img=PhotoImage(file=r"100-days-of-coding--Python-\contents\Day 31\images\wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=click)
wrong_button.grid(column=0,row=1)

right_img=PhotoImage(file=r"100-days-of-coding--Python-\contents\Day 31\images\right.png")
right_button = Button(image=right_img, highlightthickness=0, command=right_click)
right_button.grid(column=1,row=1)
click()
window.mainloop()