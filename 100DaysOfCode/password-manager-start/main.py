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
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=224, highlightthickness=0)
tomato_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=tomato_img)

canvas.grid(column=1, row=0)

# website input/label
website_label = Label(text='Website')
website_label.grid(column=0, row=1)

website_input = Entry(width=38, justify='left')
website_input.grid(column=1, row=1, columnspan=2)

# email input/label
email_label = Label(text='Email/Username')
email_label.grid(column=0, row=2)

email_input = Entry(width=38, justify='left')
email_input.grid(column=1, row=2, columnspan=2)

# password input/label
password_label = Label(text='Password')
password_label.grid(column=0, row=3)

password_input = Entry(width=21, justify='left')
password_input.grid(column=1, row=3)


def generate_password():
    pass


button = Button(text='Generate Password', command=generate_password)
button.grid(column=2, row=3)


def add_password():
    pass


button = Button(text='Add', command=add_password, width=36)
button.grid(column=1, row=4, columnspan=2)

window.mainloop()
