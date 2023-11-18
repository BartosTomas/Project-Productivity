import data

class Create_Text_Field:      #Creates new key in "Text_fields" dictionary in "data.py" script
    
    def __init__(self, key, value):     
         if key not in data.Text_fields:         #Checks if the key already exists. if yes, then it will not create new key
            data.Text_fields[key] = value

class Rewrite_Text_Fields_data:     #Rewrites existing data in "Text_fields" Dictionary in "Data.py" script
    
    def __init__(self, key, new_val):
        if data.Text_fields[key] == new_val:        #Checks if the old value of a key is equal to new one. If does, then it won´t rewrite the key value
            return
        else:
            data.Text_fields[key] = new_val         #Rewrites the value of a key

class Remove_Text_Field:        #Deletes a text field from "Text_fields" dictionary in "data.py" script

    def __init__(self, key):
         if key in data.Text_fields:     #Checks if the key exists (prevention from key error)
            del data.Text_fields[key]