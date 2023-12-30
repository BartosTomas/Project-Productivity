#                 __    ________
#                / _)  / Rooooo \
#        .-^^^-/ /     \ aaaar! /
#     __/       /       ¯¯¯¯¯¯¯¯
#    <__.|_|-|_|
# _/¯¯¯¯¯¯¯¯¯¯¯¯¯¯\_
import customtkinter
import tkinter 

class Page(customtkinter.CTk):
    def __init__(self, window):
        self.window = window
        self.page_setup()

    def page_setup(self):

        headding = customtkinter.CTkTextbox(master=self.window, font=("Helvetica", 75, "bold"))
        headding.grid(column= 3, row=0,columnspan = 7, pady = (20,0), sticky="EW")
        headding.insert("0.0", "Heading")

        textfield = customtkinter.CTkTextbox(master= self.window, font=("Helvetica", 24))
        textfield. grid(column= 3, row=1,columnspan = 7,pady = (20,0), sticky="SNEW")
        textfield.insert("0.0", "Text field")



        

