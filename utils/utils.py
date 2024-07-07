# Utility functions 
import os

targetDbfsLevelDefault = -11.4

def println(text):
    print(text + "\n")
    
def buildFilePath(path, fileName):
    return path + "/" + fileName

def getMp3FilesInDirectory(dirPath):
    fileNames = []
    for filename in os.listdir(dirPath):
        if filename.endswith(".mp3"):
            fileNames.append(filename)
    
    println("Found " + str(len(fileNames)) + " MP3 files in the directory")
    return fileNames

def createDirectory(dirPath):
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)