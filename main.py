import turtle
from turtle import Turtle, Screen
import pandas

window = Screen()
window.title("U.S States Game")
window.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

guessed = []


states_data = pandas.read_csv("50_states.csv")
states_list = states_data["state"].to_list()
states_to_learn = states_list

while len(guessed) < 50:

    answer = window.textinput(title=f"{len(guessed)}/50 States Correct", prompt="What's another state's name?").title()

    if answer in states_list:
        selected_state = states_data[states_data.state == answer]
        name = Turtle()
        name.hideturtle()
        name.penup()
        name.goto(x=int(selected_state.x),y=int(selected_state.y))
        name.write(answer)
        guessed.append(answer)
    else:
        pass

    for state in states_to_learn:
        if state in guessed:
            states_to_learn.remove(state)

    missing_state = pandas.DataFrame(states_to_learn)
    missing_state.to_csv("States_to_Learn")

window.exitonclick()
