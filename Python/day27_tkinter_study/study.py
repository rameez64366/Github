import tkinter
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    print(new_text)

windows=tkinter.Tk()
windows.title("My first GUI code")
windows.minsize(width=500,height=300)
windows.config(padx=100,pady=100) #### gives a padding which is space around widget. applicable to all widget functions


my_label=tkinter.Label(text="I am Rameez.",font=("Arial",24))
my_label.grid(column=0,row=0)

###########   Button     ##################
button=tkinter.Button(text="click me",command=button_clicked)
button.grid(column=1,row=1)

button2=tkinter.Button(text="new button")
button2.grid(column=2,row=0)
############## entry ##########
input=tkinter.Entry()
input.grid(column=3,row=2)
p=input.get()
print(p)


#
# new_entry=tkinter.Entry(width=30)
# new_entry.insert(tkinter.END, string="Some text to begin with.")
# #Gets text in entry
# new_entry.pack()
#
# text =tkinter.Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(tkinter.END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", tkinter.END))
# text.pack()
#
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = tkinter.Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = tkinter.IntVar()
# checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = tkinter.IntVar()
# radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = tkinter.Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

windows.mainloop()