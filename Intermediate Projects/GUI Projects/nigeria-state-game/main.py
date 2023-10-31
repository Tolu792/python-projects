import turtle
import pandas

screen = turtle.Screen()
screen.title(" Nigeria States game")
image = "blank_states_img_nigeria.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("36_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 37:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/37 states guessed", prompt="Guess the 37 states in "
                                                                                             "Nigeria").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
