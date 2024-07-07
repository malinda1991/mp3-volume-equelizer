# Library for the pydub
from pydub import AudioSegment
from utils import utils

def getAudioInfo(path, fileName):
    filePath = utils.buildFilePath(path, fileName)
    utils.println("Reading " + filePath)
    return AudioSegment.from_mp3(filePath)
        
def normalizeAudio(songInfo, targetDbfsLevel):
    dbfsDifference = targetDbfsLevel - songInfo.dBFS
    if dbfsDifference != 0:
        # should normalize
        utils.println("Normalizing")
        utils.println("Setting the volume level from " + str(songInfo.dBFS) + " to " + str(targetDbfsLevel))
        return songInfo.apply_gain(dbfsDifference)

    else:
        utils.println("volume is already normalized at " + str(targetDbfsLevel) + "dbfs")    
        return None
    
def exportAudioFile(normalizedAudio, exportPath, exportFileName):
    utils.println("Exporting")
    exportFilePath = utils.buildFilePath(exportPath, exportFileName)
    normalizedAudio.export(exportFilePath)
    utils.println("Successfully exported to " + exportFilePath)
    

    
    