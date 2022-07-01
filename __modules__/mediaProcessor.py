#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dmytrenko.o
"""
import sys
stdOutput = open("outlog.log", "w")
sys.stderr = stdOutput
sys.stdout = stdOutput

import os
from scipy.io import wavfile
import moviepy.editor as mp
import shutil

def name_time_stamp(timeStamp, audioDuration):
    start_hours = int(timeStamp/3600)
    start_mins = int(timeStamp/60)
    start_sec = int(timeStamp%60)
    end_hours = int((timeStamp+audioDuration)/3600)
    end_mins = int((timeStamp+audioDuration)/60)
    end_sec = int((timeStamp+audioDuration)%60)
    name = "{0}_{1}_{2}__{3}_{4}_{5}".format(start_hours, start_mins, start_sec, end_hours, end_mins, end_sec)
    timeStamp += audioDuration
    return name, timeStamp
    

def audio2parts(audiosDir, audioDuration):
    timeStamp = 0
    for file_ in os.listdir(audiosDir+'full_audios/'):
        samplerate, data = wavfile.read(audiosDir+'full_audios/'+file_)
        print ('Samplerate {0}'.format(samplerate))
        totalSize = len(data)
        ChunkSize = samplerate*audioDuration #1 minute has 60 sec
        amountChunk = int(totalSize/ChunkSize)
        
        for i in range(amountChunk):
            chunkData = data[i*ChunkSize:i*ChunkSize+ChunkSize]
            name, timeStamp = name_time_stamp(timeStamp, audioDuration)
            wavfile.write(audiosDir+str(name)+'.wav', samplerate, chunkData)
    shutil.rmtree(audiosDir+'full_audios/')
    return

def video2wav(videosDir, audiosDir):
    if os.path.exists(audiosDir):
        shutil.rmtree(audiosDir)
    if not os.path.exists(audiosDir):
            print ("Directory {0} don't exist!".format(audiosDir))
            print ("Creating {0} directory...".format(audiosDir))
            os.mkdir(audiosDir)
            print ("Directory {0} was created seccsesfuly!".format(audiosDir))   
    fullAudioDir = audiosDir+'full_audios/'
    if not os.path.exists(fullAudioDir):
        print ("Directory {0} don't exist!".format(fullAudioDir))
        print ("Creating {0} directory...".format(fullAudioDir))
        os.mkdir(fullAudioDir)
        print ("Directory {0} was created seccsesfuly!".format(fullAudioDir))
    for file_ in os.listdir(videosDir):
        if (file_.endswith(".avi") or file_.endswith(".mp4")):  
            clip = mp.VideoFileClip(videosDir+file_)
            clip.audio.write_audiofile(fullAudioDir+os.path.splitext(file_)[0].lower()+'.wav',  fps=44100, nbytes=2,  ffmpeg_params=["-ac", "1"])    #fps=1000, 
            clip.close()
    return            
            