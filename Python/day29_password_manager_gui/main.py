from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

def search():
    try:
        with open("data1.json", "r") as data_file:
            retrieved_data = json.load(data_file)

    except:
        messagebox.showinfo(title="error", message="No data found")
    else:
        if website_input.get() in retrieved_data:
            email_info=retrieved_data[website_input.get()]["email"]
            password_info=retrieved_data[website_input.get()]["password"]
            messagebox.showinfo(title=f"{website_input.get()}", message=f"Email:{email_info}\nPassword:{password_info}")

        else:
            messagebox.showinfo(title="error",message=f"No details for {website_input.get()} exists")


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for letter in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for number in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    password_list = (password_letters + password_numbers + password_symbols)

    new_password = ""
    for n in range(len(password_list)):
        new_password += random.choice(password_list)

    password_input.insert(0,new_password)
    pyperclip.copy(new_password)



def input_save():
    website_entry=website_input.get()
    email_entry=email_input.get()
    password_entry=password_input.get()
    new_data={
        website_entry:{
            "email":email_entry,
            "password":password_entry,
        }
    }
    if len(website_entry)==0 or len(password_entry)==0:
        warning=messagebox.showinfo(title="warning/error",message="please dont leave any fields empty")
    else:
        #is_ok=messagebox.askokcancel(title="save information",message=f"for the website {website_entry}, you have entered email:{email_entry} and password:{password_entry}. do you wish to save it?")
        #if is_ok:
        try:
            with open("data1.json","r") as data_file:
                data=json.load(data_file)
        except:
            with open("data1.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("data1.json","w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            #data.write(f"{website_entry} | {email_entry} | {password_entry}\n")
            website_input.delete(0,END)
            password_input.delete(0,END)

windows=Tk()
windows.title("password manager")
windows.config(padx=50,pady=50,bg="white")

canvas=Canvas(width=200,height=200,bg="white",highlightthickness=0)
logo_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:",bg="white")
website_label.grid(column=0,row=1)

email_label=Label(text="E-mail/Username:",bg="white")
email_label.grid(column=0,row=2)

password_label=Label(text="Password:",bg="white")
password_label.grid(column=0,row=3)

website_input=Entry(width=21)
website_input.grid(column=1,row=1,columnspan=2)
website_input.focus()

email_input=Entry(width=35)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(0,"mohammed.rameeznb@gmail.com")

password_input=Entry(width=21)
password_input.grid(column=1,row=3)

generate_password_button=Button(text="Generate password",command=generate_password)
generate_password_button.grid(column=2,row=3)

add_button=Button(text="Add",width=36,command=input_save)
add_button.grid(column=1,row=4,columnspan=2)

search_button=Button(text="Search",width=13,command=search)
search_button.grid(column=2,row=1)



windows.mainloop()