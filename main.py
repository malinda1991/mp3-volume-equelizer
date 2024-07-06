import traceback
import os

from libs import pydubLib


try:
    
    if not os.path.exists("volume-normalized"):
        os.makedirs("volume-normalized")
    
    exportPath = "volume-normalized"
    
    song = pydubLib.getSongInfo("audio/Green Day  21 Guns Lyrics.mp3")
    pydubLib.printSongInfo(song)
    pydubLib.normalizeAudio(song, exportPath + "/Green Day  21 Guns Lyrics-normalized.mp3")
    song2 = pydubLib.getSongInfo("audio/Lionel Richie  Endless Love ft Shania Twain.mp3")
    pydubLib.printSongInfo(song2)
    pydubLib.normalizeAudio(song2, exportPath + "/Lionel Richie  Endless Love ft Shania Twain-normalized.mp3")
    song3 = pydubLib.getSongInfo("audio/Marc Anthony Tina Arena  I Want to Spend My Lifetime Loving You.mp3")
    pydubLib.printSongInfo(song3)
    pydubLib.normalizeAudio(song3, exportPath + "/Marc Anthony Tina Arena  I Want to Spend My Lifetime Loving You-normalized.mp3")
    
except Exception as e:
    print("Error occurred", e)
    traceback.print_exc()