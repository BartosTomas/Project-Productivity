import customtkinter as ctk
import data
import save
import main

class Login_page():
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("900x450")
        self.window.title("Welcome")
        self.no_name = None
        self.wrong_password = None
        self.no_data = None
        self.exists = None
        self.diff_password = None
        self.setup()
        self.load_gui()
        self.window.mainloop()

    def setup(self):
        columns = (0, 1, 2)
        rows = (x for x in range(10))
        for column in columns:
            self.window.columnconfigure(column, weight = 1)
        for row in rows:
            self.window.rowconfigure(row, weight= 1)
        
        
    def load_gui(self):
        self.Label = ctk.CTkLabel(master = self.window, text = "Login or register")
        self.login = ctk.CTkButton(master = self.window, text = "Login", command = self.login_gui)
        self.register = ctk.CTkButton(master = self.window, text = "Register", command = self.register_gui)
        self.Label.grid(row = 1, column = 1)
        self.login.grid(row = 3, column = 1)
        self.register.grid(row = 5, column = 1)

    def register_gui(self):
        self.clear_menu()        

        self.username_entry = ctk.CTkEntry(master= self.window, placeholder_text= "username")
        self.password_entry = ctk.CTkEntry(master = self.window, placeholder_text= "password", show = "*")
        self.password_confirmation = ctk.CTkEntry(master = self.window, placeholder_text= "confirm password", show = "*")
        self.username_entry.grid(row = 3, column = 1)
        self.password_entry.grid(row = 5, column = 1)
        self.password_confirmation.grid(row = 6, column = 1)
        self.register_button = ctk.CTkButton(master = self.window, text = "register", command = self.register_check_in )
        self.register_button.grid(row  = 7, column = 1)
        self.back_button = ctk.CTkButton(master = self.window, text = "Back to menu", command= self.clear_menu)
        self.back_button.grid(row = 5, column = 2)
        self.window.mainloop()
    
    def register_check_in(self):
        if self.no_data != None:
                self.no_data.destroy()
        elif self.exists != None:
                self.exists.destroy()
        elif self.diff_password != None:
                self.diff_password.destroy()
        username = self.username_entry.get()
        password = self.password_entry.get()
        password_confirmation = self.password_confirmation.get()
        if username == '' and password == '' and password_confirmation == '':
            self.no_data = ctk.CTkLabel(master = self.window, text = "Please enter all informations")
            self.no_data.grid(row = 8, column = 1)
        elif username == '' or password == '' or password_confirmation == '':
            self.no_data = ctk.CTkLabel(master = self.window, text = "Please enter all informations")
            self.no_data.grid(row = 8, column = 1)
        elif username in data.Users:
            self.exists = ctk.CTkLabel(master = self.window, text = "Username already exists")
            self.exists.grid(row = 8, column = 1, sticky = "NW")
        elif password != password_confirmation:
            self.diff_password = ctk.CTkLabel(master = self.window, text = "Password doesn't match")
            self.diff_password.grid(row = 8, column = 1)
        else:
            data.Users[username] = password
            data.Logged_in = [username, password]
            save.Work_With_Data.Save_Data()
            self.window.destroy()
            main.main()

    
    def login_check_in(self):
        if self.no_name != None:
            self.no_name.destroy()
        if self.wrong_password != None:
            self.wrong_password.destroy()
        if self.no_data != None:
            self.no_data.destroy()
        username = self.username_login_entry.get()
        password = self.password_loggin_entry.get()
        if username == '' or password == '':
            self.no_data = ctk.CTkLabel(self.window, text = "Enter all informations")
            self.no_data.grid(row = 4, column = 1)
        elif username not in data.Users:
            self.no_name = ctk.CTkLabel(master = self.window, text = "No user named {}".format(username))
            self.no_name.grid(row = 4, column = 1)
            if data.Users[username]  != password:
                self.wrong_password = ctk.CTkLabel(master = self.window, text = "Wrong password")
                self.wrong_password.grid(row = 6, column = 1)
        else:
            data.Logged_in = [username, password]
            save.Work_With_Data.Save_Data()
            self.window.destroy()
            main.main()
    



    def login_gui(self):
        self.clear_menu()

        self.username_login_entry = ctk.CTkEntry(master= self.window, placeholder_text= "username")
        self.password_loggin_entry = ctk.CTkEntry(master = self.window, placeholder_text= "password", show = "*")
        self.username_login_entry.grid(row = 3, column = 1)
        self.password_loggin_entry.grid(row = 5, column = 1)
        self.login_button = ctk.CTkButton(master = self.window, text = "login", command = self.login_check_in)
        self.login_button.grid(row = 8, column = 1)
        self.back_button = ctk.CTkButton(master = self.window, text = "Back to menu", command= self.clear_menu)
        self.back_button.grid(row = 5, column = 2)
        self.window.mainloop()

    def clear_menu(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.load_gui()

        



if __name__ == "__main__":
    Login_page()