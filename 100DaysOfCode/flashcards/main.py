from tkinter import *
import pandas

df = pandas.read_csv('./data/french_words.csv')
french_dict = df.to_dict('records')
window = Tk()
window.title('Flashcards')
bg_color = 'lightblue'
window.config(bg=bg_color, padx=50, pady=50)
FONT_NAME = "Courier"

pairs = {
    "hola": "hi",
    "feliz": "happy"
}

first_english = ''
# for translation in french_dict:
#     print(translation["French"], ': ', translation["English"])

language = "French"
card_number = 0
card_canvas = Canvas(width=850, height=550, highlightthickness=0, bg=bg_color)
card_front_img = PhotoImage(file='./images/card_front.png')
card_canvas.create_image(425, 275, image=card_front_img)
text_id = card_canvas.create_text(425, 250, text=french_dict[card_number][language], fill='black', font=(FONT_NAME, 45, 'bold'))
card_canvas.grid(column=0, row=0, rowspan=3)

def next_card():
    global text_id
    global language
    global card_number
    card_number += 1
    card_canvas.delete(text_id)
    text_id = card_canvas.create_text(425, 250, text=french_dict[card_number][language], fill='black',
                                      font=(FONT_NAME, 45, 'bold'))


img = PhotoImage(file='./images/next_small.png')
Button(
    window,
    image=img,
    command=next_card
).grid(column=1, row=0)


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



flip_img = PhotoImage(file='./images/flip.png')
flip_button = Button(width=100, height=100, image=flip_img, bg=bg_color, command=flip_card)
flip_button.grid(column=1, row=1)

trash_canvas = Canvas(width=100, height=100, highlightthickness=0, bg=bg_color)
trash_img = PhotoImage(file='./images/trash.png')
trash_canvas.create_image(50, 50, image=trash_img)
trash_canvas.grid(column=1, row=2)

window.mainloop()
