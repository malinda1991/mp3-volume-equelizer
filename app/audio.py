from libs import pydubLib
from utils import utils

# Class for audio files
# @author Sandun Munasinghe
# @since 6/7/2024
class Audio:
    
    def __init__(self, fileName, srcFilePath, dstFilePath, targetVolumeLevel):
        self.fileName = fileName
        self.srcFilePath = srcFilePath
        self.dstFilePath = dstFilePath
        self.targetVolumeLevel = utils.targetDbfsLevelDefault
        self.audioInfo = pydubLib.getAudioInfo(srcFilePath, fileName)
        self.updatedAudio = None
        
        if targetVolumeLevel != "":
            utils.println("Setting volume to "+targetVolumeLevel)        
            self.targetVolumeLevel = float(targetVolumeLevel)
        else:
            utils.println("No target volume level is given, continues on default volume level "+str(utils.targetDbfsLevelDefault))
    
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
    
    # Normalizes the audio
    #
    # @author Sandun Munasinghe
    # @since 6/7/2024
    def normalizeVolume(self):
        self.updatedAudio = pydubLib.normalizeAudio(self.audioInfo, self.targetVolumeLevel)
    
    # Exports the updated audio to a file
    #
    # @author Sandun Munasinghe
    # @since 6/7/2024    
    def export(self):
        if not self.updatedAudio is None:
            pydubLib.exportAudioFile(self.updatedAudio, self.dstFilePath, self.fileName)
        else:
            utils.println("No audio file to export")

    # Fades out the volume at the end of the audio file
    #
    # @author Sandun Munasinghe
    # @since 7/7/2024               
    def fadeOutAtEnd(self):
        durationInSeconds = 8
        self.updatedAudio = pydubLib.fadeOut(self.updatedAudio, durationInSeconds)
        