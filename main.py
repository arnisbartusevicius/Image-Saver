from PIL import ImageGrab, Image # Allows us to get the image from clibpard
import time # Let's us wait before executing another line of code
import easygui # Let's you choose file directory
import os.path # Let's us check inside a text file or folder

if os.path.isfile("./filedir.txt") == False or os.stat("filedir.txt").st_size == 0:  # If filedir.txt doesn't exist or it's empty:
    filedir = open("filedir.txt", "w") # Opens filedir.txt in "write" mode (This also creates filedir.txt)
    path = easygui.diropenbox() # Opens up a GUI to select a folder
    filedir.write(f"{path}\image.png") # Writes the path that you selected to filedir.txt
    filedir.close() # Closes filedir.txt

while True: # This while statement runs forever; repeating the code
    img = ImageGrab.grabclipboard() # Grabs image from clipboard
    if isinstance(img, Image.Image) == False: # If clipboard doesn't have an image:
        time.sleep(1) # Waits one second
    else: # If clipboard has an image:
        filedir = open("filedir.txt", "r") # Opens filedir.txt in read mode
        img.save(filedir.read()) # Saves image in the path located in filedir.txt
        time.sleep(1) # Waits one second
