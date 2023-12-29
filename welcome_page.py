import customtkinter
import data
import ClassWindow

class Welcome_page():
    def __init__(self, window):


        self.window = window
        self.wrong_log_in = None
        self.user_exists = None

        self.Welcome_text = customtkinter.CTkLabel(master = self.window, text = "Welcome ! \n Sign in if you already have an account \n Or sign up if you are new here !", font = ("Helvetica", 20, "bold"))
        self.Welcome_text.grid(column = 0, row = 4, pady = 20, sticky = "N")

        self.sign_in_text = customtkinter.CTkLabel(master = self.window, text = "Sign in:", font = ("Helvetica", 15, "bold"))
        self.sign_in_text.grid(column = 6, row = 2)

        self.username = customtkinter.CTkEntry(master = self.window, placeholder_text= "username", corner_radius = 10)
        self.username.grid(column = 6, row = 3)
        self.password = customtkinter.CTkEntry(master = self.window, placeholder_text= "password", corner_radius= 10, show = "*" )
        self.password.grid(column = 6, row = 4, sticky = "N")

        self.sign_up_text = customtkinter.CTkLabel(master = self.window, text = "Sign up:", font = ("Helvetica", 15, "bold"))
        self.sign_up_text.grid(column = 6, row = 5, sticky = "S")

        self.sign_up_username = customtkinter.CTkEntry(master = self.window, placeholder_text= "username", corner_radius = 10)
        self.sign_up_username.grid(column = 6, row = 6)
        self.sign_up_password = customtkinter.CTkEntry(master = self.window, placeholder_text= "password", corner_radius = 10, show = "*")
        self.sign_up_password.grid(column = 6, row = 7, sticky = "N")

        self.log_in = customtkinter.CTkButton(master = self.window, text = "Log in", corner_radius= 10, command = self.Check_login)
        self.log_in.grid(column = 6, row = 4, pady = 50, sticky = "N")
        self.sign_up = customtkinter.CTkButton(master = self.window, text = "Sign up", corner_radius= 10, command = self.Sign_up)
        self.sign_up.grid(column = 6, row = 7,pady = 50, sticky = "N")
        self.window.mainloop()
    
    def Check_login(self):
        if self.wrong_log_in != None:
            self.wrong_log_in.destroy()
        username = self.username.get()
        password = self.password.get()
        if username in data.Users:
            if data.Users[username] != password:
                self.wrong_log_in = customtkinter.CTkLabel(master = self.window, text = "Wrong username or password", font = ("Helvetica", 10))
                self.wrong_log_in.grid(column = 6, row = 4, pady = 55)
            else:
                self.window.destroy()
                ClassWindow.Window("new_page")
        else:
            self.wrong_log_in = customtkinter.CTkLabel(master = self.window, text = "Username does not exist", font = ("Helvetica", 10))
            self.wrong_log_in.grid(column = 6, row = 4, pady = 55)
        
    def Sign_up(self):
        if self.user_exists != None:
            self.user_exists.destroy()
        username = self.sign_up_username.get()
        password = self.sign_up_password.get()
        if username == "" or password == "":
            pass
        else:
            if username in data.Users:
                self.user_exists = customtkinter.CTkLabel(master = self.window, text = "Username already exists", font = ("Helvetica", 10))
                self.user_exists.grid(column = 6, row = 7, pady = 55)
            else:
                data.Users[username] = password
                from save import Work_With_Data as WD
                WD.Save_Data()
                self.window.destroy()
                ClassWindow.Window("new_page")
    
    