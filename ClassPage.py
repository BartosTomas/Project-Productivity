#                 __    ________
#                / _)  / Rooooo \
#        .-^^^-/ /     \ aaaar! /
#     __/       /       ¯¯¯¯¯¯¯¯
#    <__.|_|-|_|
# _/¯¯¯¯¯¯¯¯¯¯¯¯¯¯\_
import customtkinter
import tkinter 
<<<<<<< HEAD
=======
import tkinterDnD
>>>>>>> b1c1c78f2e64c3590a7dbb7c9cf44afc6f1626cd

class Page(customtkinter.CTk):
    def __init__(self, window):
        self.window = window
        self.page_setup()

    def page_setup(self):

        headding = customtkinter.CTkTextbox(master=self.window, font=("Helvetica", 75, "bold"))
<<<<<<< HEAD
        headding.grid(column= 3, row=0,columnspan = 7, pady = (20,0), sticky="EW")
        headding.insert("0.0", "Heading")

        textfield = customtkinter.CTkTextbox(master= self.window, font=("Helvetica", 24))
        textfield. grid(column= 3, row=1,columnspan = 7,pady = (20,0), sticky="SNEW")
=======
        headding.grid(column=1, row=0, sticky="EW")
        headding.insert("0.0", "Heading")

        textfield = customtkinter.CTkTextbox(master= self.window, font=("Helvetica", 24))
        textfield. grid(column= 1, row=1, sticky="SNEW")
>>>>>>> b1c1c78f2e64c3590a7dbb7c9cf44afc6f1626cd
        textfield.insert("0.0", "Text field")



        

