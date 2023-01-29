from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import Image
import customtkinter
import json
LENGTH=600
WIDTH=600
RED = "#e7305b"
DARKSEAGREEN4="#698B69"
YELLOW = "#f7f5dd"
BLACK="#000000"
GREY99="#FCFCFC"
MINT="#BDFCC9"
ANTIQUEWHITE="#FAEBD7"
MY_FRAME_COLOR=ANTIQUEWHITE
MY_BG_COLOR=GREY99
EXTRUDE_BG_COLOR=MINT

new_data={}

customtkinter.set_appearance_mode("Standard") # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green") # Themes: "blue" (standard), "green", "dark-blue"

class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Parameter setting GUI.py")
        self.geometry(f"{LENGTH}x{WIDTH}")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.create_widgets()

    def create_widgets(self):
        self.parameter_label = customtkinter.CTkLabel(self, text="Parameters",font=customtkinter.CTkFont(family='Times',size=22,weight="bold",slant="italic",underline=1))
        self.parameter_label.grid(row=0, column=0,columnspan=3,pady=10, padx=10, sticky="EW")

        self.sketching_frame = customtkinter.CTkFrame(self, width=WIDTH,height=500, corner_radius=10)
        self.sketching_frame.grid(row=1, column=0, rowspan=4, sticky="nsew")
        self.sketching_frame.columnconfigure(0,weight=1)
        self.sketching_frame.columnconfigure(1, weight=1)
        self.sketching_frame.columnconfigure(2, weight=1)

        self.sketching_label = customtkinter.CTkLabel(self.sketching_frame,anchor="w", text="Sketching parameters",font=customtkinter.CTkFont(family='Times',size=15,weight="bold",slant="roman",underline=1),text_color=DARKSEAGREEN4)
        self.sketching_label.grid(row=0, column=0, padx=10, sticky="W")
        self.sketch_plane_label = customtkinter.CTkLabel(self.sketching_frame,anchor="w", text="1. Select plane for sketch:",font=customtkinter.CTkFont(family='Times',size=10,weight="bold",slant="roman"))
        self.sketch_plane_label.grid(row=1, column=0,padx=10, sticky="W")

        self.radio_var = tkinter.IntVar(value=0)
        self.radio_button_XY = customtkinter.CTkRadioButton(master=self.sketching_frame,text="XY", variable=self.radio_var,value=1,command=self.plane_sketch_select)
        self.radio_button_XY.grid(row=2, column=0, padx=20, sticky="W")
        self.radio_button_YZ = customtkinter.CTkRadioButton(master=self.sketching_frame,text="YZ", variable=self.radio_var, value=2,command=self.plane_sketch_select)
        self.radio_button_YZ.grid(row=2, column=1,sticky="W")
        self.radio_button_XZ = customtkinter.CTkRadioButton(master=self.sketching_frame, text="XZ", variable=self.radio_var, value=3,command=self.plane_sketch_select)
        self.radio_button_XZ.grid(row=2, column=2,sticky="W")

        self.origin_coodinate_label = customtkinter.CTkLabel(self.sketching_frame, text="2. Sketch origin coordinate:",font=customtkinter.CTkFont(family='Times', size=10, weight="bold",slant="roman"))
        self.origin_coodinate_label.grid(row=3, column=0, padx=10, sticky="W")

        self.coodinate_label = customtkinter.CTkLabel(self.sketching_frame, text="Enter coordinate in x,y,z format:",font=customtkinter.CTkFont(family='Times', size=10,weight="bold", slant="italic"))
        self.coodinate_label.grid(row=4, column=0, padx=20, sticky="W")
        self.coodinate_entry = customtkinter.CTkEntry(self.sketching_frame,width=50)
        self.coodinate_entry.grid(row=4, column=1, sticky="W")

        self.rectangle_label = customtkinter.CTkLabel(self.sketching_frame, text="3.Dimensions of rectangle:",font=customtkinter.CTkFont(family='Times', size=10,weight="bold", slant="roman"))
        self.rectangle_label.grid(row=5, column=0, padx=10, sticky="W")
        self.rectangle_length_label = customtkinter.CTkLabel(self.sketching_frame, text="Length (in mm):",font=customtkinter.CTkFont(family='Times', size=10,weight="bold", slant="italic"))
        self.rectangle_length_label.grid(row=6, column=0, padx=50, sticky="W")
        self.rectangle_length_entry = customtkinter.CTkEntry(self.sketching_frame, width=50)
        self.rectangle_length_entry.grid(row=6, column=1, sticky="W")
        self.rectangle_height_label = customtkinter.CTkLabel(self.sketching_frame, text="Height (in mm):",font=customtkinter.CTkFont(family='Times', size=10,weight="bold", slant="italic"))
        self.rectangle_height_label.grid(row=7, column=0,padx=50, sticky="W")
        self.rectangle_height_entry = customtkinter.CTkEntry(self.sketching_frame, width=50)
        self.rectangle_height_entry.grid(row=7, column=1, sticky="W")

        self.rect_image=customtkinter.CTkImage(Image.open("length_breadth.jpg"),size=(315,160))
        self.rect_image_label=customtkinter.CTkLabel(self.sketching_frame, image=self.rect_image,text="")
        self.rect_image_label.grid(row=6,column=2,rowspan=2)

        self.Extrude_frame = customtkinter.CTkFrame(self, width=WIDTH, height=500, corner_radius=10)
        self.Extrude_frame.grid(row=8, column=0, rowspan=1, sticky="nsew")
        self.Extrude_frame.columnconfigure(0, weight=0)
        self.Extrude_frame.columnconfigure(1, weight=1)
        self.Extrude_frame.columnconfigure(2, weight=0)

        self.Extrusion_label = customtkinter.CTkLabel(self.Extrude_frame, anchor="w", text="Creation of 3D model",font=customtkinter.CTkFont(family='Times', size=15, weight="bold",slant="roman", underline=1),text_color=RED)
        self.Extrusion_label.grid(row=8, column=0, padx=10, sticky="W")
        self.Beam_width_label = customtkinter.CTkLabel(self.Extrude_frame, anchor="w",text="1. Beam extrusion width (in mm):",font=customtkinter.CTkFont(family='Times', size=10,weight="bold", slant="roman"))
        self.Beam_width_label.grid(row=9, column=0, padx=10, sticky="W")
        self.Beam_width_entry = customtkinter.CTkEntry(self.Extrude_frame, width=50)
        self.Beam_width_entry.grid(row=9, column=1, sticky="W")

        self.ok_frame = customtkinter.CTkFrame(self, width=WIDTH, height=100, corner_radius=10)
        self.ok_frame.grid(row=11, column=0, rowspan=4, sticky="nsew")
        self.ok_frame.columnconfigure(0, weight=1)
        self.ok_frame.columnconfigure(1, weight=1)
        self.ok_frame.columnconfigure(2, weight=1)
        self.button_1 = customtkinter.CTkButton(master=self.ok_frame, text="Add to model",command=self.click_button)
        self.button_1.grid(row=11,column=1,pady=10)
        self.button_2 = customtkinter.CTkButton(master=self.ok_frame, text="Confirm", command=self.check_click_button)
        self.button_2.grid(row=11, column=2, pady=10)

    def plane_sketch_select(self):
        val=self.radio_var.get()
        if val==1:
            self.radio_button_XZ.configure(state="DISABLED")
            self.radio_button_YZ.configure(state="DISABLED")
        elif val==2:
            self.radio_button_XY.configure(state="DISABLED")
            self.radio_button_XZ.configure(state="DISABLED")
        else:
            self.radio_button_XY.configure(state="DISABLED")
            self.radio_button_YZ.configure(state="DISABLED")
    def origin_coordinate_input(self):
        or_val=self.coodinate_entry.get()
    def Dimension_rectangle_input(self):
        length=self.rectangle_length_entry.get()
        height=self.rectangle_height_entry.get()

    def click_button(self):
        or_val=self.coodinate_entry.get()
        length = self.rectangle_length_entry.get()
        height = self.rectangle_height_entry.get()
        extrusion_length=self.Beam_width_entry.get()

    def check_click_button(self):
        val = self.radio_var.get()
        or_val = self.coodinate_entry.get()
        length = self.rectangle_length_entry.get()
        breadth = self.rectangle_height_entry.get()
        extrusion_length = self.Beam_width_entry.get()
        #print(val,len(or_val),len(length),len(breadth),len(extrusion_length))
        if len(or_val) == 0 or len(length)==0 or len(breadth)==0 or len(breadth) == 0 or len(extrusion_length)==0 or val==0:
                messagebox.showinfo(title="warning/error", message="please dont leave any fields empty")
        else:
            if len(or_val) < 5:
                messagebox.showinfo(title="warning/error", message="please input x,y,z format for coordinate")
            elif len(or_val) > 8:
                messagebox.showinfo(title="warning/error", message="please input x,y,z format for coordinate")
            else:
                self.coodinate_entry.delete(0,END)
                self.rectangle_length_entry.delete(0,END)
                self.rectangle_height_entry.delete(0,END)
                self.Beam_width_entry.delete(0,END)
                self.radio_button_XY.configure(state="DISABLED")
                self.radio_button_YZ.configure(state="DISABLED")
                self.radio_button_XZ.configure(state="DISABLED")
                self.radio_button_XY.deselect()
                self.radio_button_YZ.deselect()
                self.radio_button_XZ.deselect()
                list1 = or_val.split(",")
                converted_list = [int(i) for i in list1]
                new_data = {
                    "Parameters": {
                        "plane_select":val,
                        "origin_value": converted_list,
                        "Rectangle_length": float(length),
                        "Rectangle_height": float(breadth),
                        "Beam width": float(extrusion_length)
                    }
                }
                print(new_data)
                with open("parameter.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
                messagebox.showinfo(title="Successful",message="Model parameters are successfully added to the model. if you wish to change parameters the programm has to be restarted.")

if __name__ == "__main__":
    GUI = GUI()
    GUI.mainloop()


