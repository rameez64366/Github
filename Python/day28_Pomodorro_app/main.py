from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS=0
timer=NONE

def reset_timer():
    starting_label.config(text="Timer",fg=GREEN)
    windows.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    check_label.config(text="")
    global REPS
    REPS=0





def start_timer():
    global REPS
    REPS+=1

    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60


    if REPS%8==0:
        count_down(long_break_sec)
        starting_label.config(text="Long break",fg=RED)
    elif REPS%2==0:
        count_down(short_break_sec)
        starting_label.config(text="short break",fg=PINK)
    else:
        count_down(work_sec)
        starting_label.config(text="Work",fg=GREEN)


def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60

    if count_min<10:
        count_min=f"0{count_min}"
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=windows.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        working_session=math.floor(REPS/2)
        for _ in range(working_session):
            mark+="✔"
        check_label.config(text=mark)



windows=Tk()
windows.title("Pomodorro app")
windows.config(padx=100,pady=50,bg=YELLOW)

starting_label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"))
starting_label.grid(column=1,row=0)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_image=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_button=Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="reset",command=reset_timer)
reset_button.grid(column=2,row=2)

check_label=Label(bg=YELLOW,fg=GREEN)
check_label.grid(column=1,row=3)



windows.mainloop()









































































# # ---------------------------- TIMER RESET ------------------------------- #
# def stop_timer():
#     title_timer.config(text="Timer",fg=GREEN)
#     windows.after_cancel(timer)
#     canvas.itemconfig(timer_text,text="00:00")
#     check_label.config(text="")
#     global REPS
#     REPS=0
#
#
#
# # ---------------------------- TIMER MECHANISM ------------------------------- #
# def start_timer():
#     global REPS
#     REPS+=1
#
#     works_sec=WORK_MIN*60
#     short_break_sec=SHORT_BREAK_MIN*60
#     long_break_sec=LONG_BREAK_MIN*60
#
#     if REPS % 8 ==0:
#         count_down(long_break_sec)
#         title_timer.config(text="long break", fg=RED)
#     elif REPS % 2==0:
#         count_down(short_break_sec)
#         title_timer.config(text="short break", fg=PINK)
#     else:
#         count_down(works_sec)
#         title_timer.config(text="working time", fg=GREEN)
#
#




# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# def count_down(count):
#     count_min=math.floor(count/60)
#     count_sec=count%60
#     if count_min<10:
#         count_min=f"0{count_min}"
#     if count_sec<10:
#         count_sec=f"0{count_sec}"
#     canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
#     if count>0:
#         global timer
#         timer=windows.after(1000,count_down,count-1)
#     else:
#         start_timer()
#         mark = ""
#         work_session = math.floor(REPS / 2)
#         for _ in range(work_session):
#             mark += "✔"
#         check_label.config(text=mark)
# # ---------------------------- UI SETUP ------------------------------- #
# windows=Tk()
# windows.title("Pomodoro App")
# windows.config(padx=100,pady=50,bg=YELLOW)
#
# canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
# tomato_image=PhotoImage(file="tomato.png")
# canvas.create_image(100,112,image=tomato_image)
# timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
# canvas.grid(column=1,row=1)
#
#
#
# title_timer=Label(text="Timer",font=(FONT_NAME,35,"bold"),bg=YELLOW,fg=GREEN)
# title_timer.grid(column=1,row=0)
#
# start_button=Button(text="Start",command=start_timer)
# start_button.grid(column=0,row=2)
#
#
# stop_button=Button(text="Reset",command=stop_timer)
# stop_button.grid(column=2,row=2)
#
# check_label=Label(fg=GREEN,bg=YELLOW)
# check_label.grid(column=1,row=4)
#
#
# windows.mainloop()