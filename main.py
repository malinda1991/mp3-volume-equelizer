import traceback

from app import Audio
from utils import utils

class AppHeader:
    
    versionNumber = "1.3.0"
    
    @classmethod
    def printAppHeader(cls):
        utils.println("MP3 Volume Equelizer Version " + cls.versionNumber)
        utils.println("A simple volume equeliver based on Pydub Python library")
    

# main function

exportPath = "volume-normalized"

try:
    
    AppHeader.printAppHeader()
    
    currentDir = utils.getCurrentDirectory()
    
    audioFileNames = utils.getMp3FilesInDirectory(currentDir)
    
    if len(audioFileNames) > 0:
        targetDbfs = input("Target volume level in dbfs : default "+str(utils.targetDbfsLevelDefault)+" - ")
        utils.createDirectory(exportPath)
        
        for fileName in audioFileNames:
            song = Audio(fileName, currentDir, exportPath, targetDbfs)
            song.printInfo()
            song.normalizeVolume()
            song.fadeOutAtEnd()
            song.export()
    
except Exception as e:
    print("Error occurred", e)
    traceback.print_exc()