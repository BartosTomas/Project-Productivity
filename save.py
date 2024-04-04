import data


class Work_With_Data:       #Class working with data

    def Save_Data():        #Function that saves new data to existing dictionary in "data.py" script
        new_dict = data.Text_fields
        new_users = data.Users
        new_logged = data.Logged_in
        new_pages = data.pages
        with open("data.py", "w") as f:         #Opens "data.py" for writing as "f" allowing the code to rewrite the file with the new dictionary
            f.writelines("Text_fields = " + str(new_dict) +"\n")        #Rewrites the "Text_fields" dictionary in "data.py" script 
            f.writelines("pages = " + str(new_pages) + "\n")
            f.writelines("Users = " + str(new_users) + "\n")    
            f.writelines("Logged_in = " + str(new_logged))