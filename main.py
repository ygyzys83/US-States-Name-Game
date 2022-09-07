import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# already used the code below to create the 50_states.csv file with coordinates
# def get_mouse_coord(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_coord)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Guess a state name").title()
    print(answer_state)

    if answer_state == "Exit":
        # list comprehension:
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        save_file = pandas.DataFrame(missing_states)
        save_file.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # grab a specific row of data and assign a variable to it:
        state_data = data[data.state == answer_state]
        # now you tap into the attributes of this row/variable and tell t the turtle to go there
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        # t.write(state_data.state.item()) can also work


