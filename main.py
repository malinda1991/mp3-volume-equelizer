import traceback

from app import Audio
from utils import utils

# main function

exportPath = "volume-normalized"

try:
    
    currentDir = utils.getCurrentDirectory()
    
    audioFileNames = utils.getMp3FilesInDirectory(currentDir)
    
    if len(audioFileNames) > 0:
        targetDbfs = input("Target volume level in dbfs : default "+str(utils.targetDbfsLevelDefault)+" - ")
        utils.createDirectory(exportPath)
        
        for fileName in audioFileNames:
            song = Audio(fileName, currentDir, exportPath, targetDbfs)
            song.printInfo()
            song.normalizeVolume()
            song.export()
    
except Exception as e:
    print("Error occurred", e)
    traceback.print_exc()