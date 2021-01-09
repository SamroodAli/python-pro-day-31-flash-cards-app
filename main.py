from tkinter import Tk, PhotoImage, Canvas, Button, N

# ---------------------------- UI COLORS AND FONT ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Courier", 20, "italic")
WORD_FONT = ("Courier", 30, "bold")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.minsize(height=750, width=900)
window.config(bg=BACKGROUND_COLOR)

# Wrong Button
WRONG_IMAGE = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=WRONG_IMAGE, borderwidth=0, highlightthickness=0, bd= 0)
wrong_button.grid(column=0, row=1)

# Right Button
RIGHT_IMAGE = PhotoImage(file="images/right.png")
right_button = Button(image=RIGHT_IMAGE, borderwidth=0, highlightthickness=0, bd= 0)
right_button.grid(column=3, row=1)

# ---------------------------- NEW CARD ------------------------------- #
# Canvas widget
FRONT_IMAGE = PhotoImage(file="images/card_front.png")
BACK_IMAGE = PhotoImage(file="images/card_back.png")


def card_side(side, language, word):
    card_canvas = Canvas(height=600, width=900, highlightthickness=0, bg=BACKGROUND_COLOR)
    card_canvas.create_image(450, 300, image=side)
    card_canvas.grid(column=0, row=0, columnspan=4)

    # Language and word on card
    card_canvas.create_text(450, 150, text=f"{language}", font=FONT)
    card_canvas.create_text(450, 300, text=f"{word}", font=WORD_FONT)


def new_card():
    card_side(FRONT_IMAGE, "French", "Chambre")
    card_side(BACK_IMAGE, "English", "Bedroom")

# ---------------------------- APP LAUNCH AND LOOP ------------------------------- #
new_card()
window.mainloop()
