from tkinter import *
from tkinter import messagebox
import random_password
import pyperclip
import json
from json import JSONDecodeError

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ------------------------------ SEARCH PASSWORD ---------------------------------- #
def search_password():
    with open('data.json', 'r') as file:
        try:
            entries = json.load(file)
        except JSONDecoderError:
            print('Not a properly formatted json')
        else:
            website = website_input.get()
            if website in entries:
                combo = entries[website]
                email = combo['email']
                password = combo['password']
                messagebox.showinfo(message=f"Email: {email}\n"
                                            f"Password: {password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    generated_password = random_password.generate()
    password_input.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_input.get()
    email = email_input.get()
    user_password = password_input.get()

    if not website or not email or not user_password:
        messagebox.showinfo(message="Please enter text in website, email, and password!")
    else:
        isok = messagebox.askokcancel(title=website, message=f"Website: {website}\n"
                                                             f"Email: {email}\n"
                                                             f"Password: {user_password}\n"
                                                             f"Is it ok to save?")
        if isok:
            with open('data.json', 'w+') as read_file:
                try:
                    entries = json.load(read_file)
                except JSONDecodeError as e:
                    entries = {}

            entries[website] = {
                'email': email,
                'password': user_password
            }

            with open('data.json', 'w') as write_file:
                json.dump(entries, write_file, indent=4)
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)
col_width = 21

canvas = Canvas(width=200, height=224, highlightthickness=0)
tomato_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=tomato_img)

canvas.grid(column=1, row=0)

# website input/label
website_label = Label(text='Website')
website_label.grid(column=0, row=1)

# middle column input size
website_input = Entry(width=21, justify='left')
website_input.grid(column=1, row=1)
website_input.focus()

button = Button(width=col_width, text='Search', command=search_password)
button.grid(column=2, row=1)

# email input/label
email_label = Label(text='Email/Username')
email_label.grid(column=0, row=2)

email_input = Entry(width=38, justify='left')
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'pattee13@gmail.com')

# password input/label
password_label = Label(text='Password')
password_label.grid(column=0, row=3)

# middle column input size
password_input = Entry(width=col_width, justify='left')
password_input.grid(column=1, row=3)

button = Button(text='Generate Password', command=generate_password)
button.grid(column=2, row=3)

button = Button(text='Add', command=add_password, width=36)
button.grid(column=1, row=4, columnspan=2)

window.mainloop()
