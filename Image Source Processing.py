import data

class Create_Image_Source:      #Function that creates image source key in "Image_src" dictionary in "data.py" script
    
    def __init__(self, key, value):
        if key not in data.Image_src:       #Checks if key exists 
            data.Image_src[key] = value
    