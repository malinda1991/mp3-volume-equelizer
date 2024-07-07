# Library for the pydub
from pydub import AudioSegment
from utils import utils

def getAudioInfo(path, fileName):
    filePath = utils.buildFilePath(path, fileName)
    utils.println("Reading " + filePath)
    return AudioSegment.from_mp3(filePath)
        
def normalizeAudio(songInfo):
    dbfsDifference = utils.targetDbfsLevelDefault - songInfo.dBFS
    if dbfsDifference != 0:
        # should normalize
        utils.println("Normalizing")
        utils.println("Setting the volume level from " + str(songInfo.dBFS) + " to " + str(utils.targetDbfsLevelDefault))
        return songInfo.apply_gain(dbfsDifference)

    else:
        utils.println("volume is already normalized at " + str(utils.targetDbfsLevelDefault) + "dbfs")    
        return None
    
def exportAudioFile(normalizedAudio, exportPath, exportFileName):
    utils.println("Exporting")
    exportFilePath = utils.buildFilePath(exportPath, exportFileName)
    normalizedAudio.export(exportFilePath)
    utils.println("Successfully exported to " + exportFilePath)
    

    
    