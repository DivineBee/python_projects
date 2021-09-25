import turtle
import pandas

screen = turtle.Screen()
screen.title("US STATES GAME!")
screen.setup(725, 491)
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

guessed_states = []
while len(guessed_states) <= 50:
    answer_state = (screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="Whats another state name?")).title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

# def get_mouse_click_coord(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coord)
# turtle.mainloop()