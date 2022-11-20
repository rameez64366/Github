import turtle
import pandas
screen=turtle.Screen()
screen.title("US states game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coord(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coord)
data_list=pandas.read_csv("50_states.csv")
state_list=data_list["state"].to_list()
guessed_list=[]
missed_state_list=[]


while len(guessed_list)<50:
    answer = screen.textinput(title=f"{len(guessed_list) + 1}/{len(state_list)} US states game",prompt="what is the state name:").title()
    if answer=="Exit":
        break
    if answer!=guessed_list:
        for state in state_list:
            if state==answer:
                new_turtle=turtle.Turtle()
                new_turtle.hideturtle()
                new_turtle.penup()
                x=int(data_list[data_list["state"]==answer]["x"])
                y = int(data_list[data_list["state"] == answer]["y"])
                new_turtle.goto(x,y)
                new_turtle.write(answer)
                guessed_list.append(answer)

location_x=[]
location_y=[]
for state in state_list:
    if state not in guessed_list:
        missed_state_list.append(state)
        x=data_list[data_list["state"]==state]["x"].item()
        y = data_list[data_list["state"] == state]["y"].item()
        location_x.append(x)
        location_y.append(y)


dictio={
    "state":missed_state_list,
    "x":location_x,
    "y":location_y
}

missed_list=pandas.DataFrame(dictio)
missed_list.to_csv("missed_list.csv")


