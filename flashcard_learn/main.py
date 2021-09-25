from tkinter import *
from pandas import *
import random
import time
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card = {}
to_learn = {}

try:
    df = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("data/german.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = df.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    card_canvas.itemconfig(card_title, text="German", fill="black")
    card_canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    card_canvas.itemconfig(card_image, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    card_canvas.itemconfig(card_title, text="English", fill="white")
    card_canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    card_canvas.itemconfig(card_image, image=back_image)


def save_card():
    to_learn.remove(current_card)
    data = DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("ILEARN")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

card_canvas = Canvas(width=800, height=600)
card_image = card_canvas.create_image(400, 300, image=front_image)
card_title = card_canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
card_word = card_canvas.create_text(400, 300, text="", font=(FONT_NAME, 60, "bold"))
card_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(image=wrong_image, command=next_card, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_image, command=save_card, highlightthickness=0)
right_button.grid(column=1, row=1)

# to show first card on opening the program
next_card()

window.mainloop()
