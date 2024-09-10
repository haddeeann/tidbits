from tkinter import *
import pandas
from PIL import Image, ImageTk

df = pandas.read_csv('./data/french_words.csv')
french_dict = df.to_dict('records')
len_french_dict = len(french_dict)
print(len_french_dict)
window = Tk()
window.title('Flashcards')
bg_color = 'lightblue'
window.config(bg=bg_color, padx=50, pady=50)
FONT_NAME = "Courier"

first_english = ''
language = "French"
card_number = 0
button_column = 2

# card canvas setup
card_canvas = Canvas(width=850, height=550, highlightthickness=0, bg=bg_color)
card_front_img = PhotoImage(file='./images/card_front.png')
card_canvas.create_image(425, 275, image=card_front_img)
text_id = card_canvas.create_text(425, 250, text=french_dict[card_number][language], fill='black', font=(FONT_NAME, 45, 'bold'))
card_canvas.grid(column=1, row=1, rowspan=2)

def next_card():
    global text_id
    global language
    global card_number
    if card_number < len_french_dict:
        card_number += 1
    else:
        card_number = 0
    card_canvas.delete(text_id)
    text_id = card_canvas.create_text(425, 250, text=french_dict[card_number][language], fill='black',
                                      font=(FONT_NAME, 45, 'bold'))

def previous_card():
    global text_id
    global language
    global card_number
    if card_number == 0:
        card_number = len_french_dict - 1
    else:
        card_number -= 1
    card_canvas.delete(text_id)
    text_id = card_canvas.create_text(425, 250, text=french_dict[card_number][language], fill='black',
                                      font=(FONT_NAME, 45, 'bold'))

# Load and resize the image using Pillow
next_image_lg = Image.open('./images/next.png')
resized_image = next_image_lg.resize((50, 50), Image.ANTIALIAS)  # Resize the image to 50x50
next_img = ImageTk.PhotoImage(resized_image)

# Create the button with the resized image
Button(
    window,
    image=next_img,
    command=next_card,
).grid(column=button_column, row=0)

# back button
back_image_lg = Image.open('./images/back.png')
resized_image = back_image_lg.resize((50, 50), Image.ANTIALIAS)  # Resize the image to 50x50
back_img = ImageTk.PhotoImage(resized_image)

# Create the button with the resized image
Button(
    window,
    image=back_img,
    command=previous_card
).grid(column=button_column, row=1)


def flip_card():
    global text_id
    global language
    global card_number
    if language == "French":
        card_canvas.delete(text_id)
        text_id = card_canvas.create_text(425, 250, text=french_dict[card_number]["English"], fill='black', font=(FONT_NAME, 45, 'bold'))
        language = "English"
    elif language == "English":
        card_canvas.delete(text_id)
        text_id = card_canvas.create_text(425, 250, text=french_dict[card_number]["French"], fill='black', font=(FONT_NAME, 45, 'bold'))
        language = "French"


# flip button
flip_image_lg = Image.open('./images/flip.png')
resized_image = flip_image_lg.resize((50, 50), Image.ANTIALIAS)  # Resize the image to 50x50
flip_img = ImageTk.PhotoImage(resized_image)

flip_button = Button(width=50, height=50, image=flip_img, bg=bg_color, command=flip_card)
flip_button.grid(column=button_column, row=2)

def trash_card():
    pass

# trash can
trash_image_lg = Image.open('./images/trash.png')
resized_image = trash_image_lg.resize((50, 50), Image.ANTIALIAS)  # Resize the image to 50x50
trash_img = ImageTk.PhotoImage(resized_image)

trash_button = Button(width=50, height=50, image=trash_img, bg=bg_color, command=trash_card)
trash_button.grid(column=button_column, row=3)

window.mainloop()
