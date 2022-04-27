# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 10:57:26 2021
Edited on Sat Mar 5 05:01:43 2022

@author: dmytr
"""
import sys
stdOutput = open("outlog.log", "a")
sys.stderr = stdOutput
sys.stdout = stdOutput

import os, subprocess
subprocess.run('python -m venv '+os.getcwd()+'/modules/', shell=True)
from __modules__ import defaultLoader, stenogramAnalyser, mediaProcessor

import time
t0 = time.time()

if __name__ == "__main__":
    
    try:
        inputFileDir = sys.argv[1]
    except:
        if not os.path.exists(os.getcwd()+'/videos/'):
            print("Directory './videos/' don't exist") 
            os.mkdir(os.getcwd()+'/videos/')
        inputFileDir =  os.getcwd()+'/videos/'
    
    audiosDir =  os.getcwd()+'/audios/'
    
    mediaProcessor.video2wav(inputFileDir, audiosDir)
    partsAudioDir = mediaProcessor.audio2parts(audiosDir, 15) #30 sec is part of audios
    
    # Add config.json file
    defaultLangs = defaultLoader.load_default_languages(os.getcwd())
    exceptedLangs = defaultLoader.load_except_languages(os.getcwd())
    modelsHashMap = defaultLoader.load_default_modelshashmap(os.getcwd())
    #
    
    templatesHashMap = defaultLoader.load_default_templateshashmap(os.getcwd()+'/templates/')
    
    ukrCount = 0
    rusCount = 0
    mixedCount = 0
    
    voskModels = defaultLoader.load_default_models(os.getcwd()+'/models/', defaultLangs, modelsHashMap)
    
    for audio in os.listdir(partsAudioDir):
        #countTemplates = {"uk" : "", "ru" : ""}
        countTemplates = dict()
        print ('Recognition of: {0}'.format(audio))
        for lang in defaultLangs:
            countTemplates[lang] = stenogramAnalyser.recognizer(partsAudioDir, audio, voskModels[lang], templatesHashMap[lang])         
        if countTemplates["uk"]>countTemplates["ru"]:
            print ('Ukrainian\n')
            sys.stdout = sys.__stdout__
            print ('Ukrainian')
            sys.stdout = stdOutput
            ukrCount += 1
        elif countTemplates["ru"]>countTemplates["uk"]:
            print ('Russian\n')
            sys.stdout = sys.__stdout__
            print ('Russian')
            sys.stdout = stdOutput
            rusCount += 1
        else:
            print ('Mixed\n')
            sys.stdout = sys.__stdout__
            print ('Mixed')
            sys.stdout = stdOutput
            mixedCount += 1
    
    print ('Ukrainian {0}'.format(ukrCount))
    print ('Russian {0}'.format(rusCount))
    print ('Mixed {0}'.format(mixedCount))
    
    print ("\nYou are lucky! The program successfully finished!\n")
    print (time.time() - t0)
    