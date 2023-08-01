from PIL import ImageGrab, Image # Allows us to get the image from clibpard
import time # Let's us wait before executing another line of code
import easygui # Let's you choose file directory
import os.path # Let's us check inside a text file or folder

if os.path.isfile("./filedir.txt") == False or os.stat("filedir.txt").st_size == 0:  # Checks if filedir.txt exists or if it's empty
    filedir = open("filedir.txt", "w") # Opens filedir.txt in "write" mode (This also creates filedir.txt)
    path = easygui.diropenbox() # Opens up a GUI to select a folder
    filedir.write(f"{path}\image.png") # Writes the path that you selected to filedir.txt
    filedir.close() # Closes filedir.txt
    
print("Saving Image...") # Displays that it's saving the image in the terminal
img = ImageGrab.grabclipboard() # Grabs image from clipboard

if isinstance(img, Image.Image) == False: # Checks if clipboard has an image
    print("You do not have an image saved in your clipboard.") # Tells the user that they don't have an image in the clibpard
    time.sleep(1) # Waits one second
    quit() # Closes the program
else:
    filedir = open("filedir.txt", "r") # Opens filedir.txt in read mode
    img.save(filedir.read()) # Saves image in the path located in filedir.txt
    print("Image saved") # Displays that the image was saved in the terminal
    time.sleep(1) # Waits one second
    quit() # Exits the program after waiting 1 second