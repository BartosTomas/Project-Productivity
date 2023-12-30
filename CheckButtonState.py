import mouse

var = 0
while True:
    if mouse.is_pressed("left"):
        while mouse.is_pressed("left") == True:
            print("držíš mě") #funkce
            var = 1
    elif mouse.is_pressed("left") == False and var == 1 : 
        break





