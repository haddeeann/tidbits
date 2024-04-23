from tkinter import *

window = Tk()
window.title('New Gui Program')
window.minsize(width=500, height=300)

my_label = Label(text='happiness is this right here.', font=("Arial", 24, "bold"))
my_label.pack()

my_label['text'] = 'Could be happier'


# button
def button_clicked():
    answer = input_field.get()
    my_label['text'] = answer


# entry
input_field = Entry(width=10)
input_field.pack()

button = Button(text='goodness', command=button_clicked)
button.pack()

window.mainloop()
