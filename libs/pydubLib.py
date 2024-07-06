from pydub import AudioSegment

targetDbfsLevel = -11.5

def println(text):
    print(text + "\n")

def getSongInfo(filePath):
    println("Reading " + filePath)
    return AudioSegment.from_mp3(filePath)
    

def convertSongDuration(durationInMiliseconds):
    totalSeconds = durationInMiliseconds / 1000
    minutes = totalSeconds / 60
    remainingSeconds = totalSeconds % 60
    return {
        "minutes" : str(int(minutes)),
        "seconds" : str(int(remainingSeconds))
    }
    
    
def printSongInfo(songInfo):
    convertedSongDuration = convertSongDuration(len(songInfo))
    
    println("-------------Song Info------------")
    println("Duration = " + convertedSongDuration["minutes"] + " Minutes " + convertedSongDuration["seconds"] + " Seconds ")
    println("Loudness in dbfs = " + str(songInfo.dBFS))
    println("Loudness in  rms = " + str(songInfo.rms))
    println("Max Loudness = " + str(songInfo.max))
    println("Max Loudness dbfs = " + str(songInfo.max_dBFS))
    
    println("---------------------------")
    
def normalizeAudio(songInfo, exportFilePath):
    dbfsDifference = targetDbfsLevel - songInfo.dBFS
    if dbfsDifference != 0:
        # should normalize
        println("Normalizing")
        normalizedAudio = songInfo.apply_gain(dbfsDifference)
        normalizedAudio.export(exportFilePath)
        println("Successfully exported to " + exportFilePath)
    else:
        println("volume is already normalized at " + str(targetDbfsLevel) + "dbfs")    
    

    
    