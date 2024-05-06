from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# work minutes 25
WORK_MIN = 25
# break minutes 5
SHORT_BREAK_MIN = 5
# long break minutes 20
LONG_BREAK_MIN = 20
reps = 0
max_reps = 7
reps_check = ''
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    global reps_check
    global reps
    reps = 0
    reps_check = ''
    check.config(text=reps_check)
    window.after_cancel(timer)
    label.config(text='Timer')
    canvas.itemconfig(timer_text, text=f"{WORK_MIN:02d}:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global reps_check
    work = False
    if reps == max_reps:
        label.config(text=f"BREAK", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        label.config(text=f"WORK {round(reps/2) + 1}", fg=GREEN)
        # minutes * 60
        count_down(WORK_MIN * 60)
        work = True
    else:
        label.config(text=f"BREAK", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    if not work:
        reps_check += '✔'
        check.config(text=reps_check)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    time_text = f"{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=time_text)

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    elif reps <= max_reps:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35))
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text=f"{WORK_MIN:02d}:00", fill='white', font=(FONT_NAME, 35, 'bold'))

canvas.grid(column=1, row=1)

start = Button(text='Start', bg=YELLOW, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text='Reset', bg=YELLOW, command=reset_timer)
reset.grid(column=2, row=2)

check = Label(bg=YELLOW, fg=GREEN)
check.grid(column=1, row=3)

window.mainloop()
