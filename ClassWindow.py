import customtkinter
import tkinter 
import ClassPage
import welcome_page


class Window:
    def __init__(self, page):
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("green")
        
        window = customtkinter.CTk()
        window.geometry("1600x900")
        window.title("page1")
        for column in range(10):
            window.columnconfigure(column, weight=1)
        
        window.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight= 10)

        if page == "welcome_page":
            welcome_page.Welcome_page(window)
        elif page == "new_page":  
            ClassPage.Page(window)

        window.mainloop()

if __name__ == "__main__":
    Window(page = "welcome_page")