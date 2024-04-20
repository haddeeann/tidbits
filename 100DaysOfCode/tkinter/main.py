import tkinter

window = tkinter.Tk()
window.title('New Gui Program')
window.minsize(width=500, height=300)

my_label = tkinter.Label(text='happiness is this right here.', font=("Arial", 24, "bold"))
my_label.pack()






window.mainloop()