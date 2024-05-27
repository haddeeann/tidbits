from tkinter import *

window = Tk()
window.title('Flashcards')
bg_color = 'lightblue'
window.config(bg=bg_color, padx=50, pady=50)
FONT_NAME = "Courier"

pairs = {
    "hola": "hi",
    "feliz": "happy"
}

first_spanish = ''
first_english = ''
for index, spanish in enumerate(pairs):
    print(index, spanish, pairs[spanish])
    first_spanish = spanish
    first_english = pairs[spanish]

card_canvas = Canvas(width=850, height=550, highlightthickness=0, bg=bg_color)
card_front_img = PhotoImage(file='./images/card_front.png')
card_canvas.create_image(425, 275, image=card_front_img)
card_canvas.create_text(425, 250, text=first_spanish, fill='black', font=(FONT_NAME, 45, 'bold'))
card_canvas.grid(column=0, row=0, rowspan=3)

forward_canvas = Canvas(width=100, height=100, highlightthickness=0, bg=bg_color)
forward_img = PhotoImage(file='./images/next_small.png')
forward_canvas.create_image(50, 50, image=forward_img)
forward_canvas.grid(column=1, row=0)


def flip_card():
    print('flip happiness')


flip_img = PhotoImage(file='./images/flip.png')
flip_button = Button(width=100, height=100, image=flip_img, bg=bg_color, command=flip_card)
flip_button.grid(column=1, row=1)

trash_canvas = Canvas(width=100, height=100, highlightthickness=0, bg=bg_color)
trash_img = PhotoImage(file='./images/trash.png')
trash_canvas.create_image(50, 50, image=trash_img)
trash_canvas.grid(column=1, row=2)

window.mainloop()
