THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.score=self.quiz.score
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label=Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)

        self.canvas=Canvas(width=300,height=250,bg="white")
        self.create_text=self.canvas.create_text(150,125,width=280,text="here",font=("Arial", 20, "italic"),fill=THEME_COLOR)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)


        self.right_image=PhotoImage(file="./images/true.png")
        self.right_button=Button(image=self.right_image,highlightthickness=0,command=self.right_button_pressed)
        self.right_button.grid(column=0,row=2)

        self.wrong_image=PhotoImage(file="./images/false.png")
        self.wrong_button=Button(image=self.wrong_image,highlightthickness=0,command=self.wrong_button_pressed)
        self.wrong_button.grid(column=1,row=2)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.score_label.config(text=f"Score:{self.quiz.score}")
            self.canvas.itemconfig(self.create_text,text=q_text)
        else:

            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            self.window.after(1000,self.canvas.itemconfig(self.create_text,text=f"Quiz Over!\nyour final score:{self.quiz.score}"))



    def right_button_pressed(self):
        answer=self.quiz.check_answer("True")
        self.give_feedback(answer)

    def wrong_button_pressed(self):
        answer=self.quiz.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self,answer):
        if answer:
            self.canvas.config(bg="green")
            #self.window.after(1000,self.canvas.itemconfig(bg="green"))
        else:
            #self.window.after(1000,self.canvas.itemconfig(bg="red"))
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)




