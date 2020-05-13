from os.path import isfile, exists
import os
import shutil


def makeFolders():
    foldersNeeded = ['Documents', 'Pictures'] # Just add whatever folders are required here 
    for folder in foldersNeeded:
        if(not exists(folder)):
            os.mkdir(folder)

def sortFiles():
    files = [f for f in os.listdir() if isfile(f)]
    for file in files:
        if (file.endswith('.pdf') or file.endswith('.docx')):
            shutil.move(file, 'Documents')
        elif (file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg')):
            shutil.move(file, 'Pictures')


if __name__ == "__main__":
    path = "/home/manantaneja/Downloads"
    os.chdir(path)
    makeFolders() ## need to run this only once or when you require a new folder
    sortFiles()

