import data

class Create_Image_Source:      #Class that creates image source key in "Image_src" dictionary in "data.py" script
    
    def __init__(self, key: str, value: str):
        if key not in data.Image_src:       #Checks if key exists 
            data.Image_src[key] = value

class Remove_Image_Source:      #Class that deletes existing image source from "Image_src" dictionary in "data.py"

    def __init__(self, key: str):
        if key in data.Image_src:       #Checks if key exists (prevents key error)
            del data.Image_src[key]
