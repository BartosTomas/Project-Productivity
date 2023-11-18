import data


class WorkWithData: #Class working with data

    def SaveData(): #Function that saves new data to existing dictionary in "data.py" script
        new_dict = data.Text_fields
        with open("data.py", "w") as f:  #Opens "data.py" for writing as "f" allowing the code to rewrite the file with the new dictionary
            f.write("Text_fields = " + str(new_dict)) #Rewrites the file
    
    def RewriteData(key, new_val): #Function thjat rewrites existing data in "Text_fields" Dictionary in "Data.py" script
        if data.Text_fields[key] == new_val: #Checks if the old value of a key is equal to new one. If does, then it won´t rewrite the key value
            return
        else:
            data.Text_fields[key] = new_val #rewrites the value of a key


