from tkinter import *

windows=Tk()

windows.title("Mile to Km converter")
windows.config(padx=20,pady=20)
def button_clicked():
    mile_value=float(entry1.get())
    convert=round(mile_value*1.609344)
    value.config(text=f"{convert}")

entry1=Entry(width=10)
entry1.grid(column=1,row=0)

label1=Label(text="Miles")
label1.grid(column=2,row=0)

label2=Label(text="is equal to")
label2.grid(column=0,row=1)

value=Label(text="0")
value.grid(column=1,row=1)

label3=Label(text="Km")
label3.grid(column=2,row=1)

button=Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=2)














windows.mainloop()