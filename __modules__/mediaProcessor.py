#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:43:43 2022

@author: dmytrenko.o
"""
import sys
stdOutput = open("outlog.log", "w")
sys.stderr = stdOutput
sys.stdout = stdOutput

import os
from scipy.io import wavfile
import moviepy.editor as mp

def audio2parts(audiosDir, sec):
    partsAudioDir = audiosDir+'part_audios/'
    if not os.path.exists(partsAudioDir):
        print ("Directory {0} don't exist!".format(partsAudioDir))
        print ("Creating {0} directory...".format(partsAudioDir))
        os.mkdir(partsAudioDir)
        print ("Directory {0} was created seccsesfuly!".format(partsAudioDir))
        
    name = 0
    for file_ in os.listdir(audiosDir+'full_audios/'):
        samplerate, data = wavfile.read(audiosDir+'full_audios/'+file_)
        print ('Samplerate {0}'.format(samplerate))
        totalSize = len(data)
        ChunkSize = samplerate*sec #1 minute has 60 sec
        amountChunk = int(totalSize/ChunkSize)
        
        for i in range(amountChunk):
            chunkData = data[i*ChunkSize:i*ChunkSize+ChunkSize]
            name += 1
            wavfile.write(partsAudioDir+str(name)+'.wav', samplerate, chunkData)
    return partsAudioDir

def video2wav(videosDir, audiosDir):
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
            