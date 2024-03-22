import turtle
import pandas

ALIGN = 'center'
FONT = ('Arial', 10, 'normal')

screen = turtle.Screen()
screen.title("US States Game")

image = 'blank_states_img.gif'
file = './50_states.csv'
screen.addshape(image)
data = pandas.read_csv(file)
all_states = data.state.to_list()

turtle.shape(image)
state_len = 50
while state_len > 0:
    answer = screen.textinput(title='Guess the state', prompt='what is another state?')
    if answer.lower() in (state.lower() for state in all_states):
        row = data[data.state == answer]
        if not row.empty:
            x = row.x.iloc[0]
            y = row.y.iloc[0]
            t = turtle.Turtle()
            t.hideturtle()
            t.color('blue')
            t.penup()
            t.goto(x, y)
            t.write(row.state.item(), align=ALIGN, font=FONT)
turtle.mainloop()