import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name ?").title()
    # If answer_state is one of the states in all states of the 50_states.csv
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        # If it is correct guess
        guessed_states.append(answer_state)
        # Creating a turtle to write the name at the given coordinate
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        state_data = data[data.state == answer_state]
        tim.goto(state_data.x.item(), state_data.y.item())
        tim.write(answer_state)


