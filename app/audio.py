from libs import pydubLib
from utils import utils

# Class for audio files
# @author Sandun Munasinghe
# @since 6/7/2024
class Audio:
    
    def __init__(self, fileName, srcFilePath, dstFilePath, targetVolumeLevel = utils.targetDbfsLevelDefault):
        self.fileName = fileName
        self.srcFilePath = srcFilePath
        self.dstFilePath = dstFilePath
        self.targetVolumeLevel = targetVolumeLevel
        self.audioInfo = pydubLib.getAudioInfo(srcFilePath, fileName)
        self.updatedAudio = None
    
    # Prints the technical info of the audio file        
    #
    # @author Sandun Munasinghe
    # @since 6/7/2024
    def printInfo(self):
        def convertAudioDuration():
            durationInMiliseconds = len(self.audioInfo)
            totalSeconds = durationInMiliseconds / 1000
            minutes = totalSeconds / 60
            remainingSeconds = totalSeconds % 60
            return {
                "minutes" : str(int(minutes)),
                "seconds" : str(int(remainingSeconds))
            }
                
        convertedSongDuration = convertAudioDuration()
        
        utils.println("-------------Song Info------------")
        utils.println("Duration = " + convertedSongDuration["minutes"] + " Minutes " + convertedSongDuration["seconds"] + " Seconds ")
        utils.println("Loudness in dbfs = " + str(self.audioInfo.dBFS))
        utils.println("Loudness in  rms = " + str(self.audioInfo.rms))
        utils.println("Max Loudness = " + str(self.audioInfo.max))
        utils.println("Max Loudness dbfs = " + str(self.audioInfo.max_dBFS))
        
        utils.println("---------------------------")
    
    # Normalizes the audio and exports the file
    #
    # @author Sandun Munasinghe
    # @since 6/7/2024
    def normalizeVolume(self):
        self.updatedAudio = pydubLib.normalizeAudio(self.audioInfo)
        
    def export(self):
        pydubLib.exportAudioFile(self.updatedAudio, self.dstFilePath, self.fileName)
                