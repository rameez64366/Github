from turtle import Turtle,Screen
def forwards():
    pointer.forward(10)
def backwards():
    pointer.backward(10)

def clockwise():
    new_heading=pointer.heading()+10
    pointer.setheading(new_heading)

def counter_clockwise():
    new_heading = pointer.heading() - 10
    pointer.setheading(new_heading)

def clear():
    pointer.clear()
    pointer.penup()
    pointer.home()
    pointer.pendown()


pointer=Turtle()
screen=Screen()
screen.listen()
screen.onkeypress(forwards,"w")
screen.onkeypress(backwards,"s")
screen.onkeypress(clockwise,"a")
screen.onkeypress(counter_clockwise,"d")
screen.onkeypress(clear,"c")

















screen.exitonclick()