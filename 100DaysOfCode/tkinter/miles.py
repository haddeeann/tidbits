from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.config(padx=10, pady=10)

i = Entry()
i.grid(row=0, column=1)

miles_label = Label(text='Miles')
miles_label.grid(row=0, column=2)

equal = Label(text='is Equal to')
equal.grid(row=1, column=0)

km_label = Label(text='Km')
km_label.grid(row=1, column=2)


def calculate():
    miles_input = float(i.get())
    output = miles_input * 1.609344
    print(output)
    output_label = Label(text=output)
    output_label.grid(row=1, column=1)


button = Button(text='Calculate', command=calculate)
button.grid(row=2, column=1)

window.mainloop()
