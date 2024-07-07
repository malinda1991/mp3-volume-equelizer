import traceback

from app import Audio
from utils import utils

# main function

exportPath = "volume-normalized"
sourcePath = "songs"

try:
    
    targetDbfs = input("Target volume level in dbfs : default "+str(utils.targetDbfsLevelDefault)+" - ")
    
    utils.createDirectory(exportPath)
    
    audioFileNames = utils.getMp3FilesInDirectory(sourcePath)
    
    for fileName in audioFileNames:
        song = Audio(fileName, sourcePath, exportPath, targetDbfs)
        song.printInfo()
        song.normalizeVolume()
        song.export()
    
except Exception as e:
    print("Error occurred", e)
    traceback.print_exc()