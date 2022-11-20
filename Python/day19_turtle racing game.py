from turtle import Turtle,Screen
import random
def racers():
    turtles = []
    for i in range(0,6):
        pointer = Turtle()
        pointer.penup()
        pointer.goto(coordinates[i])
        pointer.shape("turtle")
        pointer.color(colors[i])
        turtles.append(pointer)
    return turtles
screen=Screen()
colors=["red","violet","green","blue","yellow","orange"]
screen.setup(width=500, height=400)
coordinates=[(-230,60),(-230,30),(-230,0),(-230,-30),(-230,-60),(-230,-90)]
user_guess=screen.textinput(title="Turtle racing game",prompt="Which color turtle would win the race?: ").lower()
racers=racers()
turtle_speed = [0, 6, 1]
steps = [5, 10, 15]
winner=""
is_game=True
while is_game:
    for i in range(0, len(racers)):
        if racers[i].xcor() > 190:
            winner+=racers[i].pencolor()
            is_game=False
        racers[i].speed(random.choice(turtle_speed))
        racers[i].forward(random.choice(steps))

if user_guess==winner:
    print(f"Your choice win. Winning color: {winner} and your choice was: {user_guess}")
else:
    print(f"Your choice is wrong. Winning color: {winner} and your choice was: {user_guess}")

screen.exitonclick()
