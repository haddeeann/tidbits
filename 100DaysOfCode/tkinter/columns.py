from tkinter import *

# Creating a new window and configurations
# cant mix grid and pack in the same code

window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx=100, pady=100)

# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
# label.pack()
label.grid(column=0, row=0)


# Buttons
def action():
    print("Do something")


# calls action() when pressed
button1 = Button(text="Click Me row1 col1", command=action)
button1.grid(column=1, row=1)


# calls action() when pressed
button2 = Button(text="Click Me row0 col2", command=action)
button2.grid(column=2, row=0)

# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.grid(column=3, row=2)

window.mainloop()