import LoginPage
import customtkinter as ctk
import data
from save import Work_With_Data as WWD
import time


class main:
    def __init__(self):

        self.page_list = []
        self.warning = None
        self.window = ctk.CTk()
        self.window.geometry("1600x900")
        self.window.title("App")
        self.page_texts = []
        self.new_page_substitute = None
        self.main_window_setup()
        self.widget_placeholder()
        self.window.mainloop()

    
    def main_window_setup(self):
        for row in range(10):
            if row == 0:
                self.window.rowconfigure(row, weight = 1)
            elif row == 9:
                self.window.rowconfigure(row, weight = 1)
            else:
                self.window.rowconfigure(row, weight = 4)
        for column in range(3):
            if column == 0:
                self.window.columnconfigure(column, weight= 2)
            elif column == 2 or column == 3 or column == 4:
                self.window.columnconfigure(column, weight = 2)
            else:
                self.window.columnconfigure(column, weight = 5)
        
    def widget_placeholder(self):
        self.account = ctk.CTkButton(master = self.window, text = "account", command = self.account_setup)
        self.account.grid(row = 0, column = 3, sticky = "NW")
        self.exit_button = ctk.CTkButton(self.window, text = "exit", command = self.exit)
        self.exit_button.grid(row = 0, column = 3)
        self.scroll_frame = ctk.CTkScrollableFrame(self.window, label_text= "Pages")
        self.scroll_frame.grid(row = 3, column = 0)
        for page in data.Text_fields:
            button = ctk.CTkButton(self.scroll_frame, text = page, command = lambda name = page: self.existing_page_setup(name))
            button.pack(pady = 10)
        self.delete_page_button = ctk.CTkButton(self.window, text = "Delete page", command = self.delete_page)
        self.delete_page_button.grid(row = 4, column = 0)
        self.title = ctk.CTkLabel(master = self.window, text = "HOME PAGE", font = ("Helvetica", 57, "bold"))
        self.title.grid(row = 0, column = 1)
        self.text_box = ctk.CTkTextbox(self.window)
        self.text_box.grid(row = 1, column = 1, rowspan = 6, sticky = "NSEW")
        self.create_page = ctk.CTkButton(self.window, text = "New Page", command = self.new_page)
        self.create_page.grid(row = 1, column = 0)
        self.save_button = ctk.CTkButton(self.window, text = "Save data", command = self.save_data)
        self.save_button.grid(row = 3, column = 3)
    
       
        
    def save_data(self):
        name = self.title.cget("text")
        text = self.text_box.get("1.0", "end-1c")
        data.Text_fields[name] = text
        WWD.Save_Data()
    
    
    def delete_page(self):
        self.page_name_del = ctk.CTkEntry(self.window, placeholder_text= "Enter page name")
        self.page_name_del.grid(row = 4, column = 0)
        self.confirm_del_button = ctk.CTkButton(self.window, text = "Confirm", command = self.delete_page_substitute)
        self.confirm_del_button.grid(row = 5, column = 0)

    

    def new_page(self):
        self.page_name = ctk.CTkEntry(self.window, placeholder_text= "Enter page name")
        self.page_name.grid(row = 1, column = 0)
        self.confirm_button = ctk.CTkButton(self.window, text = "Confirm", command = self.create_page_substitute)
        self.confirm_button.grid(row = 2, column = 0)

    
    def delete_page_substitute(self):
        name = self.page_name_del.get()
        del data.Text_fields[name]
        WWD.Save_Data()
        self.page_name_del.destroy()
        self.confirm_del_button.destroy()
        for widget in self.scroll_frame.winfo_children():
            if widget._text == name:
                widget.destroy()
                self.title.destroy()
        self.home_page()

    
    def home_page(self):
        self.title = ctk.CTkLabel(master = self.window, text = "HOME PAGE", font = ("Helvetica", 57, "bold"))
        self.title.grid(row = 0, column = 1)
        self.text_box = ctk.CTkTextbox(self.window)
        self.text_box.grid(row = 1, column = 1, rowspan = 6, sticky = "NSEW")

    
    def create_page_substitute(self):
        name = self.page_name.get()
        self.page_name.destroy()
        self.confirm_button.destroy()
        self.new_page_substitute = ctk.CTkButton(self.scroll_frame, text = name, command = lambda m = name : self.new_page_setup(m))
        self.new_page_substitute.pack(pady = 10)
        data.Text_fields[name] = ""
        WWD.Save_Data()
    
    def existing_page_setup(self, name):
        self.title.destroy()
        self.title = ctk.CTkLabel(self.window, text = name, font = ("Helvetica", 60, "bold"))
        self.title.grid(row = 0, column = 1)
        self.text_box = ctk.CTkTextbox(self.window)
        self.text_box.grid(row = 1, column = 1, rowspan = 6, sticky = "NSEW")
        self.text_box.insert(text = data.Text_fields[name], index = "1.0")


    def new_page_setup(self, name):
        self.title.destroy()
        self.title = ctk.CTkLabel(self.window, text = name, font = ("Helvetica", 60, "bold"))
        self.title.grid(row = 0, column = 1)
        self.text_box = ctk.CTkTextbox(self.window)
        self.text_box.grid(row = 1, column = 1, rowspan = 6, sticky = "NSEW")
        self.text_box.insert(text = data.Text_fields[name], index = "1.0")
        self.page_list.append(name)
        data.pages.append(self.text_box.get("1.0", "end-1c"))

    def account_setup(self):
        self.del_widgets()
        self.title.destroy()
        self.title = ctk.CTkLabel(self.window, text = "Account settings", font = ("Helvetica", 57, "bold"))
        self.title.grid(row = 0, column = 1)
        self.username = ctk.CTkLabel(self.window, text = "Username:",font = ("Helvetica", 20, "bold"))
        self.username.grid(row = 2, column = 1, sticky = "W")
        self.display_username = ctk.CTkLabel(self.window, text = data.Logged_in[0], font = ("Helvetica", 20, "bold"))
        self.display_username.grid(row = 2, column = 1)
        self.change_username = ctk.CTkButton(self.window, text = "Change username", command = self.change_username_func)
        self.change_username.grid(row = 2, column = 1, sticky = "E")
        self.change_password = ctk.CTkButton(self.window, text = "Change password", command = self.change_password_func)
        self.change_password.grid(row = 3, column = 1, sticky = "E")
        self.sign_out = ctk.CTkButton(self.window, text = "Sign out", command = self.sign_out_gui)
        self.sign_out.grid(row = 3, column = 1)
        self.delete_account = ctk.CTkButton(self.window, text = "Delete account", command = self.delete_account_func)
        self.delete_account.grid(row = 3, column = 1, sticky = "W")
        self.back_button = ctk.CTkButton(self.window, text = "Go back", command = self.del_widgets)
        self.back_button.grid(row = 4, column = 1)

    def delete_account_func(self):
        name = data.Logged_in[0]
        password = data.Logged_in[1]
        del data.Users[name]
        data.Logged_in = []
        data.Text_fields = {}
        WWD.Save_Data()
        self.window.destroy()
        LoginPage.Login_page()
    
    def del_widgets(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        self.widget_placeholder()
    
    def sign_out_gui(self):
        self.popup_box = ctk.CTk()
        self.popup_box.geometry("400x250")
        self.popup_box.title("Sign out")
        for row in range(2):
            self.popup_box.rowconfigure(row, weight = 1)
        for column in range(3):
            self.popup_box.columnconfigure(column, weight= 1)
        question = ctk.CTkLabel(self.popup_box, text = "Are you sure?", font = ("Helvetica", 20, "bold"))
        question.grid(row = 0, column = 1)
        yes = ctk.CTkButton(self.popup_box, text = "YES", command = self.YES)
        yes.grid(row = 1, column = 0)
        no = ctk.CTkButton(self.popup_box, text = "NO", command = self.NO)
        no.grid(row = 1, column = 2)
        self.popup_box.mainloop()
    
    def YES(self):
        self.exit()
        self.window.destroy()
        self.popup_box.destroy()
        LoginPage.Login_page()
    
    def NO(self):
        self.popup_box.destroy()

    
    def change_username_func(self):
        self.change_window = ctk.CTk()
        self.change_window.geometry("400x250")
        self.change_window.title("Change username")
        for row in range(3):
            self.change_window.rowconfigure(row, weight = 1)
        self.change_window.columnconfigure(0, weight= 1)

        self.new_name = ctk.CTkEntry(self.change_window, placeholder_text= "New username")
        self.new_name.grid(row = 0, column = 0)
        self.confirm_name = ctk.CTkEntry(self.change_window, placeholder_text= "Confirm name")
        self.confirm_name.grid(row = 1, column = 0)

        self.confirm_button = ctk.CTkButton(self.change_window, text = "Confirm", command = self.confirm)
        self.confirm_button.grid(row = 2, column = 0, sticky = "e")

        self.cancel = ctk.CTkButton(self.change_window, text = "Cancel", command = self.change_window.destroy)
        self.cancel.grid(row = 2, column = 0, sticky = "w")

        self.change_window.mainloop()

    def confirm(self):
        if self.warning != None:
            self.warning.destroy()
        if self.new_name.get() == "" or self.confirm_name.get() == "":
            self.warning = ctk.CTkLabel(self.change_window, text = "Please enter name", font = ("Helvetica", 15, "bold"))
            self.warning.grid(row = 1, column = 0, sticky = "S")
        elif self.new_name.get() in data.Users:
            self.warning = ctk.CTkLabel(self.change_window, text = "Name in use", font = ("Helvetica", 15, "bold"))
            self.warning.grid(row = 1, column = 0, sticky = "S")
        elif self.new_name.get() != self.confirm_name.get():
            self.warning = ctk.CTkLabel(self.change_window, text = "Name does not match", font = ("Helvetica", 15, "bold"))
            self.warning.grid(row = 1, column = 0, sticky = "S")
        else:
            data.Users[self.new_name.get()] = data.Users[self.display_username._text]
            del data.Users[self.display_username._text]
            data.Logged_in[0] = self.new_name.get()
            WWD.Save_Data()
            self.display_username.configure(text = self.new_name.get())
            self.change_window.destroy()
        


    def change_password_func(self):
        self.change_window = ctk.CTk()
        self.change_window.geometry("400x250")
        self.change_window.title("Change password")
        for row in range(3):
            self.change_window.rowconfigure(row, weight = 1)
        self.change_window.columnconfigure(0, weight= 1)

        self.new_password = ctk.CTkEntry(self.change_window, placeholder_text= "New password", show = "*")
        self.new_password.grid(row = 0, column = 0)
        self.confirm_password_entry = ctk.CTkEntry(self.change_window, placeholder_text= "Confirm password", show = "*")
        self.confirm_password_entry.grid(row = 1, column = 0)

        self.confirm_button = ctk.CTkButton(self.change_window, text = "Confirm", command = self.confirm_password)
        self.confirm_button.grid(row = 2, column = 0, sticky = "e")

        self.cancel = ctk.CTkButton(self.change_window, text = "Cancel", command = self.change_window.destroy)
        self.cancel.grid(row = 2, column = 0, sticky = "w")

        self.change_window.mainloop()
        
    def confirm_password(self):
        if self.warning != None:
            self.warning.destroy()
        if self.new_password.get() == "" or self.confirm_password_entry.get() == "":
            self.warning = ctk.CTkLabel(self.change_window, text = "Please enter password", font = ("Helvetica", 15, "bold"))
            self.warning.grid(row = 1, column = 0, sticky = "S")
        elif self.new_password.get() == data.Logged_in[1] or self.confirm_password_entry.get() == data.Logged_in[1]:
            self.warning = ctk.CTkLabel(self.change_window, text = "Password already in use", font = ("Helvetica", 15, "bold"))
            self.warning.grid(row = 1, column = 0, sticky = "S")
        elif self.new_password.get() != self.confirm_password_entry.get():
            self.warning = ctk.CTkLabel(self.change_window, text = "Password does not match", font = ("Helvetica", 15, "bold"))
            self.warning.grid(row = 1, column = 0, sticky = "S")
        else:
            data.Logged_in[1] = self.confirm_password_entry.get()
            data.Users[data.Logged_in[0]] = self.confirm_password_entry.get()
            WWD.Save_Data()
            self.change_window.destroy()

    def exit(self):
        for i in data.pages:
            self.save_data()
        self.window.destroy()
    
    def auto_save(self):
        for i in data.pages:
            self.save_data()


if __name__ == "__main__":
    main()
