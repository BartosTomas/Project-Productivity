#                 __    ________
#                / _)  / Rooooo \
#        .-^^^-/ /     \ aaaar! /
#     __/       /       ¯¯¯¯¯¯¯¯
#    <__.|_|-|_|
# _/¯¯¯¯¯¯¯¯¯¯¯¯¯¯\_
import customtkinter
import tkinter 
import tkinterDnD
import keyboard

class Page(customtkinter.CTk):
    def __init__(self, window):
        self.window = window
        self.page_setup()

    def page_setup(self):

        headding = customtkinter.CTkTextbox(master=self.window, font=("Helvetica", 75, "bold"))
        headding.grid(column=1, row=0, sticky="EW")
        headding.insert("0.0", "Heading")

        self.textfield = customtkinter.CTkTextbox(master= self.window, font=("Helvetica", 24))
        self.textfield. grid(column= 1, row=1, sticky="SNEW")
        self.textfield.insert("0.0", "Text field")



        

