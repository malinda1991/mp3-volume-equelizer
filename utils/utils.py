# Utility functions 
import os

targetDbfsLevelDefault = -11.4

def println(text):
    print(text + "\n")
    
def buildFilePath(path, fileName):
    return path + "/" + fileName

def listFilesInDirectory(dirPath):
    return os.listdir(dirPath)

def createDirectory(dirPath):
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)