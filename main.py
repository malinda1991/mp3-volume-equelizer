import traceback

from app import Audio
from utils import utils

# main function

exportPath = "volume-normalized"
sourcePath = "songs"

try:
    
    utils.createDirectory(exportPath)
    
    audioFileNames = utils.getMp3FilesInDirectory(sourcePath)
    # audioFileNames = [
    #     "Marc Anthony Tina Arena  I Want to Spend My Lifetime Loving You.mp3",
    #     "Lionel Richie  Endless Love ft Shania Twain.mp3",
    #     "Elvis Presley  Cant Help Falling In Love Official Audio.mp3"
    # ]
    
    for fileName in audioFileNames:
        song = Audio(fileName, sourcePath, exportPath, utils.targetDbfsLevelDefault)
        song.printInfo()
        song.normalizeVolume()
        song.export()
    
except Exception as e:
    print("Error occurred", e)
    traceback.print_exc()