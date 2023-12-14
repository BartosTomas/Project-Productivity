import data


class Work_With_Data:       #Class working with data

    def Save_Data():        #Function that saves new data to existing dictionary in "data.py" script
        new_dict = data.Text_fields
        new_img = data.Image_src
        with open("data.py", "w") as f:         #Opens "data.py" for writing as "f" allowing the code to rewrite the file with the new dictionary
            f.writelines("Text_fields = " + str(new_dict) +"\n")        #Rewrites the "Text_fields" dictionary in "data.py" script
            f.writelines("Image_src = "+ str(new_img) + "\n")       #Rewrites the "Image_src" dictionary in "data.py" script
    
    def Clear_Data():   #Clears all data in every dictionary
        data.Text_fields = {}
        data.Image_src = {}

if __name__ == "__main__":
    import Text_Fields_Data_Processing as tw
    tw.Create_Text_Field("Name", "Ondra")
    Work_With_Data.Save_Data()
    import API
    API.API.Create_file()