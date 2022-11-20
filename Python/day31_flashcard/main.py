import pandas
from tkinter import *
from tkinter import messagebox
import random

GREEN = "#B1DDC6"
current_card={}
new_list={}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    new_list=original_data.to_dict(orient="records")
else:
    new_list = data.to_dict(orient="records")

def data_block():
    global current_card,timer
    windows.after_cancel(timer)
    current_card=random.choice(new_list)
    front_canvas.itemconfig(text1,text="French",fill="black")
    front_canvas.itemconfig(text2,text=f"{current_card['French']}",fill="black")
    front_canvas.itemconfig(initial_pic,image=front_image)
    timer = windows.after(3000,func=flip_card)

def flip_card():
    front_canvas.itemconfig(initial_pic,image=final_image)
    front_canvas.itemconfig(text1,text="English",fill="white")
    front_canvas.itemconfig(text2,text=f"{current_card['English']}",fill="white")

def is_known():
    new_list.remove(current_card)
    data = pandas.DataFrame(new_list)
    data.to_csv("data/words_to_learn", index=False)
    data_block()

windows=Tk()
windows.title("Flash card gui")
windows.config(padx=50,pady=50,bg=GREEN)

timer=windows.after(3000,func=flip_card)

front_canvas=Canvas(width=800,height=526,highlightthickness=0,bg=GREEN)
front_image=PhotoImage(file="images/card_front.png")
final_image = PhotoImage(file="images/card_back.png")

initial_pic=front_canvas.create_image(400,263,image=front_image)

text1=front_canvas.create_text(400,150,text="title",font=("Ariel",40,"italic"),fill="black")
text2=front_canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"),fill="black")
front_canvas.grid(column=0,row=0,columnspan=2)

wrong_image=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_image,highlightthickness=0,bg=GREEN,command=data_block)
wrong_button.grid(column=0,row=1)

right_image=PhotoImage(file="images/right.png")
right_button=Button(image=right_image,highlightthickness=0,bg=GREEN,command=is_known)
right_button.grid(column=1,row=1)

data_block()

windows.mainloop()