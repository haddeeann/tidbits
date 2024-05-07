from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, bg=PINK)

canvas = Canvas(width=200, height=200, bg=PINK, highlightthickness=0)
padlock_img = PhotoImage(file='logo.png')
canvas.create_image(200, 200, image=padlock_img)

window.mainloop()
