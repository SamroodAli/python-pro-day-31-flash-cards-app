from tkinter import Tk, PhotoImage, Canvas, Button, N
import pandas
import random
# ---------------------------- UI COLORS AND FONT ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Courier", 20, "italic")
WORD_FONT = ("Courier", 30, "bold")

# ---------------------------- WINDOW SETUP ------------------------------- #

window = Tk()
window.title("Flash Card App")
window.minsize(height=750, width=900)
window.config(bg=BACKGROUND_COLOR)


# ------------------------------------------- DATA ------------------------------------------- #

data = pandas.read_csv("data/french_words.csv")
french_data = data.French.to_list()
english_data = data.English.to_list()
print(french_data)
print(english_data)
# ---------------------------- NEW CARD ------------------------------- #

FRONT_IMAGE = PhotoImage(file="images/card_front.png")
BACK_IMAGE = PhotoImage(file="images/card_back.png")


# Canvas widget
def card_side(side, language, word):
    card_canvas = Canvas(height=600, width=900, highlightthickness=0, bg=BACKGROUND_COLOR)
    card_canvas.create_image(450, 300, image=side)
    card_canvas.grid(column=0, row=0, columnspan=4)

    # Language and word on card
    card_canvas.create_text(450, 150, text=f"{language}", font=FONT)
    card_canvas.create_text(450, 300, text=f"{word}", font=WORD_FONT)


def new_card():
    word_index = random.randint(0, len(french_data))
    english_word = english_data[word_index]
    french_word = french_data[word_index]
    card_side(FRONT_IMAGE, "French", f"{french_word}")
    window.after(2000, card_side, BACK_IMAGE, "English", f"{english_word}")


# ---------------------------- RIGHT AND WRONG EVENTS and BUTTONS ------------------------------- #

def on_right():
    new_card()


def on_wrong():
    new_card()


# Wrong Button
WRONG_IMAGE = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=WRONG_IMAGE, borderwidth=0, highlightthickness=0, bd=0, command=on_wrong)
wrong_button.grid(column=0, row=1)

# Right Button
RIGHT_IMAGE = PhotoImage(file="images/right.png")
right_button = Button(image=RIGHT_IMAGE, borderwidth=0, highlightthickness=0, bd=0, command=on_right)
right_button.grid(column=3, row=1)

# ---------------------------- APP LAUNCH AND LOOP ------------------------------- #
new_card()
window.mainloop()
