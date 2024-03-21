import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = 'blank_states_img.gif'
states = './50_states.csv'
screen.addshape(image)
data = pandas.read_csv(states)
print(data)
turtle.shape(image)

answer_state = screen.textinput(title='Guess the state', prompt='what is another state?')

turtle.mainloop()