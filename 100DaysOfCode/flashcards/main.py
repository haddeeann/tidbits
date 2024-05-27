from tkinter import *

window = Tk()
window.title('Flashcards')
bg_color = 'lightblue'
window.config(bg=bg_color, padx=50, pady=50)

card_front = Canvas(width=850, height=550, highlightthickness=0, bg=bg_color)
card_front_img = PhotoImage(file='./images/card_front.png')
card_front.create_image(425, 275, image=card_front_img)
card_front.grid(column=0, row=0)

forward = Canvas(width=100, height=100, highlightthickness=0, bg=bg_color)
forward_img = PhotoImage(file='./images/next_small.png')
forward.create_image(50, 50, image=forward_img)
forward.grid(column=1, row=0)

window.mainloop()