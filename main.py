"""Main project file"""
import random
from tkinter import Tk, PhotoImage, Canvas, Button
from data_fetcher import still_to_learn_words, front_heading, back_heading, write_csv
# ---------------------------- UI COLORS AND FONT ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Courier", 20, "italic")
WORD_FONT = ("Courier", 30, "bold")

# ---------------------------- WINDOW SETUP ------------------------------- #

window = Tk()
window.title("Flash Card App")
window.minsize(height=750, width=900)
window.config(bg=BACKGROUND_COLOR)

# ---------------------------- NEW CARD ------------------------------- #

FRONT_CARD_IMAGE = PhotoImage(file="images/card_front.png")
BACK_CARD_IMAGE = PhotoImage(file="images/card_back.png")


# Canvas widget
def card_side(side, language, word):
    """Card side function"""
    card_canvas = Canvas(height=600, width=900, highlightthickness=0, bg=BACKGROUND_COLOR)
    card_canvas.create_image(450, 300, image=side)
    card_canvas.grid(column=0, row=0, columnspan=4)

    # Language and word on card
    card_canvas.create_text(450, 150, text=f"{language}", font=FONT)
    card_canvas.create_text(450, 300, text=f"{word}", font=WORD_FONT)


# Saving next word and FLIP TIMER globally to remove if learned and to cancel window.after timer
NEW_WORD = None
FLIP_TIMER_ID = None


def new_card():
    """New card function"""
    global FLIP_TIMER_ID
    global NEW_WORD
    NEW_WORD = random.choice(still_to_learn_words)
    front_word = NEW_WORD[front_heading]
    back_word = NEW_WORD[back_heading]

    card_side(FRONT_CARD_IMAGE, f"{front_heading}", f"{front_word}")
    FLIP_TIMER_ID = window.after(2000, card_side, BACK_CARD_IMAGE,f"{back_heading}", f"{back_word}")


# ---------------------------- RIGHT AND WRONG EVENTS and BUTTONS ------------------------------- #

def on_right():
    """IF you got the card right"""
    global FLIP_TIMER_ID
    still_to_learn_words.remove(NEW_WORD)
    window.after_cancel(FLIP_TIMER_ID)
    new_card()


def on_wrong():
    """IF you got the card wrong"""
    write_csv()
    global FLIP_TIMER_ID
    window.after_cancel(FLIP_TIMER_ID)
    new_card()


# Wrong Button
WRONG_IMAGE = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=WRONG_IMAGE, borderwidth=0,highlightthickness=0, bd=0, command=on_wrong)
wrong_button.grid(column=0, row=1)

# Right Button
RIGHT_IMAGE = PhotoImage(file="images/right.png")
right_button = Button(image=RIGHT_IMAGE, borderwidth=0, highlightthickness=0, bd=0, command=on_right)
right_button.grid(column=3, row=1)

# ---------------------------- APP LAUNCH AND LOOP ------------------------------- #
new_card()
window.mainloop()
