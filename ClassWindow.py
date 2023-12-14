import customtkinter
import tkinter 
import tkinterDnD
import ClassPage


class Window:
    def __init__(self):
        customtkinter.set_ctk_parent_class(tkinterDnD.Tk)

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("green")
        
        window = customtkinter.CTk()
        window.geometry("1600x900")
        window.title("page1")
        for column in range(3):
            window.columnconfigure(column, weight=1)
        
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=3)
        
        ClassPage.Page(window)
        window.mainloop()

if __name__ == "__main__":
    Window()