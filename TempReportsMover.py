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
    print(f'Moving "{file}" from "{sourceFolder}" to "{destinationFolder}"')
    
    # os.rename won't work since we're moving to other drives while shutil.move is drive agnostic.
    shutil.move(f"{sourceFolder}/{file}", f"{destinationFolder}/{file}")



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