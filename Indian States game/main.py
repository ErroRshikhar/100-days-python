import turtle
import pandas as pd
import os

# Setup screen
screen = turtle.Screen()
screen.title("Indian States & UTs Game")

# Add India Map
image = "blank_india_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load CSV
data = pd.read_csv("india_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Game loop
while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/{len(all_states)} Correct",
        prompt="Enter the name of the Indian state or UT (or type 'Exit' to quit):"
    )

    if not answer_state:
        continue

    answer_state = answer_state.title()

    # Exit and save missing
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pd.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    # Correct guess
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, align="center", font=("Arial", 8, "normal"))
