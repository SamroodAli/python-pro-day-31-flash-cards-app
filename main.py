from tkinter import Tk, PhotoImage, Canvas, Button, N

# ---------------------------- UI COLORS AND FONT ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.minsize(height=750, width=900)
window.config(bg=BACKGROUND_COLOR)

# Canvas widget
FRONT_IMAGE = PhotoImage(file="images/card_front.png")
front_image_canvas = Canvas(height=600, width=900, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image_canvas.create_image(450, 300, image=FRONT_IMAGE)
front_image_canvas.grid(column=0, row=0, columnspan=4,sticky=N)

# Wrong Button
WRONG_IMAGE = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=WRONG_IMAGE, borderwidth=0, highlightthickness=0, bd= 0)
wrong_button.grid(column=0, row=1)

# Right Button
RIGHT_IMAGE = PhotoImage(file="images/right.png")
right_button = Button(image=RIGHT_IMAGE, borderwidth=0, highlightthickness=0, bd= 0)
right_button.grid(column=3, row=1)

window.mainloop()
