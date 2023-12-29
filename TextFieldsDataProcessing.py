import data

class Create_Text_Field:      #Creates new key in "Text_fields" dictionary in "data.py" script
    
    def Create_field(self, key, value): 
        if self.Check_key(key) == False:
            data.Text_fields[key] = value
    
    def Check_key(self,key):
        if key in data.Text_fields:
            return True
        else:
            return False

class Rewrite_Text_Fields_data:     #Rewrites existing data in "Text_fields" Dictionary in "Data.py" script
    
    def __init__(self, key : str, new_val: str):
        if data.Text_fields[key] == new_val:        #Checks if the old value of a key is equal to new one. If does, then it won´t rewrite the key value
            return None
        else:
            data.Text_fields[key] = new_val         #Rewrites the value of a key

class Remove_Text_Field:        #Deletes a text field from "Text_fields" dictionary in "data.py" script

    def __init__(self, key: str):
         if key in data.Text_fields:     #Checks if the key exists (prevention from key error)
            del data.Text_fields[key]

class Load_data:

    def Load(key : str):
        if key in data.Text_fields:
            return data.Text_fields[key]