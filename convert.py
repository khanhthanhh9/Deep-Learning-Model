from os import path
from pydub import AudioSegment
import os
from pathlib import Path
import pydub


# AudioSegment.ffmpeg = os.getcwd()+"\\ffmpeg\\bin\\ffmpeg.exe"
# print (AudioSegment.ffmpeg)
#
# print(AudioSegment.ffmpeg)
# mypaths = os.getenv('PATH').split(';')  # replace 'PATH' by 'your search path' if needed.
#
# for i in mypaths:
#     if i.find('python'):
#         print(i)
#
# print("Current cwd")
# print(os.getcwd())

# # files
# src = "\\bsb.mp3"
# dst = "test.wav"
#
#
# pydub.AudioSegment.converter = os.getcwd()+ "\\ffmpeg.exe"
# pydub.AudioSegment.ffprobe   = os.getcwd()+ "\\ffprobe.exe"
#
# # \
# # convert wav to mp3
import glob
all = glob.glob("*.mp3")
dst = 'test.wav'
global s
for fileName in all:
    # Only split the last ., because song name can have . inside it
    fileNameBeforeTxt = fileName.rsplit('.',1)[0]
    print(fileNameBeforeTxt)
    sound = AudioSegment.from_mp3(fileName)
    sound.export(f"{fileNameBeforeTxt}.wav", format="wav")
    # DELETE .MP3
    os.remove(fileName)
    print(f"Deleted {fileName}")
# sound = AudioSegment.from_mp3('bsb.mp3')
# sound.export(dst, format="wav")