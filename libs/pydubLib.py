# Library for the pydub
from pydub import AudioSegment
from pydub.utils import mediainfo
from utils import utils

def getAudioInfo(path, fileName):
    filePath = utils.buildFilePath(path, fileName)
    utils.println("Reading " + filePath)
    return AudioSegment.from_mp3(filePath)

def getMediaInfo(path, fileName):
    filePath = utils.buildFilePath(path, fileName)
    return mediainfo(filePath)
        
def normalizeAudio(songInfo, targetDbfsLevel):
    dbfsDifference = targetDbfsLevel - songInfo.dBFS
    if dbfsDifference != 0:
        # should normalize
        utils.println("Normalizing")
        utils.println("Setting the volume level from " + str(songInfo.dBFS) + " to " + str(targetDbfsLevel))
        
        if dbfsDifference > 0:
            # makes audio louder
            utils.println("Increasing volume by "+ str(dbfsDifference))
        else:
            # makes audio quieter
            utils.println("Reducing volume by "+ str(dbfsDifference))
            
        return songInfo.apply_gain(dbfsDifference)

    else:
        utils.println("volume is already normalized at " + str(targetDbfsLevel) + "dbfs")    
        return None
    
def exportAudioFile(normalizedAudio, exportPath, exportFileName, exportFormat, exportBitrate):
    utils.println("Exporting audio in "+exportFormat+" format and at "+str(exportBitrate) + " bitrate")
    
    exportFilePath = utils.buildFilePath(exportPath, exportFileName)
    
    normalizedAudio.export(exportFilePath, format=exportFormat, bitrate=exportBitrate)
    
    utils.println("Successfully exported to " + exportFilePath)
    
def fadeOut(songInfo, durationInSeconds = 0):
    utils.println("Fading out for "+ str(durationInSeconds) + " seconds")
    durationInMiliseconds = durationInSeconds * 1000
    return songInfo.fade_out(durationInMiliseconds)
    

    
    