import os, glob, shutil, threading, json
from tkinter import E

logFolder = "log"
logFileName = "log.txt"

jsonFile = open("config.json", "r")
data = json.load(jsonFile)
jsonFile.close()

'''
Moves file from one location to another
@params
    file: a string representing the file name
'''
def moveFile(file):
    sourceFolder = data["sourceFolder"]
    destinationFolder = data["destinationFolder"]
    
    # os.rename won't work since we're moving to other drives while shutil.move is drive agnostic.
    try:
        shutil.move(f"{sourceFolder}/{file}", f"{destinationFolder}/{file}")
        print(f'Moved "{file}" from "{sourceFolder}" to "{destinationFolder}"')
    except FileNotFoundError as e:
        print(e)
        pass



'''
Scans the source directory for any files with the desired extension.
If a file is found, then it will be moved to the destination directory.
'''
def scan():
    os.chdir(data["sourceFolder"])
    for file in glob.glob("*." + data["fileExtension"]):
        moveFile(file)



# Main function
def main():
    threading.Timer(data["scanInterval"], main).start()
    scan()
    
main()