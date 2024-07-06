import traceback

from app import Audio
from utils import utils

# main function

exportPath = "volume-normalized"
sourcePath = "songs"

try:
    
    utils.createDirectory(exportPath)
    
    audioFileNames = utils.listFilesInDirectory(sourcePath)
    
    for fileName in audioFileNames:
        song = Audio(fileName, sourcePath, exportPath, utils.targetDbfsLevelDefault)
        song.printInfo()
        song.normalizeVolume()
    
except Exception as e:
    print("Error occurred", e)
    traceback.print_exc()