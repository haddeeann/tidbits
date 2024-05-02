from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    time_text = f"{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=time_text)
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35))
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text=f"{WORK_MIN}:00", fill='white', font=(FONT_NAME, 35, 'bold'))

canvas.grid(column=1, row=1)

start = Button(text='Start', bg=YELLOW, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text='Reset', bg=YELLOW)
reset.grid(column=2, row=2)

check = Label(text='✔', bg=YELLOW, fg=GREEN)
check.grid(column=1, row=3)

window.mainloop()
