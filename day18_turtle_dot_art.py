import turtle
from turtle import Turtle,Screen
import random

pointer=Turtle()
screen=Screen()

#####################
# triangles to decagon
#colors=["red","blue","yellow","black","green","orange","violet","indigo"]
# number_of_sides=[3,4,5,6,7,8,9,10]
# for i in range(len(number_of_sides)):
#     angle=(360/number_of_sides[i])
#     pointer.color(colors[i])
#     for i in range(number_of_sides[i]):
#         pointer.forward(100)
#         pointer.right(angle)

turtle.colormode(255)
# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     return (r,g,b)

#random walk with random colors
# direction=[0,90,180,270]
# pointer.pensize(10)
#pointer.speed("fastest")
# for i in range(200):
#     pointer.color(random_color())
#     pointer.forward(30)
#     pointer.setheading(random.choice(direction))

#spirograph
# gap=int(input("how much gap needed:"))
# for i in range(int(360/gap)):
#     pointer.color(random_color())
#     pointer.circle(100)
#     pointer.setheading(pointer.heading()+gap)
#
#Hirst painting
import colorgram#
import math
def color():
    rgb = first_color.rgb
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    return (red,green,blue)

colors=colorgram.extract('hirst spot painting.jpg',20)
c=[]
for i in range(len(colors)):
    first_color=colors[i]
    c.append(color())

screen.screensize(500,500)
pointer.penup()
pointer.goto(-300,-270)
pointer.pendown()
number_of_dots=100
number_of_rows=round(math.sqrt(number_of_dots))
max_row=0
is_print=True
while is_print:
    for i in range(number_of_rows):
        pointer.dot(20,random.choice(c))
        pointer.penup()
        pointer.forward(20)
        pointer.color(random.choice(c))
        pointer.forward(20)
        pointer.pendown()
    max_row+=1
    x = pointer.xcor()
    y = pointer.ycor()
    pointer.penup()
    pointer.goto(-300,y+40)
    pointer.pendown()
    if max_row==number_of_rows:
        pointer.hideturtle()
        is_print=False










screen.exitonclick()